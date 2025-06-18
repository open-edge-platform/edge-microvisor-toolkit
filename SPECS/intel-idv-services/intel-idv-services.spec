%define systemd_user_dir %{buildroot}/usr/lib/systemd/user
%define systemd_system_dir %{buildroot}/etc/systemd/system

Name:           intel-idv-services
Version:        0.1
Release:        1%{?dist}
Summary:        A package to install scripts and systemd services for Intelligent Desktop Virtualization
Distribution:   Edge Microvisor Toolkit
Vendor:         Intel Corporation
License:        Apache-2.0
URL:            https://github.com/open-edge-platform/edge-desktop-virtualization
Source0:        https://github.com/open-edge-platform/edge-desktop-virtualization/releases/download/pre-release-v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
Requires(post): systemd
Requires(preun): systemd

%description
This package installs the scripts folder to /opt/idv, enables and starts a root-level systemd service, and enables and starts a user-level systemd service.

%prep
%setup -q

%build

%install
# Copy the scripts folder to /opt/idv
mkdir -p %{buildroot}/opt/idv
cp -r init %{buildroot}/opt/idv
cp -r launcher %{buildroot}/opt/idv

# Install the idv-init service and idv-launcher service
mkdir -p %{systemd_user_dir}
install -m 644 idv-init.service %{systemd_user_dir}/idv-init.service
install -m 644 idv-launcher.service %{systemd_user_dir}/idv-launcher.service

# Install the autologin.conf file
mkdir -p %{systemd_system_dir}/getty@tty1.service.d
install -m 644 autologin.conf %{systemd_system_dir}/getty@tty1.service.d/autologin.conf

%files
/opt/idv/
/usr/lib/systemd/user/idv-init.service
/usr/lib/systemd/user/idv-launcher.service
%config(noreplace) /etc/systemd/system/getty@tty1.service.d/autologin.conf

%post
systemctl daemon-reload

%preun
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

    rm -rf /opt/idv/
fi

%changelog
* Wed Jun 18 2025 Dhanya A <dhanya.a@intel.com> - 0.1-4
- Use custom macros for standard path

* Tue Jun 17 2025 Dhanya A <dhanya.a@intel.com> - 0.1-3
- Remove command to create logs file.

* Mon Jun 16 2025 Dhanya A <dhanya.a@intel.com> - 0.1-2
- Initial Edge Microvisor Toolkit import from Fedora 43 (license: MIT). License verified.

* Fri Jun 13 2025 Dhanya A <dhanya.a@intel.com> - 0.1-1
- Initial RPM package for scripts and systemd services
