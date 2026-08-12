import os
import json
import argparse
import re
import git
import subprocess # nosec B404 - subprocess is invoked only with fixed argument lists (shell=False); see get_value_from_make / get_spec_variable_valu
import glob

DIST_TAG = ""
repo_root = ""

# class representation of a patch for a package
class Patch:
    def __init__(self, name, value, desc):
        self.name = name
        self.value = value
        self.desc = desc

    def to_dict(self):
        return {'id': self.name, 'fix_status': self.value, 'description': self.desc}

    def __repr__(self):
        return f"Patch(name={self.name}, value={self.value}, desc={self.desc})"
    
# class representation of a package within a spec file
class Package:
    def __init__(self, name):
        self.name = name
        self.version = []
        self.patches = []

    def add_version(self, version):
        if isinstance(version, str):
            self.version.append(version)
        else:
            raise TypeError("Only strings can be added as versions.")

    def add_patch(self, patch):
        if isinstance(patch, Patch):
            self.patches.append(patch)
        else:
            raise TypeError("Only instances of Patch can be added to the package.")
        self.ensure_unique_patches()

    def remove_patch(self, patch):
        if patch in self.patches:
            self.patches.remove(patch)
        else:
            raise ValueError("Patch not found in the package.")
    
    def ensure_unique_patches(self):
        unique_patches = {}
        for patch in self.patches:
            unique_patches[patch.name] = patch
        self.patches = list(unique_patches.values())

    def to_dict(self):
        return {
            'packages': self.version,
            'cve': [patch.to_dict() for patch in self.patches]
        }

    def __repr__(self):
        return f"Package(name={self.name}, version={self.version}, patches={self.patches})"

# class representation of OS spec
class Spec:
    def __init__(self, name):
        self.name = name
        self.packages = []

    def add_package(self, package):
        if isinstance(package, Package):
            self.packages.append(package)
        else:
            raise TypeError("Only instances of Package can be added.")

    def to_dict(self):
        spec_dict = {}
        for package in self.packages:
            package_dict = {
                'packages': package.version,
                'cve': [patch.to_dict() for patch in package.patches]
            }
            if package.name not in spec_dict:
                spec_dict[package.name] = []
            spec_dict[package.name].append(package_dict)
        return {self.name: spec_dict}

    def __repr__(self):
        return f"Spec(name={self.name}, packages={self.packages})"

# get all .spec files in dir and sub dir
def find_spec_files(folder):
    spec_files = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".spec"):
                spec_files.append(os.path.join(root, file))

    # return list of spec files
    return spec_files

# determine if the entry is patch
def is_patch(key, value):
    # ignore comment line
    if key.startswith(f"#"):
        return False
    
    # determine the line is specifying patch info
    if "patch" in key.lower():
        if ".patch" in value.lower() or ".nopatch" in value.lower():
            return True

    # default return false if not found
    return False

# get all cve id
def get_patchid(value):
    # Define the regex pattern for CVE codes
    # pattern 'CVE-4 digit-1 to 7 digit'
    pattern = r'CVE-\d{4}-\d{1,7}'
    # Find all matches in the text
    matches = re.findall(pattern, value)

    # return list of CVE patches
    return matches

# get patch type
def get_patchtype(value):
    if ".patch" in value.lower():
        return "PATCH"
    if ".nopatch" in value.lower():
        return "NOPATCH"

# get no patch reason assuming its written
# as comment above the nopatch entry
def get_description(value, info, index):
    # empty description if its a patch
    if ".patch" in value.lower():
        return ""
    
    # loop back to extract comment for no patch
    if ".nopatch" in value.lower():
        comments = []
        is_found = False
        # Backward loop based on the current index
        for backward_index in range(index - 1, -1, -1):
            backward_key, backward_value = list(info.items())[backward_index]
            splitter = ":"
            if backward_value == "":
                splitter = ""
            combined_string = backward_key + splitter + backward_value
            if combined_string.startswith(f"#"):
                if "nopatches section" in combined_string.lower():
                    continue
                is_found = True
                clean_combine = combined_string.replace("#", "").strip()
                comments.append(clean_combine)
            else:
                if is_found:
                    break
        # since loop is backward need to reverse it
        reversed_comments = comments[::-1]
        return "\n".join(reversed_comments)

# read each spec file,
# extract cve patches
def read_spec_files(spec_files):
    # init OS spec file with OS version
    spec_object = Spec(get_value_from_make(get_repo_root() +
                                            "/toolkit","RELEASE_MAJOR_ID"))
    
    # extract info from all spec file
    for spec_file in spec_files:
        info = extract_info_from_file(spec_file)
        # determine if CVE patches present
        is_CVE = False
        for index, (key, value) in enumerate(info.items()):
            if is_patch(key, value):
                pacthes = get_patchid(value.upper())
                if pacthes:
                    is_CVE = True
                    break

        # check for no patch cve
        nopatch_files = find_nopatch_files(spec_file)
        if nopatch_files:
            is_CVE = True

        # exclude package if no CVE ID found
        if not is_CVE:
            continue

        # get packages
        package_object = Package(info['Name'].strip())
        package_object.add_version(info['Name'].strip() + "-" + info['Version'].strip() + "-" + info['Release'].strip())
        bunch_of_package = extract_packages_from_file(spec_file)
        for package in bunch_of_package:
            # If {Epoch} available
            # {Name}-{package}-{Epoch}:{Version}-{Release}

            #If {Epoch} not available
            #{Name}-{package}-{Version}-{Release}

            # version and release to use sub-package if exist
            name = info['Name'].strip()
            subname = package['Name'].strip()
            version = info['Version'].strip()
            release = info['Release'].strip()
            if "Version" in package:
                version = package['Version'].strip()
            if "Release" in package:
                release = package['Release'].strip() 

            big_name = name + "-" + subname
            if subname.startswith("$"):
                big_name = subname.replace("$", "").strip()

            if "Epoch" in package: 
                package_object.add_version(big_name + "-" + package['Epoch'].strip() + ":" + version + "-" + release)
            else:
                package_object.add_version(big_name + "-" + version + "-" + release)

        # add no patch from outside (low prio)
        for nopatch in nopatch_files:
            # get clean name
            clean_filenames = os.path.basename(nopatch)

            # get content
            with open(nopatch, "r") as file:
                nopatch_comment = file.read()

            patch_object = Patch(clean_filenames.rstrip('.nopatch'), get_patchtype(clean_filenames), nopatch_comment)
            package_object.add_patch(patch_object)

        # get patches
        for index, (key, value) in enumerate(info.items()):
            if is_patch(key, value):
                pacthes = get_patchid(value.upper())
                # exclude package if no CVE ID found
                if not pacthes:
                    continue
                # get CVE patches
                for patchid in pacthes:
                    patch_object = Patch(patchid, get_patchtype(value), get_description(value,info,index))
                    package_object.add_patch(patch_object)

        # add package to OS spec
        spec_object.add_package(package_object)

    # return single OS spec
    return spec_object

# extract version and name variable
def extract_string(input_string, lines):
    # get strings based on this pattern %{strings}
    pattern = r'%{([^}]*)}'
    if re.search(pattern, input_string):
        return re.sub(pattern, lambda match: translate_string(match.group(1), lines, 0), input_string)
    
    # return original string if cant find match
    return input_string

# translate variable to value
def translate_string(input_string, lines, cnt):
    # get from other file
    if input_string == "?dist":
        global DIST_TAG
        if DIST_TAG != "":
            return DIST_TAG
        DIST_TAG = get_value_from_make(get_repo_root() + "/toolkit","DIST_TAG")
        return DIST_TAG

    max_search = 5
    # get variable from current spec file
    for line in lines:
        if line.startswith(f"%define") or line.startswith(f"%global"):
            parts = line.strip().split()
            if len(parts) >= 3 and parts[1] == input_string:
                pattern = r'%{([^}]*)}'
                if re.search(pattern, parts[2]) and cnt < max_search:
                    n = cnt + 1
                    return re.sub(pattern, lambda match: translate_string(match.group(1), lines, n), parts[2])
                return parts[2]
        # get declared variable
        elif line.upper().startswith(input_string.upper()+":"):
            parts = line.split(':', 1)
            return parts[1].strip()

    # cannot find return empty
    return ""

# run the make file to get value
def get_value_from_make(directory, var):
    try:
        command = ["make", "-s", f"printvar-{var}"]

        result = subprocess.run(
            command,
            cwd=directory,
            text=True,
            capture_output=True,
            check=True,
            shell=False
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return "NotFound"

# extract info of spec file into array
def extract_info_from_file(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    info = {}
    # extract each line to key pair
    for line in lines:
        if ":" in line:
            split_string = line.split(':', 1)
            key = split_string[0]
            value = split_string[1]
            # make unique assume correct version 
            # is at the top of spec file
            if key not in info:
                info[key] = extract_string(value, lines)
        else:
            # save key only
            info[line] = ""
    return info

# extract packages
def extract_packages_from_file(file_name):
    processed_spec = get_spec_variable_value(file_name)
    line = []
    if not processed_spec == "":
        lines = [data.strip() for data in processed_spec.split('\n')]
    else:
        with open(file_name, 'r') as file:
            lines = file.readlines()
    bunch_of_package = []
    package = {}
    is_package = False
    # find %package
    for line in lines:
        # terminate package section
        if is_package:
            if line.startswith(f"%"):
                # Copy the new dictionary
                copied_package = package.copy()
                bunch_of_package.append(copied_package)
                is_package = False
                continue
            # extract key pair
            if ":" in line:
                split_string = line.split(':', 1)
                key = split_string[0]
                value = split_string[1]
                # make unique assume correct version 
                # is at the top of spec file
                if key not in package:
                    package[key] = extract_string(value, lines)
        else:
            if line.startswith(f"%package"):
                package.clear()
                # get name of new package
                split_string = extract_string(line, lines).split()
                name = "not found"
                for isname in split_string:
                    # assume naming format in line %package -n name
                    if not isname.startswith("-") and not isname.startswith(f"%"):
                        if " -n " in line:
                            # indicate absolute name
                            name = "$"+isname
                        else:
                            name = isname
                package["Name"] = name
                is_package = True

    return bunch_of_package

# get processed spec
def get_spec_variable_value(spec_file_path):
    try:
        # Run the rpmspec command to get the spec file data
        result = subprocess.run(['rpmspec', '-P', spec_file_path], capture_output=True, text=True, check=True, shell=False)
        spec_data = result.stdout

        return spec_data
    except subprocess.CalledProcessError as e:
        # ignore error and return empty
        return ""

# get no patch cve list
def find_nopatch_files(file_path):
    # Get the directory of the file
    directory = os.path.dirname(file_path)
    
    # Find all files with the postfix ".nopatch" in the directory
    nopatch_files = glob.glob(os.path.join(directory, "*.nopatch"))
    
    # Return the list of found files
    return nopatch_files

# write to json file
def output_to_text_file(spec_objects):
    outputDir = get_repo_root() + "/build"
    outputFile = outputDir + "/spec_parser.json"
    if not os.path.exists(outputDir):
        os.makedirs(outputDir)
    if os.path.exists(outputFile):
        os.remove(outputFile)
    spec_dict = spec_objects.to_dict()
    with open(outputFile, 'w') as json_file:
        json.dump(spec_dict, json_file, indent=4)

# get repo root directory
def get_repo_root(path='.'):
    global repo_root
    if repo_root != "":
        return repo_root
    repo = git.Repo(path, search_parent_directories=True)
    repo_root = repo.git.rev_parse("--show-toplevel")
    return repo_root

def main(folder):
    # get all CVE patch
    spec_files = find_spec_files(folder)
    spec_objects = read_spec_files(spec_files)
    output_to_text_file(spec_objects)
    print("Output written to "+get_repo_root()+"/build/spec_parser.json")


if __name__ == "__main__":
    # accept a directory input to process
    # or repo root folder by default
    parser = argparse.ArgumentParser(description="Process some directory.")
    parser.add_argument(
        "folder",
        nargs='?',
        default=get_repo_root(),
        help="The directory to process (default: current directory)"
    )

    args = parser.parse_args()
    main(args.folder)
