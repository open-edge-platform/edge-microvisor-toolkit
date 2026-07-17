# Resolves clang15 linking issues
%global _lto_cflags %nil

%bcond_without compat_build
%bcond_without check

%global maj_ver 16
%global min_ver 0
%global patch_ver 6

%if %{with compat_build}
%global pkg_name llvm%{maj_ver}
%global exec_suffix -%{maj_ver}
%global install_prefix %{_libdir}/%{name}
%global install_bindir %{install_prefix}/bin
%global install_includedir %{install_prefix}/include
%global install_libdir %{install_prefix}/lib

%global pkg_bindir %{install_bindir}
%global pkg_includedir %{_includedir}/%{name}
%global pkg_libdir %{install_libdir}
%else
%global pkg_name llvm
%global install_prefix /usr
%global install_libdir %{_libdir}
%global pkg_bindir %{_bindir}
%global pkg_libdir %{install_libdir}
%global exec_suffix %{nil}
%endif


%global build_install_prefix %{buildroot}%{install_prefix}

Summary:        A collection of modular and reusable compiler and toolchain technologies.
Name:		%{pkg_name}
Version:	%{maj_ver}.%{min_ver}.%{patch_ver}
Release:        1%{?dist}
License:        Apache-2.0 WITH LLVM-exception OR NCSA
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit
Group:          Development/Tools
URL:            https://llvm.org/
Source0:        https://github.com/llvm/llvm-project/archive/refs/tags/llvmorg-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  libffi-devel
BuildRequires:  libxml2-devel
BuildRequires:  ninja-build
BuildRequires:  python3-devel
Requires:       libxml2
Provides:       llvm(major) = %{maj_ver}
Provides:       %{name} = %{version}
Provides:       %{name} = %{version}-%{release}

%description
The LLVM Project is a collection of modular and reusable compiler and toolchain technologies. Despite its name, LLVM has little to do with traditional virtual machines, though it does provide helpful libraries that can be used to build them. The name "LLVM" itself is not an acronym; it is the full name of the project.

%package devel
Summary:        Development headers for llvm
Requires:       %{name} = %{version}-%{release}


Provides:	llvm-devel(major) = %{maj_ver}

%description devel
The llvm-devel package contains libraries, header files and documentation
for developing applications that use llvm.

%prep
%autosetup -p1 -n llvm-project-llvmorg-%{version}

%build
# Disable symbol generation
export CFLAGS="`echo " %{build_cflags} " | sed 's/ -g//'`"
export CXXFLAGS="`echo " %{build_cxxflags} " | sed 's/ -g//'`"

mkdir -p build
cd build
cmake -G Ninja                              \
      -DCMAKE_INSTALL_PREFIX=%{install_prefix}     \
      -DLLVM_ENABLE_FFI=ON                  \
      -DLLVM_ENABLE_RTTI=ON                 \
      -DCMAKE_BUILD_TYPE=Release            \
      -DLLVM_PARALLEL_LINK_JOBS=1           \
      -DLLVM_PARALLEL_COMPILE_JOBS=%{?_smp_ncpus_max:%_smp_build_ncpus} \
      -DLLVM_BUILD_LLVM_DYLIB=ON            \
      -DLLVM_LINK_LLVM_DYLIB=ON             \
      -DLLVM_INCLUDE_TESTS=ON               \
      -DLLVM_BUILD_TESTS=ON                 \
      -DLLVM_TARGETS_TO_BUILD="host;AMDGPU;BPF" \
      -DLLVM_INCLUDE_GO_TESTS=No            \
      -DLLVM_ENABLE_RTTI=ON                 \
%if %{without compat_build}
      -DLLVM_BINUTILS_INCDIR=%{_includedir} \
%else
      -DLLVM_INSTALL_UTILS:BOOL=OFF \
%endif
      -Wno-dev ../llvm

%ninja_build LLVM
%ninja_build

%install
%ninja_install -C build

mkdir -p %{buildroot}/%{_bindir}

%if %{with compat_build}

# Add version suffix to binaries
for f in %{buildroot}/%{install_bindir}/*; do
  filename=`basename $f`
  ln -s ../../%{install_bindir}/$filename %{buildroot}/%{_bindir}/$filename%{exec_suffix}
done

# Move header files
mkdir -p %{buildroot}/%{pkg_includedir}
ln -s ../../../%{install_includedir}/llvm %{buildroot}/%{pkg_includedir}/llvm
ln -s ../../../%{install_includedir}/llvm-c %{buildroot}/%{pkg_includedir}/llvm-c

# Fix multi-lib
#%multilib_fix_c_header --file %{install_includedir}/llvm/Config/llvm-config.h

# Create ld.so.conf.d entry
mkdir -p %{buildroot}/etc/ld.so.conf.d
cat >> %{buildroot}/etc/ld.so.conf.d/%{name}-%{_arch}.conf << EOF
%{pkg_libdir}
EOF


# Remove opt-viewer, since this is just a compatibility package.
rm -Rf %{build_install_prefix}/share/opt-viewer

%endif

# llvm-config special casing. llvm-config is managed by update-alternatives.
# the original file must remain available for compatibility with the CMake
# infrastructure. Without compat, cmake points to the symlink, with compat it
# points to the original file.

%if %{without compat_build}

mv %{buildroot}/%{pkg_bindir}/llvm-config %{buildroot}/%{pkg_bindir}/llvm-config%{exec_suffix}-%{__isa_bits}
# We still maintain a versionned symlink for consistency across llvm versions.
# This is specific to the non-compat build and matches the exec prefix for
# compat builds. An isa-agnostic versionned symlink is also maintained in the (un)install
# steps.
(cd %{buildroot}/%{pkg_bindir} ; ln -s llvm-config%{exec_suffix}-%{__isa_bits} llvm-config-%{maj_ver}-%{__isa_bits} )
# ghost presence
touch %{buildroot}%{_bindir}/llvm-config-%{maj_ver}

%else

rm %{buildroot}%{_bindir}/llvm-config%{exec_suffix}
(cd %{buildroot}/%{pkg_bindir} ; ln -s llvm-config llvm-config%{exec_suffix}-%{__isa_bits} )

%endif

# ghost presence
touch %{buildroot}%{_bindir}/llvm-config%{exec_suffix}

cp -Rv cmake/Modules/* %{buildroot}%{pkg_libdir}/cmake/llvm

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%check
# disable security hardening for tests
rm -f $(dirname $(gcc -print-libgcc-file-name))/../specs
%if %{with check}
cd build
ninja check-all
%endif


%files
%defattr(-,root,root)
%{_bindir}/*

%exclude %{_bindir}/llvm-config%{exec_suffix}
%exclude %{pkg_bindir}/llvm-config%{exec_suffix}-%{__isa_bits}

%if %{without compat_build}
%{_libdir}/libLLVM-%{maj_ver}.so
%{_libdir}/libLLVM.so.%{maj_ver}.%{min_ver}
%{_libdir}/libLTO.so*
%{_libdir}/libRemarks.so*
%dir %{_datadir}/opt-viewer
%{_datadir}/opt-viewer/opt-diff.py
%{_datadir}/opt-viewer/opt-stats.py
%{_datadir}/opt-viewer/opt-viewer.py
%{_datadir}/opt-viewer/optpmap.py
%{_datadir}/opt-viewer/optrecord.py
%{_datadir}/opt-viewer/style.css
%else
%{pkg_bindir}
%{pkg_libdir}/libLLVM-%{maj_ver}.so
%config(noreplace) /etc/ld.so.conf.d/%{name}-%{_arch}.conf
%{pkg_libdir}/libLLVM-%{maj_ver}.%{min_ver}*.so
%{pkg_libdir}/libLTO.so*
%exclude %{pkg_libdir}/libLTO.so
%endif
%{pkg_libdir}/libRemarks.so*

%files devel
%if %{without compat_build}
%{_libdir}/*.a
%else
%{_libdir}/%{name}/lib/*.a
%endif

%ghost %{_bindir}/llvm-config%{exec_suffix}
%{pkg_bindir}/llvm-config%{exec_suffix}-%{__isa_bits}

%if %{without compat_build}
%{_includedir}/llvm
%{_includedir}/llvm-c
%{_libdir}/cmake/llvm/*
%{_libdir}/libLLVM.so
%{pkg_bindir}/llvm-config-%{maj_ver}-%{__isa_bits}
%ghost %{_bindir}/llvm-config-%{maj_ver}
%else
%{install_includedir}/llvm
%{install_includedir}/llvm-c
%{pkg_includedir}/llvm
%{pkg_includedir}/llvm-c
%{pkg_libdir}/libLTO.so
%{pkg_libdir}/libLLVM.so
%{pkg_libdir}/cmake/llvm
%endif

%changelog
* Mon Jun 6 2026 Lee Chee Yang <chee.yang.lee@intel.com> - 16.0.6-1
- Add llvm16

* Thu Jul 24 2025 Swee Yee Fonn <swee.yee.fonn@intel.com> - 15.0.7-1
- Upgrade from llvm14 to llvm15.
- Support compat build based on Fedora.

* Tue Dec 24 2024 Naveen Saini <naveen.kumar.saini@intel.com> - 14.0.5-2
- Updated initial changelog entry having fedora version and license info.

* Fri Sep 27 2024 Junxiao Chang <junxiao.chang@intel.com> - 14.0.5-1
- Initial Edge Microvisor Toolkit import from Fedora 36 (license: MIT). License verified.
