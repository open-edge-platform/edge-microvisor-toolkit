%global tinkworkergitpath github.com/open-edge-platform/infra-onboarding

Summary:        In-memory Operating System Installation Environment for Executing Tinkerbell Workflows
Name:           tink-worker
Version:        1.2.2
Release:        2%{?dist}
Distribution:   Edge Microvisor Toolkit
Vendor:         Intel Corporation
License:        Apache-2.0
URL:            github.com/open-edge-platform/infra-onboarding
Source0:        https://%{tinkworkergitpath}/archive/refs/tags/%{name}/v%{version}.tar.gz#/%{name}-v%{version}.tar.gz
Source1:        tink-worker.service
Source2:        tink-worker-v%{version}-vendor.tar.gz

%{?systemd_requires}
BuildRequires:  golang < 1.27
BuildRequires:  golang >= 1.26.2
BuildRequires:  systemd-rpm-macros

%description
The tink-worker will parse the /proc/cmdline in order to retrieve the specific configuration to start for the current/correct machine.
It will begin to execute the workflow/actions associated with that machine.


%prep
%setup -q -n infra-onboarding-%{name}-v%{version}
cd tink-worker
tar -xzf %{SOURCE2} -C .

%build
export GOEXPERIMENT=nosystemcrypto
cd tink-worker
CGO_ENABLED=0 go build -buildmode=pie -mod=vendor -trimpath -gcflags="all=-l" -gcflags="%{tinkworkergitpath}/...=-spectre=all" -asmflags="%{tinkworkergitpath}/...=-spectre=all" -o tink-worker ./cmd/tink-worker

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
* Tue May 5 2026 Andy <andy.peng@intel.com> - 1.2.2-2
- Upgrade golang version to 1.26.2

* Tue Mar 24 2026 Andy <andy.peng@intel.com> - 1.2.2-1
- Upgrade tink-worker version to 1.2.2 for bug fix
- limit to build with golang version < 1.26.0

* Tue Feb 24 2026 Andy <andy.peng@intel.com> - 1.2.0-2
- Upgrade golang version to use 1.25.7

* Tue Feb 3 2026 Andy <andy.peng@intel.com> - 1.2.0-1
- Update version to fix CVE
- CVE-2025-47913
- CVE-2025-61727
- CVE-2025-58181

* Tue Jan 6 2026 Andy <andy.peng@intel.com> - 1.1.5-1
- Update version to fix CVE
- CVE-2025-52881

* Tue Dec 2 2025 Andy <andy.peng@intel.com> - 1.1.4-1
- Update version to fix CVE
- CVE-2025-47913
- CVE-2025-47914
- CVE-2025-52881
- CVE-2024-25621

* Tue Nov 25 2025 Lee Chee Yang <chee.yang.lee@intel.com> - 1.1.2-2
- amend build required golang version

* Mon Nov 3 2025 Andy <andy.peng@intel.com> - 1.1.2-1
- Update tink worker version to 1.1.2

* Fri Oct 3 2025 Lee Chee Yang <chee.yang.lee@intel.com> - 1.1.1-3
- build with golang < 1.25

* Tue Sep 2 2025 Polmoorx shiva kumar <polmoorx.shiva.kumar@intel.com> - 1.1.1-2
- Update go version to use above 1.24.4

* Wed Jun 18 2025 Andy <andy.peng@intel.com> - 1.1.1-1
- Update go version to 1.24.1

* Tue Jun 17 2025 Andy <andy.peng@intel.com> - 1.1.0-1
- Update version to fix grpc CVE

* Tue May 20 2025 Andy <andy.peng@intel.com> - 1.0.0-1
- Original version for Edge Microvisor Toolkit. License verified.
