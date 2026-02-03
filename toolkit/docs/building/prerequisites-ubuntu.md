
# Build Requirements for Edge Microvisor Toolkit on Ubuntu

This page outlines the requirements for building with the Edge Microvisor toolkit on Ubuntu.

## System-Specific Requirements

## Git

Install Git on Ubuntu with the package manager:

```bash
sudo apt-add-repository ppa:git-core/ppa
sudo apt update
sudo apt install git
```

### Golang Package Requirements

The Edge Microvsor toolkit on Ubuntu has been validated with the following:

- **Ubuntu 22.04**: Validated with `golang-1.24.11` from https://go.dev/

## Installation Methods

### Method 1: Using Make Targets (Recommended)

The make targets automatically install the appropriate packages:

```bash
# For interactive development environments (local machines)
# Installs prerequisites but doesn't modify system configuration
sudo make -C toolkit install-prereqs

# Manually install and configure for Go
wget https://go.dev/dl/go1.24.12.linux-amd64.tar.gz && echo "bddf8e653c82429aea7aec2520774e79925d4bb929fe20e67ecc00dd5af44c50 go1.24.12.linux-amd64.tar.gz" | sha256sum -c
sudo rm -rf /usr/local/go
sudo tar -C /usr/local -xzf go1.24.12.linux-amd64.tar.gz

# Manually create Go symlinks for proper PATH integration
sudo ln -sf /usr/local/go/bin/go /usr/bin/go
sudo ln -sf /usr/local/go/bin/gofmt /usr/bin/gofmt

# Manually configure Docker if needed
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker $USER
# Note: You will need to log out and log back in for user changes to take effect

# the above 2 steps can alternatively be done using the following command if preferred:
# sudo ./toolkit/docs/building/prerequisites-ubuntu.sh --no-install-prereqs --fix-go-links --configure-docker

----------------------

# For automated environments (CI/CD pipelines) or complete setup
# Installs prerequisites AND configures Docker and Go links
sudo make -C toolkit install-prereqs-and-configure
```

**Recommendation**:
- Use `install-prereqs` on your local development machine
- Use `install-prereqs-and-configure` in CI/CD pipelines or when you need a complete environment setup

### Method 2: Direct Script Execution

If you prefer running the script directly, you have several options:

```bash
# Basic installation with Go
sudo ./toolkit/docs/building/prerequisites-ubuntu.sh

# Manually install and configure for Go
wget https://go.dev/dl/go1.24.12.linux-amd64.tar.gz && echo "bddf8e653c82429aea7aec2520774e79925d4bb929fe20e67ecc00dd5af44c50 go1.24.12.linux-amd64.tar.gz" | sha256sum -c
sudo rm -rf /usr/local/go
sudo tar -C /usr/local -xzf go1.24.12.linux-amd64.tar.gz

# Manually create Go symlinks for proper PATH integration
sudo ln -sf /usr/local/go/bin/go /usr/bin/go
sudo ln -sf /usr/local/go/bin/gofmt /usr/bin/gofmt

# Manually configure Docker if needed
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker $USER
# Note: You will need to log out and log back in for user changes to take effect

# the above 2 steps can alternatively be done using the following command if preferred:
# sudo ./toolkit/docs/building/prerequisites-ubuntu.sh --no-install-prereqs --fix-go-links --configure-docker
```

## Script Options

The `prerequisites-ubuntu.sh` script supports the following options:

- `--fix-go-links`: Creates symbolic links for Go binaries to make them available in your PATH
- `--configure-docker`: Installs Docker and adds your user to the docker group
- `--no-install-prereqs`: Skips installation of prerequisite packages
- `--help`: Displays usage information

> **Note**: If you use `--configure-docker`, you will need to log out and log back in for the user changes to take effect.
