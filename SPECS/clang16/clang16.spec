# Build compat packages llvmN instead of main package for the current LLVM
# version.
%bcond_without compat_build
%bcond_without check

%global maj_ver 16
%global min_ver 0
%global patch_ver 6
%global clang_version %{maj_ver}.%{min_ver}.%{patch_ver}

%if %{with compat_build}
%global pkg_name clang%{maj_ver}
# Install clang to same prefix as llvm, so that apps that use llvm-config
# will also be able to find clang libs.
%global install_prefix %{_libdir}/llvm%{maj_ver}
%global install_bindir %{install_prefix}/bin
%global install_includedir %{install_prefix}/include
%global install_libdir %{install_prefix}/lib

%global pkg_bindir %{install_bindir}
%global pkg_includedir %{install_includedir}
%global pkg_libdir %{install_libdir}
%else
%global pkg_name clang
%global install_prefix /usr
%global pkg_libdir %{_libdir}
%endif


%global clang_srcdir llvm-project-llvmorg-%{version}

Summary:        C, C++, Objective C and Objective C++ front-end for the LLVM compiler.
Name:           %pkg_name
Version:        %{clang_version}
Release:        1%{?dist}
License:        Apache-2.0 WITH LLVM-exception OR NCSA
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit
Group:          Development/Tools
URL:            https://clang.llvm.org
Source0:        https://github.com/llvm/llvm-project/archive/refs/tags/llvmorg-%{version}.tar.gz



%if %{with compat_build}
# Ensure that clang looks for LLVMgold.so in the directory the compat build
# uses.
Patch100:   fix-lto-path.patch
%endif

BuildRequires:  cmake
BuildRequires:  libxml2-devel
%if %{with compat_build}
BuildRequires:	llvm%{maj_ver}-devel = %{version}
%else
BuildRequires:	llvm-devel = %{version}
%endif
BuildRequires:  ncurses-devel
BuildRequires:  python3-devel
BuildRequires:  zlib-devel
Requires:       %{name}-libs = %{version}-%{release}
Requires:       libstdc++-devel
Requires:       libxml2
%if %{with compat_build}
Requires:       llvm%{maj_ver}
%else
Requires:       llvm
%endif
Requires:       ncurses
Requires:       python3
Requires:       zlib
Provides:	clang(major) = %{maj_ver}

Conflicts:	compiler-rt < 11.0.0

%description
The goal of the Clang project is to create a new C based language front-end: C, C++, Objective C/C++, OpenCL C and others for the LLVM compiler. You can get and build the source today.

%package devel
Summary:        Development headers for clang
License:        NCSA
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-libs = %{version}-%{release}
%if %{without compat_build}
# The clang CMake files reference tools from clang-tools-extra.
Requires:       %{name}-tools-extra = %{version}-%{release}
%endif

%package libs
Summary:        Runtime library for clang
License:        NCSA
Recommends:     compiler-rt%{?_isa} = %{version}
Recommends:     libomp%{_isa} = %{version}
# libomp-devel is required, so clang can find the omp.h header when compiling
# with -fopenmp.
Recommends: libomp-devel%{_isa} = %{version}

%description libs
Runtime library for clang.

%description devel
The clang-devel package contains libraries, header files and documentation
for developing applications that use clang.

%if %{without compat_build}
%package analyzer
Summary:        A source code analysis framework
License:        NCSA AND MIT
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description analyzer
The Clang Static Analyzer consists of both a source code analysis
framework and a standalone tool that finds bugs in C and Objective-C
programs. The standalone tool is invoked from the command-line, and is
intended to run in tandem with a build of a project or code base.

%package -n git-clang-format
Summary:        Integration of clang-format for git
License:        NCSA
Requires:       git
Requires:       python3

%description -n git-clang-format
clang-format integration for git.

%package tools-extra
Summary:        Extra tools for clang
License:        NCSA
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description tools-extra
A set of extra tools built using Clang's tooling API.

%package tools-extra-devel
Summary: Development header files for clang tools
Requires: %{name}-tools-extra = %{version}-%{release}

%description tools-extra-devel
Development header files for clang tools.

%endif


%prep
%setup -q -n %{clang_srcdir}

%py3_shebang_fix \
    clang-tools-extra/clang-tidy/tool/ \
    clang-tools-extra/clang-include-fixer/find-all-symbols/tool/run-find-all-symbols.py

%py3_shebang_fix \
    clang/tools/clang-format/ \
    clang/tools/clang-format/git-clang-format \
    clang/utils/hmaptool/hmaptool \
    clang/tools/scan-view/bin/scan-view \
    clang/tools/scan-view/share/Reporter.py \
    clang/tools/scan-view/share/startfile.py \
    clang/tools/scan-build-py/bin/* \
    clang/tools/scan-build-py/libexec/*

%build
# Disable symbol generation
export CFLAGS="`echo " %{build_cflags} " | sed 's/ -g//'`"
export CXXFLAGS="`echo " %{build_cxxflags} " | sed 's/ -g//'`"

mkdir -p build
cd build
cmake  \
%if %{with compat_build}
       -DLLVM_CMAKE_DIR=%{install_libdir}/cmake/llvm \
       -DCMAKE_INSTALL_PREFIX=%{install_prefix} \
       -DCLANG_INCLUDE_TESTS:BOOL=OFF \
       -DBUILD_SHARED_LIBS=OFF \
%else
       -DCMAKE_INSTALL_PREFIX=%{_prefix}       \
%endif
       -DCLANG_ENABLE_STATIC_ANALYZER:BOOL=ON \
       -DCMAKE_BUILD_TYPE=Release    \
       -DLLVM_ENABLE_EH=ON \
       -DLLVM_ENABLE_RTTI=ON \
       -DCLANG_LINK_CLANG_DYLIB=ON \
       -Wno-dev ../clang

%make_build

%install
cd build
%make_install

%if %{with compat_build}

# Remove binaries/other files
find %{buildroot}%{install_bindir} -type f ! -name clang-%{maj_ver} ! -name clang \
     ! -name clang++ ! -name clang-cl ! -name clang-cpp -delete
rm -Rf %{buildroot}%{install_prefix}/share
rm -Rf %{buildroot}%{install_prefix}/libexec
# Remove scanview-py helper libs
rm -Rf %{buildroot}%{install_prefix}/lib/{libear,libscanbuild}

# Add clang-{version} symlinks
mkdir -p %{buildroot}%{_bindir}
ln -s %{install_bindir}/clang %{buildroot}%{_bindir}/clang-%{maj_ver}
ln -s %{install_bindir}/clang++ %{buildroot}%{_bindir}/clang++-%{maj_ver}
ln -s clang++ %{buildroot}%{install_bindir}/clang++-%{maj_ver}

%else

# Remove emacs integration files.
rm %{buildroot}%{_datadir}/clang/*.el

# Remove editor integrations (bbedit, sublime, emacs, vim).
rm -vf %{buildroot}%{_datadir}/clang/clang-format-bbedit.applescript
rm -vf %{buildroot}%{_datadir}/clang/clang-format-sublime.py*

# Remove HTML docs
rm -Rvf %{buildroot}%{_pkgdocdir}
rm -Rvf %{buildroot}%{_datadir}/clang/clang-doc-default-stylesheet.css
rm -Rvf %{buildroot}%{_datadir}/clang/index.js

# Remove bash autocomplete files.
rm -vf %{buildroot}%{_datadir}/clang/bash-autocomplete.sh

# Add clang++-{version} symlink
ln -s clang++ %{buildroot}%{_bindir}/clang++-%{maj_ver}

%endif

# Create sub-directories in the clang resource directory that will be
# populated by other packages
mkdir -p %{buildroot}%{pkg_libdir}/clang/%{version}/{include,lib,share}/


%if %{without compat_build}
# Add a symlink in /usr/bin to clang-format-diff
ln -s %{_datadir}/clang/clang-format-diff.py %{buildroot}%{_bindir}/clang-format-diff
%endif

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%check
%if %{without compat_build}
%if %{with check}
cd build
make clang-check
%endif
%endif

%files
%defattr(-,root,root)
%{_bindir}/clang-%{maj_ver}
%{_bindir}/clang++-%{maj_ver}
%if %{without compat_build}
%{_bindir}/clang
%{_bindir}/clang++
%{_bindir}/clang-cl
%{_bindir}/clang-cpp
%else
%{pkg_bindir}/clang
%{pkg_bindir}/clang++
%{pkg_bindir}/clang-%{maj_ver}
%{pkg_bindir}/clang++-%{maj_ver}
%{pkg_bindir}/clang-cl
%{pkg_bindir}/clang-cpp
%endif

%files libs
%if %{without compat_build}
%{_libdir}/clang/%{version}/include/*
%{_libdir}/*.so.*
%else
%{pkg_libdir}/*.so.*
%{pkg_libdir}/clang/%{version}/include/*
%endif

%files devel
%defattr(-,root,root)
%if %{without compat_build}
%dir %{_datadir}/clang/
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/cmake/*
%{_includedir}/clang/
%{_includedir}/clang-c/
%else
%{pkg_libdir}/*.so
%{pkg_libdir}/*.a
%{pkg_includedir}/clang/
%{pkg_includedir}/clang-c/
%{pkg_libdir}/cmake/
%endif

%dir %{pkg_libdir}/clang/
%dir %{pkg_libdir}/clang/%{version}/
%dir %{pkg_libdir}/clang/%{version}/include/
%dir %{pkg_libdir}/clang/%{version}/lib/
%dir %{pkg_libdir}/clang/%{version}/share/
%if %{without compat_build}
%{pkg_libdir}/clang/%{maj_ver}
%endif
%if %{without compat_build}
%files analyzer
%{_bindir}/scan-view
%{_bindir}/scan-build
%{_bindir}/analyze-build
%{_bindir}/intercept-build
%{_bindir}/scan-build-py
%{_libexecdir}/ccc-analyzer
%{_libexecdir}/c++-analyzer
%{_libexecdir}/analyze-c++
%{_libexecdir}/analyze-cc
%{_libexecdir}/intercept-c++
%{_libexecdir}/intercept-cc
%{_datadir}/scan-view/
%{_datadir}/scan-build/
%{_mandir}/man1/scan-build.1.*
%{_libdir}/libear/*
%{_libdir}/libscanbuild/*

%files -n git-clang-format
%{_bindir}/git-clang-format

%files tools-extra
%{_bindir}/clang-apply-replacements
%{_bindir}/clang-change-namespace
%{_bindir}/clang-check
%{_bindir}/clang-doc
%{_bindir}/clang-extdef-mapping
%{_bindir}/clang-format
%{_bindir}/clang-include-fixer
%{_bindir}/clang-move
%{_bindir}/clang-offload-bundler
%{_bindir}/clang-offload-packager
%{_bindir}/clang-offload-wrapper
%{_bindir}/clang-linker-wrapper
%{_bindir}/clang-nvlink-wrapper
%{_bindir}/clang-pseudo
%{_bindir}/clang-query
%{_bindir}/clang-refactor
%{_bindir}/clang-rename
%{_bindir}/clang-reorder-fields
%{_bindir}/clang-repl
%{_bindir}/clang-scan-deps
%{_bindir}/clang-tidy
%{_bindir}/clangd
%{_bindir}/diagtool
%{_bindir}/hmaptool
%{_bindir}/pp-trace
%{_bindir}/c-index-test
%{_bindir}/find-all-symbols
%{_bindir}/modularize
%{_bindir}/clang-format-diff
%{_datadir}/clang/clang-format.py*
%{_datadir}/clang/clang-format-diff.py*
%{_datadir}/clang/clang-include-fixer.py*
%{_datadir}/clang/clang-tidy-diff.py*
%{_bindir}/run-clang-tidy
%{_datadir}/clang/run-find-all-symbols.py*
%{_datadir}/clang/clang-rename.py*
%{_libdir}/libear/__init__.py
%{_libdir}/libear/config.h.in
%{_libdir}/libear/ear.c
%{_libdir}/libscanbuild/__init__.py
%{_libdir}/libscanbuild/analyze.py
%{_libdir}/libscanbuild/arguments.py
%{_libdir}/libscanbuild/clang.py
%{_libdir}/libscanbuild/compilation.py
%{_libdir}/libscanbuild/intercept.py
%{_libdir}/libscanbuild/report.py
%{_libdir}/libscanbuild/resources/scanview.css
%{_libdir}/libscanbuild/resources/selectable.js
%{_libdir}/libscanbuild/resources/sorttable.js
%{_libdir}/libscanbuild/shell.py
%{_libexecdir}/analyze-c++
%{_libexecdir}/analyze-cc
%{_libexecdir}/intercept-c++
%{_libexecdir}/intercept-cc

%files tools-extra-devel
%{_includedir}/clang-tidy/

%endif
%changelog
* Tue Jul 7 2026 Andy <andy.peng@intel.com> - 16.0.6-1
- Upgrade from llvm15 to llvm16

* Thu Jul 24 2025 Swee Yee Fonn <swee.yee.fonn@intel.com> - 15.0.7-1
- Upgrade from llvm14 to llvm15
- Support compat build based on Fedora.

* Mon Dec 23 2024 Naveen Saini <naveen.kumar.saini@intel.com@intel.com> - 14.0.5-2
- Updated initial log entry having fedora version.

* Fri Sep 27 2024 Junxiao Chang <junxiao.chang@intel.com> - 14.0.5-1
- Initial Edge Microvisor Toolkit import from Fedora 36 (license: MIT). License verified.
