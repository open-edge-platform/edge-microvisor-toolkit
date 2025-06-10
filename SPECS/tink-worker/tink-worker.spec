%global tinkworkergitpath github.com/tinkerbell/tink

Summary:        In-memory Operating System Installation Environment for Executing Tinkerbell Workflows
Name:           tink-worker
Version:        0.10.0
Release:        1%{?dist}
Distribution:   Edge Microvisor Toolkit
Vendor:         Intel Corporation
License:        Apache-2.0
URL:            https://tinkerbell.org
Source0:        https://%{tinkworkergitpath}/archive/v%{version}/tink-%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        tink-worker.service
Source2:        tink-worker-%{version}-vendor.tar.gz
Patch0:         tink-worker.patch

%{?systemd_requires}

BuildRequires:  golang >= 1.23
BuildRequires:  systemd-rpm-macros

%description
The tink-worker will parse the /proc/cmdline in order to retrieve the specific configuration to start for the current/correct machine.
It will begin to execute the workflow/actions associated with that machine.


%prep
%setup -q -n tink-%{version}
%patch 0 -p1
tar -xzf %{SOURCE2} -C .

%build
CGO_ENABLED=0 go build -buildmode=pie -mod=vendor -trimpath -gcflags="all=-spectre=all -l" -asmflags="all=-spectre=all" -o tink-worker ./cmd/tink-worker

%install
install -D -p -m 0755 -t %{buildroot}%{_bindir} ./tink-worker

# systemd units
install -Dp -m0644 %{SOURCE1} %{buildroot}%{_unitdir}/tink-worker.service

%post
%systemd_post tink-worker.service

%files
%{_bindir}/tink-worker
%{_unitdir}/tink-worker.service

%changelog
* Tue May 20 2025 Andy <andy.peng@intel.com> - 0.10.0-1
- Original version for Edge Microvisor Toolkit. License verified.