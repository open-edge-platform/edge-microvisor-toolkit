%global llvm_compat 16
%global debug_package %{nil}

Name:           vc-intrinsics
Version:        0.25.0
Release:        1%{?dist}
Summary:        New intrinsics on top of core LLVM %{?llvm_compat} IR instructions
License:        MIT
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit
URL:            https://github.com/intel/vc-intrinsics
Source0:        %{url}/archive/v%{version}/%{name}-v%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  llvm%{?llvm_compat}-devel

%description
VC Intrinsics project contains a set of new intrinsics on top of core LLVM %{?llvm_compat} IR instructions
that represent SIMD semantics of a program targeting GPU.

%package devel
Summary: Development files for LLVM %{?llvm_compat} VC Intrinsics

%description devel
This package contains libraries and header files for
developing against %{upstream_name} built against LLVM %{?llvm_compat}.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%if 0%{?llvm_compat}
%cmake -DLLVM_DIR=%{_libdir}/llvm%{?llvm_compat}/lib/cmake -DCMAKE_BUILD_TYPE=Release -DLLVM_INCLUDE_TESTS=OFF -DBUILD_SHARED_LIBS:BOOL=OFF
%else
%cmake -DLLVM_DIR=%%{_libdir}/cmake/llvm -DCMAKE_BUILD_TYPE=Release -DLLVM_INCLUDE_TESTS=OFF -DBUILD_SHARED_LIBS:BOOL=OFF
%endif
%cmake_build

%install
%cmake_install

%files devel
%license LICENSE.md
%{_libdir}/libLLVMGenXIntrinsics.a
%{_libdir}/cmake/VCIntrinsics*/*
%{_libdir}/cmake/LLVMGenXIntrinsics/*
%{_includedir}/llvm/GenXIntrinsics/*

%doc
%changelog
* Tue Jul 7 2026 Andy <andy.peng@intel.com> - 0.25.0-1
- Update version to 0.25.0.

* Thu Jul 24 2025 Swee Yee Fonn <swee.yee.fonn@intel.com> - 0.22.1-1
- Update to v0.22.1 and upgrade to build against llvm15.

* Tue Dec 24 2024 Naveen Saini <naveen.kumar.saini@intel.com> - 0.19.0-2
- Updated initial changelog entry having fedora version and license info.

* Fri Sep 27 2024 Junxiao Chang <junxiao.chang@intel.com> - 0.19.0-1
- Initial Edge Microvisor Toolkit import from Fedora 41 (license: MIT). License verified.
