%global tinkworkergitpath github.com/open-edge-platform/infra-onboarding

Summary:        In-memory Operating System Installation Environment for Executing Tinkerbell Workflows
Name:           tink-worker
Version:        1.0.0
Release:        1%{?dist}
Distribution:   Edge Microvisor Toolkit
Vendor:         Intel Corporation
License:        Apache-2.0
URL:            github.com/open-edge-platform/infra-onboarding
Source0:        https://%{tinkworkergitpath}/archive/refs/tags/%{name}/v%{version}.tar.gz#/%{name}-v%{version}.tar.gz
Source1:        tink-worker.service
Source2:        tink-worker-v%{version}-vendor.tar.gz

%{?systemd_requires}

BuildRequires:  golang >= 1.23
BuildRequires:  systemd-rpm-macros

%description
The tink-worker will parse the /proc/cmdline in order to retrieve the specific configuration to start for the current/correct machine.
It will begin to execute the workflow/actions associated with that machine.


%prep
%setup -q -n infra-onboarding-%{name}-v%{version}
cd tink-worker
tar -xzf %{SOURCE2} -C .

%build
cd tink-worker
CGO_ENABLED=0 go build -buildmode=pie -mod=vendor -trimpath -gcflags="all=-spectre=all -l" -asmflags="all=-spectre=all" -o tink-worker ./cmd/tink-worker

%install
cd tink-worker
install -D -p -m 0755 -t %{buildroot}%{_bindir} ./tink-worker

# systemd units
install -Dp -m0644 %{SOURCE1} %{buildroot}%{_unitdir}/tink-worker.service

%post
%systemd_post tink-worker.service

%files
%{_bindir}/tink-worker
%{_unitdir}/tink-worker.service

%changelog
* Tue May 20 2025 Andy <andy.peng@intel.com> - 1.0.0-1
- Original version for Edge Microvisor Toolkit. License verified.