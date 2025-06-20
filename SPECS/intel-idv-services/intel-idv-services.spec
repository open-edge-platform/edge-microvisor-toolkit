%define systemd_user_dir %{buildroot}/usr/lib/systemd/user
%define systemd_system_dir %{buildroot}/etc/systemd/system
%define local_bin_dir %{buildroot}/usr/local/bin

Name:           intel-idv-services
Version:        0.1
Release:        1%{?dist}
Summary:        A package to install scripts and systemd services for Intelligent Desktop Virtualization(IDV)
Distribution:   Edge Microvisor Toolkit
Vendor:         Intel Corporation
License:        Apache-2.0
URL:            https://github.com/open-edge-platform/edge-desktop-virtualization
Source0:        https://github.com/open-edge-platform/edge-desktop-virtualization/releases/download/pre-release-v%{version}/%{name}-%{version}.tar.gz
Source1:        90-default.preset

BuildArch:      noarch
Requires(post): systemd
Requires(preun): systemd

%description
This package installs the scripts and services that are needed to run IDV solution

%prep
%setup -q

%build

%install
# Copy the scripts folder to /usr/local/bin/idv
mkdir -p %{local_bin_dir}/idv
cp -r init %{local_bin_dir}/idv
cp -r launcher %{local_bin_dir}/idv

# Install the idv-init service. This service sets up the environment required for running virtual machines
mkdir -p %{systemd_user_dir}
install -m 644 idv-init.service %{systemd_user_dir}/idv-init.service

# Install the idv-launcher service. This service launches virtual machines based on the configuration specified in the launcher/vm.conf file.
install -m 644 idv-launcher.service %{systemd_user_dir}/idv-launcher.service

# Install the autologin.conf file. This enables autologin for a specified user.
mkdir -p %{systemd_system_dir}/getty@tty1.service.d
install -m 644 autologin.conf %{systemd_system_dir}/getty@tty1.service.d/autologin.conf

# Default presets for user
mkdir -p %{buildroot}/usr/lib/systemd/user-preset
install -m 644 %{SOURCE1} -t %{buildroot}/usr/lib/systemd/user-preset/

%files
/usr/local/bin/idv/*
/usr/lib/systemd/user/idv-*.service
%config(noreplace) /etc/systemd/system/getty@tty1.service.d/autologin.conf
/usr/lib/systemd/user-preset/90-default.preset

%post
systemctl daemon-reload

%preun
set -e
# Stop and disable the idv-init service before uninstalling
if [ $1 -eq 0 ]; then
    USER_ID=$(id -u $SUDO_USER)
    export XDG_RUNTIME_DIR=/run/user/$USER_ID
    if [ -d "$XDG_RUNTIME_DIR" ]; then
        sudo -u $SUDO_USER XDG_RUNTIME_DIR=$XDG_RUNTIME_DIR systemctl --user stop idv-init.service
        sudo -u $SUDO_USER XDG_RUNTIME_DIR=$XDG_RUNTIME_DIR systemctl --user disable idv-init.service

        sudo -u $SUDO_USER XDG_RUNTIME_DIR=$XDG_RUNTIME_DIR systemctl --user stop idv-launcher.service
        sudo -u $SUDO_USER XDG_RUNTIME_DIR=$XDG_RUNTIME_DIR systemctl --user disable idv-launcher.service
    fi
fi

%changelog
* Fri Jun 20 2025 Dhanya A <dhanya.a@intel.com> - 0.1-6
- Update comment in spec file

* Thu Jun 19 2025 Dhanya A <dhanya.a@intel.com> - 0.1-5
- Copy scripts to bin directory and add preset file

* Wed Jun 18 2025 Dhanya A <dhanya.a@intel.com> - 0.1-4
- Use custom macros for standard path

* Tue Jun 17 2025 Dhanya A <dhanya.a@intel.com> - 0.1-3
- Remove command to create logs file.

* Mon Jun 16 2025 Dhanya A <dhanya.a@intel.com> - 0.1-2
- Initial Edge Microvisor Toolkit import from Fedora 43 (license: MIT). License verified.

* Fri Jun 13 2025 Dhanya A <dhanya.a@intel.com> - 0.1-1
- Initial RPM package for scripts and systemd services
