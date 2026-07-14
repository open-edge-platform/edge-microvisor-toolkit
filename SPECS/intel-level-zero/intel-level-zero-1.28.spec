Summary:        OneAPI Level Zero Specification Headers and Loader
Name:           intel-level-zero
Version:        1.28.2
Release:        1%{?dist}
License:        MIT
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit
URL:            https://github.com/oneapi-src/level-zero
Source:         https://github.com/oneapi-src/level-zero/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
ExclusiveArch:  x86_64
BuildRequires:  chrpath
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  make
#BuildRequires:  opencl-headers
BuildRequires:  spdlog-devel
# Useful for a quick oneAPI Level-Zero testing
Recommends:     %{name}-zello_world

%description
The objective of the oneAPI Level-Zero Application Programming Interface
(API) is to provide direct-to-metal interfaces to offload accelerator
devices. Its programming interface can be tailored to any device needs
and can be adapted to support broader set of languages features such as
function pointers, virtual functions, unified memory,
and I/O capabilities.

%package        devel
Summary:        The oneAPI Level Zero Specification Headers and Loader development package
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains library and header files for
developing applications that use %{name}.

%package        zello_world
Summary:        The oneAPI Level Zero quick test package with zello_world binary
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    zello_world
The %{name}-zello_world package contains a zello_world binary which is capable of a quick test
of the oneAPI Level-Zero driver and dumping out the basic device and driver characteristics.

%prep
%autosetup -p1 -n level-zero-%{version}

%build
# spdlog uses fmt, but since this doesn't setup linking, use it in header only mode
export CXXFLAGS="%{build_cxxflags} -DFMT_HEADER_ONLY=1"
%cmake -DSYSTEM_SPDLOG=ON
%cmake_build

%install
%cmake_install
# Install also the zello_world binary to ease up testing of the l0
mkdir -p %{buildroot}%{_bindir}/
install -p -m 755 ./bin/zello_world %{buildroot}%{_bindir}/zello_world
chrpath --delete %{buildroot}%{_bindir}/zello_world

%files
%license LICENSE
%doc README.md SECURITY.md
%{_libdir}/libze_loader.so.%{version}
%{_libdir}/libze_loader.so.1
%{_libdir}/libze_validation_layer.so.%{version}
%{_libdir}/libze_validation_layer.so.1
%{_libdir}/libze_tracing_layer.so.%{version}
%{_libdir}/libze_tracing_layer.so.1

%files zello_world
%{_bindir}/zello_world

%files devel
%{_includedir}/level_zero
%{_libdir}/libze_loader.so
%{_libdir}/libze_validation_layer.so
%{_libdir}/libze_tracing_layer.so
%{_libdir}/pkgconfig/libze_loader.pc
%{_libdir}/pkgconfig/level-zero.pc

%changelog
* Mon Jul 6 2026 Andy <andy.peng@intel.com> - 1.28.2-1
- Update version to 1.28.2.

* Wed Apr 22 2026 Andy <andy.peng@intel.com> - 1.27.0-1
- Update version to 1.27.0.

* Mon Jan 19 2026 Andy <andy.peng@intel.com> - 1.24.2-1
- Update version to 1.24.2.

* Wed Aug 08 2025 Polmoorx Shiva Kumar <polmoorx.shiva.kumar@intel.com> - 1.21.9-2
- Update to use the system installed spdlog

* Mon Jul 21 2025 Swee Yee Fonn <swee.yee.fonn@intel.com> - 1.21.9-1
- Update version to 1.21.9.

* Fri Dec 27 2024 Naveen Saini <naveen.kumar.saini@intel.com> - 1.17.44-2
- Update Source URL.

* Thu Oct 03 2024 Mun Chun Yep <mun.chun.yep@intel.com> - 1.17.44-1
- Initial Edge Microvisor Toolkit import from Fedora 42 (license: MIT). License verified.
