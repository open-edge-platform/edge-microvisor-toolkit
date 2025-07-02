Name:           intel-idv-services
Version:        1.0.0~rc1
Release:        1%{?dist}
Summary:        A package to install scripts and systemd services for Intelligent Desktop Virtualization(IDV)
Distribution:   Edge Microvisor Toolkit
Vendor:         Intel Corporation
License:        Apache-2.0
URL:            https://github.com/open-edge-platform/edge-desktop-virtualization
Source0:        https://github.com/open-edge-platform/edge-desktop-virtualization/releases/download/%{version_no_tilde}/%{name}-%{version_no_tilde}.tar.gz

BuildArch:       noarch
BuildRequires:   systemd-rpm-macros
Requires(post):  systemd
Requires(preun): systemd

%description
The intel-idv-services package introduces two key services:

idv-init.service:
This service sets up the environment required for running virtual machines. It performs tasks such as enumerating SR-IOV virtual functions, configuring display settings, starting the X server, and launching Openbox.
This is a prerequisite for launching the virtual machines with SR-IOV capabilities.

idv-launcher.service:
This service launches virtual machines based on the configuration specified in the vm.conf file. The VMs are displayed in full-screen mode on their respective monitors with USB passthrough enabled.

%prep
%setup -q -n %{name}-%{version_no_tilde}

%build

%install
# Copy the scripts folder to bindir
mkdir -p %{buildroot}%{_bindir}/idv
cp -r init %{buildroot}%{_bindir}/idv
cp -r launcher %{buildroot}%{_bindir}/idv

# Install the idv-init service. This service sets up the environment required for running virtual machines
mkdir -p %{buildroot}%{_userunitdir}
install -m 644 idv-init.service %{buildroot}%{_userunitdir}/idv-init.service

# Install the idv-launcher service. This service launches virtual machines based on the configuration specified in the launcher/vm.conf file.
install -m 644 idv-launcher.service %{buildroot}%{_userunitdir}/idv-launcher.service

# Install the autologin.conf file. This enables autologin for a specified user.
mkdir -p %{buildroot}%{_sysconfdir}/systemd/system/getty@tty1.service.d
install -m 644 autologin.conf %{buildroot}%{_sysconfdir}/systemd/system/getty@tty1.service.d/autologin.conf

%files
%{_bindir}/idv/*
%{_userunitdir}/idv-*.service
%config(noreplace) %{_sysconfdir}/systemd/system/getty@tty1.service.d/autologin.conf

%post

%preun

%changelog
* Wed Jul 02 2025 Dhanya A <dhanya.a@intel.com> - 1.0.0~rc1-1
- Bump up version to v1.0.0~rc1

* Fri Jun 27 2025 Dhanya A <dhanya.a@intel.com> - 0.2-1
- Remove logging to a log file in shell scripts

* Wed Jun 25 2025 Dhanya A <dhanya.a@intel.com> - 0.1-1
- Original version for Edge Microvisor Toolkit. License verified.
