Summary:        Intel XPU System Management Interface
Name:           intel-xpu-smi
Version:        1.2.39
Release:        4%{?dist}
License:        MIT
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit
URL:            https://github.com/intel/xpumanager
Source0:        https://github.com/intel/xpumanager/archive/refs/tags/V%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  glibc-static >= 2.38-10%{?dist}
BuildRequires:  libpciaccess-devel
BuildRequires:  intel-level-zero-devel
BuildRequires:  intel-metee-devel
BuildRequires:  intel-igsc-devel

Requires:       intel-level-zero
Requires:       intel-metee
Requires:       intel-igsc
Requires:       intel-compute-runtime
Requires:       libva-intel-media-driver
Requires:       intel-vpl-gpu-rt

%description
Intel XPU System Management Interface is an in-band node-level tool that
provides local GPU management. It is easily integrated into the cluster
management solutions and cluster scheduler. GPU users may use it to manage
Intel GPUs, locally. It supports local command line interface and local
library call interface.

%package devel
Summary:    Development files for %{name}
Requires:   %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for %{name}.

%prep
%autosetup -n xpumanager-%{version}

%build
mkdir build
cd build
cmake .. \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} \
    -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DDAEMONLESS=ON \
    -DCPACK_GENERATOR=RPM
make %{?_smp_mflags}

%install
cd build
make install DESTDIR=%{buildroot}

%files
%license LICENSE.md
%doc README.md SMI_README.md
%{_bindir}/xpu-smi
%{_libdir}/libxpum.so.%{version}
%{_libdir}/xpu-smi/config/diagnostics.conf
%{_libdir}/xpu-smi/config/pci.conf
%{_libdir}/xpu-smi/config/pci.ids
%{_libdir}/xpu-smi/config/perf_metrics.conf
%{_libdir}/xpu-smi/config/vgpu.conf
%{_libdir}/xpu-smi/config/xpum.conf
%{_libdir}/xpu-smi/config/xpum.conf.template

%files devel
%{_includedir}/xpum_api.h
%{_includedir}/xpum_structs.h
%{_libdir}/libxpum.so
%{_libdir}/libxpum.so.1
%{_libdir}/xpu-smi/resources/*

%changelog
* Thu jul 24 2025 Lee Chee Yang <chee.yang.lee@intel.com> - 1.2.39-4
- rebuild for glibc bump

* Fri Dec 27 2024 Naveen Saini <naveen.kumar.saini@intel.com> - 1.2.39-3
- Update Source URL.

* Thu Nov 14 2024 Anuj Mittal <anuj.mittal@intel.com> - 1.2.39-2
- Bump Release for glibc

* Thu Oct 10 2024 Mun Chun Yep <mun.chun.yep@intel.com> - 1.2.39-1
- Original version for Edge Microvisor Toolkit. License verified.
