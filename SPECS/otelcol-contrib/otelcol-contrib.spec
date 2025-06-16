Summary:        OpenTelemetry Collector Contrib
Name:           otelcol-contrib
Version:        0.117.0
Release:        4%{?dist}
License:        Apache-2.0
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit
Group:          Tools
URL:            https://github.com/open-telemetry/opentelemetry-collector-releases
#see create-vendor-tarball.sh for how to create this
Source0:        %{url}/releases/download/v%{version}/%{name}_%{version}_linux_amd64.tar.gz#/%{name}-%{version}-vendored.tar.gz
Source1:        otelcol_contrib.te
Source2:        otelcol_contrib.fc
Patch0:         CVE-2025-22872.patch
BuildRequires:  golang
BuildRequires:  make
BuildRequires:  systemd-rpm-macros
Requires:       (%{name}-selinux if selinux-policy-targeted)

%description
%{summary}

%global selinuxtype targeted
%global modulename  otelcol_contrib

%package        selinux
Summary:        %{name} SELinux policy
Requires:       %{name} = %{version}-%{release}
BuildRequires:  selinux-policy
BuildRequires:  selinux-policy-devel
BuildArch:      noarch
%{?selinux_requires}

%description    selinux
SELinux policy for %{name}.

%prep
%autosetup -p1

%build
cd _build
go build -trimpath -o otelcol-contrib -mod=vendor
cd -

mkdir selinux
cp -p %{SOURCE1} selinux/
cp -p %{SOURCE2} selinux/
make -f %{_datadir}/selinux/devel/Makefile %{modulename}.pp

%install
mkdir -p %{buildroot}/%{_bindir}
install -p -m 755 _build/otelcol-contrib %{buildroot}%{_bindir}/otelcol-contrib

mkdir -p %{buildroot}%{_datadir}/selinux/packages
install -m 644 %{modulename}.pp %{buildroot}%{_datadir}/selinux/packages/%{modulename}.pp

%files
%license LICENSE
%{_bindir}/otelcol-contrib

%files selinux
%{_datadir}/selinux/packages/%{modulename}.pp

%post selinux
%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/%{modulename}.pp

%postun selinux
%selinux_modules_uninstall -s %{selinuxtype} %{modulename}

%changelog
* Fri Jun 13 2025 Tham Jing Hui <jing.hui.tham@intel.com> - 0.117.0-4
- Include patch for CVE-2025-22872

* Fri Mar 21 2025 Anuj Mittal <anuj.mittal@intel.com> - 0.117.0-3
- Bump Release to rebuild

* Thu Jan 16 2025 Christopher Nolan <christopher.nolan@intel.com> - 0.117.0-2
- Remove install of configuration and service files

* Thu Jan 09 2025 Tadeusz Matenko <tadeusz.matenko@intel.com> - 0.117.0-1
- Upgrade to version 0.117.0. Fixes CVE-2024-45338.

* Mon Jan 06 2025 Naveen Saini <naveen.kumar.saini@intel.com> - 0.113.0-5
- Update Source URLs.

* Fri Dec 20 2024 Tan Jia Yong <jia.yong.tan@intel.com> - 0.113.0-4
- Fix SELinux policy

* Mon Dec 16 2024 Tadeusz Matenko <tadeusz.matenko@intel.com> - 0.113.0-3
- Require SELinux subpackage if selinux-policy-targeted is present

* Fri Dec 13 2024 Tadeusz Matenko <tadeusz.matenko@intel.com> - 0.113.0-2
- Add SELinux subpackage

* Tue Nov 12 2024 Tadeusz Matenko <tadeusz.matenko@intel.com> - 0.113.0-1
- Upgrade to version 0.113.0

* Mon Oct 21 2024 Christopher Nolan <christopher.nolan@intel.com> - 0.111.0-1
- Upgrade to version 0.111.0

* Tue Sep 24 2024 Christopher Nolan <christopher.nolan@intel.com> - 0.104.0-3
- Modify generated vendor source tar to only include the required plugins

* Fri Aug 30 2024 Naveen Saini <naveen.kumar.saini@intel.com> - 0.104.0-2
- Build vendor source tar from opentelemetry-collector-releases

* Wed Jul 24 2024 Naveen Saini <naveen.kumar.saini@intel.com> - 0.104.0-1
- Original version for Edge Microvisor Toolkit. License verified.
