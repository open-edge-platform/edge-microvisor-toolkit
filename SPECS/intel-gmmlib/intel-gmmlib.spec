Name:           intel-gmmlib
Version:        22.9.0
Release:        1%{?dist}
Summary:        Intel Graphics Memory Management Library
License:        MIT
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit
URL:            https://github.com/intel/gmmlib
Source0:        %{url}/archive/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++

%description
The Intel Graphics Memory Management Library provides device specific
and buffer management for the Intel Graphics Compute Runtime for OpenCL
and the Intel Media Driver for VAAPI.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1 -n gmmlib-intel-gmmlib-%{version}
# Fix license perm
chmod -x LICENSE.md README.rst
# Fix source code perm
find Source -name "*.cpp" -exec chmod -x {} ';'
find Source -name "*.h" -exec chmod -x {} ';'


%build
mkdir build && cd build
%cmake \
  -DRUN_TEST_SUITE:BOOL=False ..

%cmake_build

%install
%make_install -C build

%ldconfig_scriptlets

%files
%license LICENSE.md
%doc README.rst
%{_libdir}/libigdgmm.so.12*

%files devel
%{_includedir}/igdgmm
%{_libdir}/libigdgmm.so
%{_libdir}/pkgconfig/igdgmm.pc

%changelog
* Tue Mar 10 2026 Andy <andy.peng@intel.com> - 22.9.0-1
- Upgraded to version 22.9.0.

* Fri Jul 11 2025 Liang Yang <liang1.yang@intel.com> - 22.7.1-1
- Upgraded to version 22.7.1.

* Tue Dec 24 2024 Naveen Saini <naveen.kumar.saini@intel.com> - 22.5.1-2
- Updated initial changelog entry having fedora version and license info.

* Sept. 10, 2024 Junxiao Chang <junxiao.chang@intel.com> - 22.5.1-1
- Initial Edge Microvisor Toolkit import from Fedora 41 (license: MIT). License verified.
