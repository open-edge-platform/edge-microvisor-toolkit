Summary:	    Intel Neural Processing Unit Driver
Name:		    intel-npu-driver
Version:	    1.28.0
Release:	    1%{?dist}
License:	    MIT AND Apache-2.0
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit
URL:		    https://github.com/intel/linux-npu-driver
Source0:	    %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-v%{version}.tar.gz
Source1:	    https://github.com/intel/level-zero-npu-extensions/archive/61e4aeb00afd2a5b6955986269eed3a713c7b562/level-zero-npu-extensions-61e4aeb.tar.gz
Source2:	    https://github.com/openvinotoolkit/npu_compiler_elf/archive/9d91134722e70bf52297adaeb221a0be8e408b14/npu_compiler_elf-9d91134.tar.gz

ExclusiveArch:	x86_64

BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:	glibc-devel
BuildRequires:	gmock-devel
BuildRequires:	gtest-devel
BuildRequires:	libudev-devel
BuildRequires:	intel-level-zero-devel
BuildRequires:	openssl-devel
BuildRequires:	yaml-cpp-devel

Requires:	intel-level-zero

%description
Intel NPU device is an AI inference accelerator integrated with Intel client CPUs, starting from Intel Core Ultra generation of CPUs (formerly known as Meteor Lake).
It enables energy-efficient execution of artificial neural network tasks.


%prep
%setup -q -n linux-npu-driver-%{version}

# thirdparty deps
rm -rf thirdparty/googletest thirdparty/level-zero third_party/level-zero-npu-extensions \
   thirdparty/perfetto thirdparty/yaml-cpp third_party/npu_compiler_elf
tar xf %{SOURCE1}
mv level-zero-npu-extensions-* third_party/level-zero-npu-extensions
tar xf %{SOURCE2}
mv npu_compiler_elf-* third_party/npu_compiler_elf

sed -i '/add_subdirectory(googletest EXCLUDE_FROM_ALL)/s/^/#/' third_party/CMakeLists.txt
sed -i '/add_subdirectory(yaml-cpp EXCLUDE_FROM_ALL)/s/^/#/' third_party/CMakeLists.txt

%build
cmake \
	-B build -S . \
	-DENABLE_VALIDATION_BUILD=OFF \
	-DENABLE_NPU_COMPILER_BUILD=OFF

cmake --build build

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
* Mon Jan 19 2026 Andy <andy.peng@intel.com> - 1.28.0-1
- Initial Edge Microvisor Toolkit import from Fedora 42 (license: MIT). License verified.
