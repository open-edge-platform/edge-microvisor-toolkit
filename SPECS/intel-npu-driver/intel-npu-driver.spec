Summary:	    Intel Neural Processing Unit Driver
Name:		    intel-npu-driver
Version:	    1.34.0
Release:	    1%{?dist}
License:	    MIT AND Apache-2.0
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit
URL:		    https://github.com/intel/linux-npu-driver
Source0:	    %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-v%{version}.tar.gz
Source1:	    https://github.com/intel/level-zero-npu-extensions/archive/f9ad3bf89c2418d714aef2e6b96a5aafb12a1971/level-zero-npu-extensions-f9ad3bf.tar.gz
Source2:	    https://github.com/intel-innersource/libraries.ai.npu.elf/archive/eca361b16892e3035f95c03bfb7f8d53ad2c8ef7/libraries.ai.npu.elf-eca361b.tar.gz

ExclusiveArch:	x86_64

# Disable LTO - the project builds static libraries (.a) with LTO bitcode
# objects that the BFD linker cannot resolve, causing undefined reference
# errors when linking unit tests.
%define _lto_cflags %{nil}

BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:	glibc-devel
BuildRequires:	gmock-devel
BuildRequires:	gtest-devel
BuildRequires:	libudev-devel
BuildRequires:	intel-level-zero-devel >= 1.28.2
BuildRequires:	openssl-devel
BuildRequires:	yaml-cpp-devel

Requires:	intel-level-zero

%description
Intel NPU device is an AI inference accelerator integrated with Intel client CPUs, starting from Intel Core Ultra generation of CPUs (formerly known as Meteor Lake).
It enables energy-efficient execution of artificial neural network tasks.


%prep
%setup -q -n drivers.vpu.linux.client-npu-1.34.0-release_ttl_presilicon-20260619-27819362393

# thirdparty deps
rm -rf thirdparty/googletest thirdparty/level-zero third_party/level-zero-npu-extensions \
   thirdparty/perfetto thirdparty/yaml-cpp third_party/npu_elf
tar xf %{SOURCE1}
mv level-zero-npu-extensions-* third_party/level-zero-npu-extensions
tar xf %{SOURCE2}
mv libraries.ai.npu.elf-* third_party/npu_elf

sed -i '/include(cmake\/googletest.cmake)/s/^/#/' third_party/CMakeLists.txt
sed -i '/include(cmake\/yaml-cpp.cmake)/s/^/#/' third_party/CMakeLists.txt
sed -i '/include(cmake\/movi-scripts.cmake)/s/^/#/' third_party/CMakeLists.txt

# Fix system yaml-cpp cmake config referencing non-existent static library
sed -i 's|/usr/lib/libyaml-cpp.a|/usr/lib64/libyaml-cpp.so|' /usr/lib/cmake/yaml-cpp/yaml-cpp-targets.cmake

%build
cmake \
	-B build -S . \
	-DENABLE_VALIDATION_BUILD=OFF \
	-DENABLE_NPU_COMPILER_BUILD=OFF \
	-DENABLE_NPU_COMPILER_DOWNLOAD=OFF \
	-DENABLE_NPU_FIRMWARE_API_DOWNLOAD=OFF

cmake --build build --target ze_intel_npu

%install
mkdir -p %{buildroot}%{_libdir}
cmake --install build --prefix=%{buildroot}%{_libdir}
cp -a %{buildroot}%{_libdir}/lib64/libze_intel_npu.so.* %{buildroot}%{_libdir}
rm -rf %{buildroot}%{_libdir}/lib64

%files
%defattr(-,root,root)
%license LICENSE.md
%doc README.md
%{_libdir}/libze_intel_npu.so*

%changelog
* Thu Jul 2 2026 Andy <andy.peng@intel.com> - 1.33.0-1
- Update version to v1.33.0

* Tue Apr 14 2026 Andy <andy.peng@intel.com> - 1.32.0-1
- Upgrade version to 1.32.0.

* Fri Apr 3 2026 Andy <andy.peng@intel.com> - 1.30.0-1
- Upgrade version to 1.30.0.

* Mon Jan 19 2026 Andy <andy.peng@intel.com> - 1.28.0-1
- Initial Edge Microvisor Toolkit import from Fedora 42 (license: MIT). License verified.
