Summary:        Intel Graphics System Controller Firmware Update Library
Name:           intel-igsc
Version:        0.9.5
Release:        2%{?dist}
License:        Apache-2.0
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit
URL:            https://github.com/intel/igsc
Source0:        https://github.com/intel/igsc/archive/refs/tags/V%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  intel-metee-devel
BuildRequires:  libudev-devel
BuildRequires:  syslog-ng-devel

%description
The Intel Graphics System Firmware Update Library (IGSC FUL) is a pure C low
level library that exposes a required API to perform a firmware update of a
particular Intel discrete graphics device. The library utilized a cross platform
library metee in order to access the GSC (mei) device. GSC device is an
extension of the Intel discrete graphics device (dGFX).

%package devel
Summary:    Development files for %{name}
Requires:   %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for %{name}.

%prep
%autosetup -n igsc-%{version}

%build
%cmake -G Ninja
%cmake_build

%install
%cmake_install

%files
%license LICENSE.txt
%doc README.md SECURITY.md
%{_bindir}/igsc
%{_libdir}/libigsc.so.%{version}

%files devel
%{_includedir}/igsc_lib.h
%{_libdir}/libigsc.so
%{_libdir}/libigsc.so.0
%{_libdir}/cmake/igsc/igsc*.cmake

%changelog
* Wed Jan 21 2026 Lishan Liu <lishan.liu@intel.com> - 0.9.5-2
- Bump release to rebuild with latest metee
 
* Tue Jul 22 2025 Swee Yee Fonn <swee.yee.fonn@intel.com> - 0.9.5-1
- Upgrade to 0.9.5

* Tue Dec 31 2024 Naveen Saini <naveen.kumar.saini@intel.com> - 0.9.4-2
- Update Source URL.

* Mon Oct 07 2024 Mun Chun Yep <mun.chun.yep@intel.com> - 0.9.4-1
- Original version for Edge Microvisor Toolkit. License verified.
