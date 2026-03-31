%global mfx_ver_major 2
%global mfx_ver_minor 16

Name:           intel-vpl-gpu-rt
Version:        25.4.6
Release:        1%{?dist}
Summary:        Intel Video Processing Library (Intel VPL) GPU Runtime
License:        MIT
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit
URL:            https://www.intel.com/content/www/us/en/developer/tools/oneapi/onevpl.html
ExclusiveArch:  x86_64

Source0:        https://github.com/intel/vpl-gpu-rt/archive/intel-onevpl-%{version}/intel-onevpl-%{version}.tar.gz

Patch0001: 0001-avce-Use-VDEnc-for-YUY2-AYUV-RGB-formats.patch
Patch0002: 0002-AVC10b-Decode-feature.patch
Patch0003: 0003-Enable-HEVC-VDENC-422-for-MTL-ARL.patch
Patch0004: 0004-Correct-luma-and-chroma-offsets-linux.patch
Patch0005: 0005-Add-NVL-platform-support-to-build-configuration.patch
Patch0006: 0006-Add-new-device-IDs-for-NVL-S.patch
Patch0007: 0005-Enable-AV1-422-decode.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libvpl-devel >= 2.11.0
BuildRequires:  libva-devel >= 2.22.0
BuildRequires:  pkgconfig(libdrm) >= 2.4
# Should be >= 1.9 but fails with libva < 2.12 (VAProcFilterCap3DLUT):
# https://github.com/oneapi-src/oneVPL-intel-gpu/issues/198
BuildRequires:  pkgconfig(libva) >= 1.12

Requires:       libvpl%{?_isa} >= 1:2.10.1

Obsoletes:      oneVPL-intel-gpu < %{version}-%{release}
Provides:       oneVPL-intel-gpu = %{version}-%{release}

%description
Intel oneVPL GPU Runtime is a Runtime implementation of oneVPL API for Intel Gen
GPUs. Runtime provides access to hardware-accelerated video decode, encode and
filtering.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1 -n vpl-gpu-rt-intel-onevpl-%{version}

%build
%cmake
%cmake_build
%install
%cmake_install
%files
%license LICENSE
%doc README.md CONTRIBUTING.md
%{_libdir}/libmfx-gen.so.1.%{mfx_ver_major}
%{_libdir}/libmfx-gen.so.1.%{mfx_ver_major}.%{mfx_ver_minor}
%dir %{_libdir}/libmfx-gen
%{_libdir}/libmfx-gen/enctools.so

%files devel
%{_libdir}/libmfx-gen.so
%{_libdir}/pkgconfig/libmfx-gen.pc

%changelog
* Wed Apr 1 2026 Lishan Liu <lishan.liu@intel.com> - 25.4.6-1
- Upgraded to version 25.4.6

* Thu Jul 10 2025 Swee Yee Fonn<swee.yee.fonn@intel.com> - 25.2.3-1
- Upgraded to version 25.2.3

* Tue Dec 24 2024 Naveen Saini <naveen.kumar.saini@intel.com> - 24.2.5-2
- Updated initial changelog entry having fedora version and license info.

* Sept. 10, 2024 Junxiao Chang <junxiao.chang@intel.com> - 24.2.5-1
- Initial Edge Microvisor Toolkit import from Fedora 40 (license: MIT). License verified.
