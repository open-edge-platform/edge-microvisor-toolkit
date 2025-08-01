Name:           spirv-llvm-translator
Version:        18.1.1
Release:        1%{?dist}
Summary:        LLVM to SPIRV Translator
License:        NCSA
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit
URL:            https://github.com/KhronosGroup/SPIRV-LLVM-Translator
Source0:        %{url}/archive/v%{version}/%{name}-v%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  llvm-devel
BuildRequires:  spirv-headers-devel
BuildRequires:  spirv-tools-devel
BuildRequires:  zlib-devel

%description
Khronos LLVM to SPIRV Translator. This is a library
to be used by Mesa for OpenCL support. It translate
LLVM IR to Khronos SPIR-V. It also includes a
standalone tool used for building libclc.

%package devel
Summary: Development files for LLVM to SPIRV Translator
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains libraries and header files for
developing against %{name}

%package tools
Summary: Standalone llvm to spirv translator tool
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
       -DLLVM_DIR="/usr/lib/cmake/llvm/" \
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
* Tue Aug 01 2025 Jayanth kintali<jayanthx.kintali@intel.com> - 18.1.1-1
- Upgrade the spirv-llvm-translator component version from 14.0.3s to 18.1.1

* Tue Dec 24 2024 Naveen Saini <naveen.kumar.saini@intel.com> - 14.0.3-2
- Updated initial changelog entry having fedora version and license info.

* Fri Sep 27 2024 Junxiao Chang <junxiao.chang@intel.com> - 14.0.3-1
- Initial Edge Microvisor Toolkit import from Fedora 36 (license: MIT). License verified.
