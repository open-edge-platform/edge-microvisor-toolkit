Name:           intel-media-driver
Version:        25.2.3
Release:        1%{?dist}
Summary:        The Intel Media Driver for VAAPI
License:        MIT and BSD-3-Clause
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit
URL:        https://github.com/intel/media-driver

# Original source has non-free and/or patented files, use following on the original source!
# $ python3 strip.py
# ref. https://github.com/intel/media-driver/wiki/Media-Driver-Shaders-(EU-Kernels)#build-with-open-source-shaders

Source0:    https://github.com/intel/media-driver/archive/refs/tags/intel-media-%{version}.tar.gz

# This is an Intel only vaapi backend
ExclusiveArch:  x86_64

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(igdgmm)
BuildRequires:  libva-devel
BuildRequires:  libpciaccess-devel
BuildRequires:  libdrm-devel
BuildRequires:  pkgconfig(x11)

%description
The Intel Media Driver for VAAPI is a new VA-API (Video Acceleration API)
user mode driver supporting hardware accelerated decoding, encoding,
and video post processing for GEN based graphics hardware.
https://01.org/intel-media-for-linux

%package -n     libva-intel-media-driver
Summary:        The Intel Media Driver for VAAPI.

%description -n libva-intel-media-driver
%{description}

%package -n     libigfxcmrt
Summary:        Library to load own GPU kernels on render engine via Intel media driver.
Requires:       libva-intel-media-driver%{?_isa} = %{version}-%{release}

%description -n libigfxcmrt
libigfxcmrt is a runtime library needed when user wants to execute their own GPU kernels on render engine.
It calls Intel media driver to load the kernels and allocate the resources.
It provides a set of APIs for user to call directly from application.

%package -n     libigfxcmrt-devel
Summary:        Development files for libigfxcmrt
Requires:       libigfxcmrt%{?_isa} = %{version}-%{release}

%description -n libigfxcmrt-devel
The libigfxcmrt-devel package contains libraries and header files for
developing applications that use libigfxcmrt.

%prep
%autosetup -p1 -n media-driver-intel-media-%{version}%{?pre}
# Fix license perm
chmod -x LICENSE.md README.md CMakeLists.txt

# Remove pre-built (but unused) files
rm -rv Tools/MediaDriverTools/UMDPerfProfiler/MediaPerfParser

%build
mkdir build && cd build
%cmake \
  -DLIBVA_DRIVERS_PATH=%{_libdir}/dri \
  -DMEDIA_BUILD_FATAL_WARNINGS=OFF \
  ..

%cmake_build
%install
cd build
%make_install
# Fix perm on library to be stripped
chmod +x %{buildroot}%{_libdir}/dri/iHD_drv_video.so

# TODO - have pci based hw detection
%if 0
fn=%{buildroot}%{_metainfodir}/intel-media-driver.metainfo.xml
%{SOURCE9} src/i965_pciids.h | xargs appstream-util add-provide ${fn} modalias
%endif

%files -n libva-intel-media-driver
%doc README.md
%license LICENSE.md
%{_libdir}/dri/iHD_drv_video.so

%files -n libigfxcmrt
%{_libdir}/libigfxcmrt.so.*

%files -n libigfxcmrt-devel
%{_libdir}/libigfxcmrt.so
%{_includedir}/igfxcmrt
%{_libdir}/pkgconfig/igfxcmrt.pc

%changelog
* Fri Jul 11 2025 Liang Yang <liang1.yang@intel.com> - 25.2.3-1
- Upgraded to version 25.2.3.

* Tue Dec 24 2024 Naveen Saini <naveen.kumar.saini@intel.com> - 24.2.5-2
- Updated initial changelog entry having fedora version and license info.

* Sept. 10, 2024 Junxiao Chang <junxiao.chang@intel.com> - 24.2.5-1
- Initial Edge Microvisor Toolkit import from Fedora 40 (license: MIT). License verified.
