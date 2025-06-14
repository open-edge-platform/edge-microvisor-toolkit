Name:           idv-solution
Version:        1.0
Release:        1%{?dist}
Summary:        A package to install scripts and systemd services

License:        Proprietary
Source0:        https://github.com/open-edge-platform/edge-desktop-virtualization/releases/download/pre-release-v0.1/%{name}-%{version}.tar.gz

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

# Create log file
touch %{buildroot}/opt/idv/launcher/start_all_vms.log

# Install the idv-init service
mkdir -p %{buildroot}/usr/lib/systemd/user/
install -m 644 idv-init.service %{buildroot}/usr/lib/systemd/user/idv-init.service

# Install the idv-launcher service
mkdir -p %{buildroot}/usr/lib/systemd/user/
install -m 644 idv-launcher.service %{buildroot}/usr/lib/systemd/user/idv-launcher.service

# Install the autologin.conf file
mkdir -p %{buildroot}/etc/systemd/system/getty@tty1.service.d
install -m 644 autologin.conf %{buildroot}/etc/systemd/system/getty@tty1.service.d/autologin.conf

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
* Sat Jun 14 2025 Dhanya A <dhanya.a@intel.com> - 1.0-1
- Initial RPM package for scripts and systemd services
