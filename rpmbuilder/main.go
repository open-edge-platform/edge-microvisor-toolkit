// RPM Builder - Standalone tool to build RPM packages from spec files
package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"os/exec"
	"path/filepath"
	"strings"
	"sync"
)

type RPMBuilder struct {
	specsDir    string
	buildDir    string
	srpmsDir    string
	rpmsDir     string
	workers     int
	maxPackages int // For testing - limit number of packages to build
}

func NewRPMBuilder(specsDir string, workers int, maxPackages int) *RPMBuilder {
	return &RPMBuilder{
		specsDir:    specsDir,
		buildDir:    "BUILD",
		srpmsDir:    "SRPMS",
		rpmsDir:     "RPMS",
		workers:     workers,
		maxPackages: maxPackages,
	}
}

func (rb *RPMBuilder) createDirectories() error {
	dirs := []string{rb.buildDir, rb.srpmsDir, rb.rpmsDir}
	for _, dir := range dirs {
		if err := os.MkdirAll(dir, 0755); err != nil {
			return fmt.Errorf("failed to create directory %s: %v", dir, err)
		}
	}
	return nil
}

func (rb *RPMBuilder) findSpecFiles() ([]string, error) {
	var specFiles []string

	err := filepath.Walk(rb.specsDir, func(path string, info os.FileInfo, err error) error {
		if err != nil {
			return err
		}
		if strings.HasSuffix(info.Name(), ".spec") {
			specFiles = append(specFiles, path)
			// Limit for testing
			if rb.maxPackages > 0 && len(specFiles) >= rb.maxPackages {
				return filepath.SkipAll
			}
		}
		return nil
	})

	return specFiles, err
}

func (rb *RPMBuilder) getPackageName(specFile string) (string, error) {
	file, err := os.Open(specFile)
	if err != nil {
		return "", err
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := strings.TrimSpace(scanner.Text())
		if strings.HasPrefix(line, "Name:") {
			parts := strings.Fields(line)
			if len(parts) > 1 {
				return parts[1], nil
			}
		}
	}
	return "", fmt.Errorf("package name not found in %s", specFile)
}

func (rb *RPMBuilder) buildSRPM(specFile string) error {
	packageName, err := rb.getPackageName(specFile)
	if err != nil {
		return fmt.Errorf("failed to get package name: %v", err)
	}

	fmt.Printf("Building SRPM for %s...\n", packageName)

	cmd := exec.Command("rpmbuild",
		"-bs",
		"--define", fmt.Sprintf("_topdir %s", filepath.Dir(rb.specsDir)),
		"--define", fmt.Sprintf("_builddir %s", rb.buildDir),
		"--define", fmt.Sprintf("_srcrpmdir %s", rb.srpmsDir),
		specFile,
	)

	output, err := cmd.CombinedOutput()
	if err != nil {
		return fmt.Errorf("SRPM build failed for %s: %v\nOutput: %s", packageName, err, output)
	}

	fmt.Printf("✓ SRPM built successfully for %s\n", packageName)
	return nil
}

func (rb *RPMBuilder) buildWorker(jobs <-chan string, results chan<- error, wg *sync.WaitGroup, buildType string) {
	defer wg.Done()

	for specFile := range jobs {
		var err error
		switch buildType {
		case "srpm":
			err = rb.buildSRPM(specFile)
		}
		results <- err
	}
}

func (rb *RPMBuilder) buildAll(specFiles []string, buildType string) []error {
	jobs := make(chan string, len(specFiles))
	results := make(chan error, len(specFiles))

	var wg sync.WaitGroup

	// Start workers
	for i := 0; i < rb.workers; i++ {
		wg.Add(1)
		go rb.buildWorker(jobs, results, &wg, buildType)
	}

	// Send jobs
	for _, specFile := range specFiles {
		jobs <- specFile
	}
	close(jobs)

	// Wait for completion
	wg.Wait()
	close(results)

	// Collect errors
	var errors []error
	for err := range results {
		if err != nil {
			errors = append(errors, err)
		}
	}

	return errors
}

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Usage: go run main.go <SPECS_DIR> [workers] [max_packages]")
		fmt.Println("  SPECS_DIR: Directory containing .spec files")
		fmt.Println("  workers: Number of parallel workers (default: 2)")
		fmt.Println("  max_packages: Max number of packages to build (default: 3, 0 for all)")
		os.Exit(1)
	}

	specsDir := os.Args[1]
	workers := 2
	maxPackages := 3 // Default to 3 packages for testing

	if len(os.Args) > 2 {
		fmt.Sscanf(os.Args[2], "%d", &workers)
	}

	if len(os.Args) > 3 {
		fmt.Sscanf(os.Args[3], "%d", &maxPackages)
	}

	builder := NewRPMBuilder(specsDir, workers, maxPackages)

	// Create build directories
	if err := builder.createDirectories(); err != nil {
		log.Fatalf("Failed to create directories: %v", err)
	}

	// Find spec files (limited for testing)
	specFiles, err := builder.findSpecFiles()
	if err != nil {
		log.Fatalf("Failed to find spec files: %v", err)
	}

	if len(specFiles) == 0 {
		log.Fatalf("No .spec files found in %s", specsDir)
	}

	fmt.Printf("Found %d spec files for testing:\n", len(specFiles))
	for _, spec := range specFiles {
		fmt.Printf("  - %s\n", spec)
	}

	// Build packages (only SRPMs for testing)
	fmt.Println("\n=== Building SRPMs ===")
	if errors := builder.buildAll(specFiles, "srpm"); len(errors) > 0 {
		fmt.Printf("\n❌ SRPM build errors:\n")
		for _, err := range errors {
			fmt.Printf("  - %v\n", err)
		}
	} else {
		fmt.Printf("\n✅ All SRPMs built successfully!\n")
	}
}
