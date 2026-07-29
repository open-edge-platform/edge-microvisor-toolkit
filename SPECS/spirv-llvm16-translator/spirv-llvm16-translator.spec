%global llvm_compat 16

Name:           spirv-llvm16-translator
Version:        16.0.23
Release:        1%{?dist}
Summary:        LLVM %{?llvm_compat} to SPIRV Translator
License:        NCSA
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit
URL:            https://github.com/KhronosGroup/SPIRV-LLVM-Translator
Source0:        %{url}/archive/v%{version}/spirv-llvm-translator-v%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  llvm%{llvm_compat}-devel
BuildRequires:  spirv-headers-devel
BuildRequires:  spirv-tools-devel
BuildRequires:  zlib-devel

%description
Khronos LLVM %{llvm_compat} to SPIRV Translator. This is a library
that is used by Mesa and compute-runtime for OpenCL support.
It translates LLVM IR to Khronos SPIR-V. It also includes a
standalone tool used for building libclc.

%package devel
Summary: Development files for LLVM %{llvm_compat} to SPIRV Translator
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains libraries and header files for
developing against %{name}

%package tools
Summary: Standalone llvm %{llvm_compat} to spirv translator tool
Requires: %{name}%{?_isa} = %{version}-%{release}

%description tools
This package contains the standalone llvm to spirv tool.

%prep
%autosetup -n SPIRV-LLVM-Translator-%{version} -p1

%build
%cmake -GNinja \
       -DLLVM_BUILD_TOOLS=ON \
       -DCMAKE_BUILD_TYPE=Release \
       -DCMAKE_INSTALL_RPATH:BOOL=";" \
%if 0%{?llvm_compat}
       -DLLVM_DIR=%{_libdir}/llvm%{?llvm_compat}/lib/cmake/llvm \
%else
       -DLLVM_DIR="/usr/lib/cmake/llvm/" \
%endif
       -DBUILD_SHARED_LIBS=YES \
       -DLLVM_EXTERNAL_PROJECTS="SPIRV-Headers" \
       -DLLVM_EXTERNAL_SPIRV_HEADERS_SOURCE_DIR="/usr/include/spirv/"

%cmake_build

%install
%cmake_install

%files
%doc README.md
%{_libdir}/libLLVMSPIRVLib.so.*

%files tools
%{_bindir}/llvm-spirv

%files devel
%dir %{_includedir}/LLVMSPIRVLib/
%{_includedir}/LLVMSPIRVLib/
%{_libdir}/libLLVMSPIRVLib.so
%{_libdir}/pkgconfig/LLVMSPIRVLib.pc

%changelog
* Wed Jul 8 2026 Andy <andy.peng@intel.com> - 16.0.23-1
- Initial Edge Microvisor Toolkit import from Fedora 38 (license: MIT). License verified.
