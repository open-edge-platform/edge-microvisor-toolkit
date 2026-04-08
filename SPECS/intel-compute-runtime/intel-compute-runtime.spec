%global neo_major 25
%global neo_minor 40
%global neo_build 35563.4

%global optflags %{optflags} -Wno-error=maybe-uninitialized

Name:           intel-compute-runtime
Version:        %{neo_major}.%{neo_minor}.%{neo_build}
Release:        1%{?dist}
Summary: Intel Graphics Compute Runtime for oneAPI Level Zero and OpenCL

#LTO is controlled in compute-runtime itself, but temp disable it here
%global _lto_cflags %{nil}

License:        MIT
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit
URL:            https://github.com/intel/compute-runtime
Source0:        %{url}/archive/%{version}/compute-runtime-%{version}.tar.gz

# This is just for Intel GPUs
ExclusiveArch:  x86_64

BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  intel-gmmlib-devel >= 22.7.0
BuildRequires:  libva-devel >= 2.2.0
BuildRequires:  libdrm-devel
BuildRequires:  intel-igc-devel >= 2.11.7
BuildRequires:  ninja-build
BuildRequires:  ocl-icd-devel
BuildRequires:  opencl-headers
BuildRequires:  intel-level-zero-devel >= 1.21.9
BuildRequires:  intel-igsc-devel >= 0.9.5

# This doesn't get added automatically, so specify it explicitly
Requires:       intel-igc >= 2.11.7

# Let compute-runtime be a meta package for intel-ocloc, intel-opencl and intel-level-zero
Requires:       intel-ocloc = %{version}-%{release}
Requires:       intel-opencl = %{version}-%{release}
Requires:       intel-level-zero-gpu = %{version}-%{release}

# prelim/drm
Provides: bundled(drm-uapi-helper)

%description
The Intel Graphics Compute Runtime for oneAPI Level Zero and OpenCL
Driver is an open-source project supporting computations for Intel graphics
hardware architectures using oneAPI Level Zero and Open Computing Language
(OpenCL) APIs.

%package -n    intel-ocloc
Summary:       Tool for managing Intel Compute GPU device binary format

%description -n intel-ocloc
ocloc is a tool for managing Intel Compute GPU device binary format (a format
used by Intel Compute GPU runtime). It can be used for generation (as part of
'compile' command) as well as manipulation (decoding/modifying - as part of
'disasm'/'asm' commands) of such binary files.

%package -n    intel-ocloc-devel
Summary:       Tool for managing Intel Compute GPU device binary format - Devel Files
Requires:      intel-ocloc%{?_isa} = %{version}-%{release}

%description -n intel-ocloc-devel
Devel files (headers and libraries) for developing against
intel-ocloc (a tool for managing Intel Compute GPU device binary format).

%package -n    intel-opencl
Summary:       OpenCL support implementation for Intel GPUs
Requires:      intel-igc-libs%{?_isa}
Requires:      intel-gmmlib%{?_isa}

%description -n intel-opencl
Implementation for the Intel GPUs of the OpenCL specification - a generic
compute oriented API. This code base contains the code to run OpenCL programs
on Intel GPUs which basically defines and implements the OpenCL host functions
required to initialize the device, create the command queues, the kernels and
the programs and run them on the GPU.

%package -n    intel-level-zero-gpu
Summary:       oneAPI L0 support implementation for Intel GPUs
Requires:      intel-igc-libs%{?_isa}
Requires:      intel-gmmlib%{?_isa}
# In some references, the package is named intel-level-zero-gpu, so provide that for convenience too
Provides:      intel-level-zero-gpu%{?_isa}

%description -n intel-level-zero-gpu
Runtime library providing the ability to use Intel GPUs with the oneAPI Level
Zero programming interface. Level Zero is the primary low-level interface for
language and runtime libraries. Level Zero offers fine-grain control over
accelerators capabilities, delivering a simplified and low-latency interface to
hardware, and efficiently exposing hardware capabilities to applications.

%package -n    intel-level-zero-gpu-devel
Summary:       oneAPI L0 support implementation for Intel GPUs - Devel Files
Requires:      intel-level-zero-gpu%{?_isa} = %{version}-%{release}

%description -n intel-level-zero-gpu-devel
Devel files for developing against intel-level-zero

%prep
%autosetup -p1 -n compute-runtime-%{version}

# remove sse2neon completely as we're building just for x86(_64)
rm -rv third_party/sse2neon

%build
# -DNEO_DISABLE_LD_GOLD=1 for https://bugzilla.redhat.com/show_bug.cgi?id=2043178 and https://bugzilla.redhat.com/show_bug.cgi?id=2043758
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DNEO_OCL_VERSION_MAJOR=%{neo_major} \
    -DNEO_OCL_VERSION_MINOR=%{neo_minor} \
    -DNEO_VERSION_BUILD=%{neo_build} \
    -DSKIP_UNIT_TESTS=1 \
    -DNEO_DISABLE_LD_GOLD=1 \
    -DNEO_ENABLE_I915_PRELIM_DETECTION=TRUE \
    -DNEO_ENABLE_XE_PRELIM_DETECTION=TRUE

%cmake_build

%install
%cmake_install
# Symlink to provide ocloc
pushd %{buildroot}%{_bindir}
ln -s ocloc-* ocloc
popd

%files

%files -n intel-opencl
%license LICENSE.md
%dir %{_libdir}/intel-opencl/
%{_libdir}/intel-opencl/libigdrcl.so
%{_sysconfdir}/OpenCL/vendors/intel.icd

%files -n intel-level-zero-gpu
%license LICENSE.md
%{_libdir}/libze_intel_gpu.so.*

%files -n intel-level-zero-gpu-devel
%{_includedir}/level_zero/*.h
%{_includedir}/level_zero/driver_experimental/*.h

%files -n intel-ocloc
%license LICENSE.md
%{_bindir}/ocloc
%{_bindir}/ocloc-*
%{_libdir}/libocloc.so

%files -n intel-ocloc-devel
%{_includedir}/ocloc_api.h

%doc
%changelog
* Mon Mar 9 2026 Andy <andy.peng@intel.com> - 25.40.35563.4-1
- Update version to 25.40.35563.4.

* Mon Jul 21 2025 Swee Yee Fonn <swee.yee.fonn@intel.com> - 25.18.33578.6-1
- Update version to 25.18.33578.6.

* Mon Dec 23 2024 Naveen Saini <naveen.kumar.saini@intel.com> - 24.35.30872.22-3
- Update initial changelog entry having fedora version and license info.

* Mon Nov 18 2024 Junxiao Chang <junxiao.chang@intel.com> - 24.35.30872.22-2
- Adding intel level zero plugin package

* Fri Sep 27 2024 Junxiao Chang <junxiao.chang@intel.com> - 24.35.30872.22-1
- Initial Edge Microvisor Toolkit import from Fedora 41 (license: MIT). License verified.
