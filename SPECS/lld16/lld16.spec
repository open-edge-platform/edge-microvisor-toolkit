
%bcond_without check
%bcond_without compat_build

%global lld_srcdir llvm-project-llvmorg-%{version}
%global maj_ver 16
%global min_ver 0
%global patch_ver 6

%if %{with compat_build}
%global pkg_name lld%{maj_ver}
%global install_prefix %{_libdir}/llvm%{maj_ver}
%global install_includedir %{install_prefix}/include
%global install_libdir %{install_prefix}/lib
%else
%global pkg_name lld
%global install_prefix /usr
%global install_includedir %{_includedir}
%global install_libdir %{_libdir}
%endif


Summary:        LLD is a linker from the LLVM project that is a drop-in replacement for system linkers and runs much faster than them
Name:           %{pkg_name}
Version:        %{maj_ver}.%{min_ver}.%{patch_ver}
Release:        1%{?dist}
License:        Apache-2.0 WITH LLVM-exception OR NCSA
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit
Group:          Development/Tools
URL:            https://lld.llvm.org/
Source0:        https://github.com/llvm/llvm-project/archive/refs/tags/llvmorg-%{version}.tar.gz

BuildRequires:  build-essential
BuildRequires:  cmake
BuildRequires:  file
%if %{with compat_build}
BuildRequires:	llvm%{maj_ver}-devel = %{version}
%else
BuildRequires:	llvm-devel = %{version}
%endif
BuildRequires:  ninja-build
BuildRequires:  python3
Requires:       %{name}-libs = %{version}-%{release}

%package devel
Summary:        Libraries and header files for LLD
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%if %{without compat_build}
# lld tools are referenced in the cmake files, so we need to add lld as a
# dependency.
Requires:       %{name} = %{version}-%{release}
%endif

%package libs
Summary:        LLD shared libraries

%description
The LLVM project linker.

%description devel
This package contains library and header files needed to develop new native
programs that use the LLD infrastructure.

%description libs
Shared libraries for LLD.

%prep
%autosetup -n %{lld_srcdir}

%if %{with compat_build}
# For compat builds, we don't want to build the actual lld binary. While there is an
# LLD_BUILD_TOOLS cmake option, it is incomplete in various ways (e.g. still leaves install
# targets and symlinks), so instead skip the tools/lld build entirely.
# We can't simply delete the binaries after the fact, because this would leave checks for
# their existence in the cmake exports.
sed 's/add_subdirectory(tools\/lld)//' -i lld/CMakeLists.txt
%endif

%build
mkdir -p build
cd build
%cmake \
       -G Ninja                                                   \
       -DCMAKE_BUILD_TYPE=Release                                 \
       -DCMAKE_SKIP_RPATH:BOOL=on                                 \
       -DCMAKE_C_FLAGS=-I../../libunwind-%{version}.src/include   \
       -DCMAKE_CXX_FLAGS=-I../../libunwind-%{version}.src/include \
       -DLLVM_LINK_LLVM_DYLIB:BOOL=on                             \
       -DCMAKE_INSTALL_PREFIX=%{install_prefix}                   \
       -DBUILD_SHARED_LIBS:BOOL=ON                                \
       -DLLVM_DYLIB_COMPONENTS="all"                              \
%if %{with compat_build}
        -DLLVM_DIR=%{install_libdir}/cmake/llvm \
        -DLLVM_INCLUDE_TESTS=OFF \
%else
        -DLLVM_DIR=%{_libdir}/cmake/llvm                           \
        -DLLVM_INCLUDE_TESTS=ON \
%endif
       -Wno-dev                                                   \
       ../lld

%ninja_build

%install
cd build
%ninja_install

%if %{without compat_build}
%files
%license LICENSE.TXT
%{_bindir}/lld*
%{_bindir}/ld.lld
%{_bindir}/ld64.lld
%{_bindir}/wasm-ld
%endif

%files devel
%{install_includedir}/lld
%{install_libdir}/liblld*.so
%{install_libdir}/cmake/lld/

%files libs
%{install_libdir}/liblld*.so.*

%changelog
* Tue Jul 7 2026 Andy <andy.peng@intel.com> - 16.0.6-1
- Upgrade from llvm15 to llvm16

* Thu Jul 24 2025 Swee Yee Fonn <swee.yee.fonn@intel.com> - 15.0.7-1
- Upgrade from llvm14 to llvm15
- Modify for compat build as per Fedora 43.

* Tue Dec 24 2024 Naveen Saini <naveen.kumar.saini@intel.com> - 14.0.5-2
- Updated initial changelog entry having fedora version and license info.

* Fri Sep 27 2024 Junxiao Chang <junxiao.chang@intel.com> - 14.0.5-1
- Initial Edge Microvisor Toolkit import from Fedora 36 (license: MIT). License verified.
