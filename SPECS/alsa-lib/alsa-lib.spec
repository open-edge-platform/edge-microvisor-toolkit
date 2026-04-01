%define version_alsa_tplg 1.2.5

Summary:        ALSA library
Name:           alsa-lib
Version:        1.2.9
Release:        3%{?dist}
License:        LGPLv2+
Distribution:   Edge Microvisor Toolkit
Vendor:         Intel Corporation
Group:          Applications/Internet
URL:            https://alsa-project.org
Source0:        https://www.alsa-project.org/files/pub/lib/%{name}-%{version}.tar.bz2
Source1:        https://www.alsa-project.org/files/pub/lib/alsa-topology-conf-%{version_alsa_tplg}.tar.bz2
Patch0:         CVE-2026-25068.patch

BuildRequires:  python3-devel
BuildRequires:  python3-libs
Requires:       python3

%description
The ALSA Library package contains the ALSA library used by programs
(including ALSA Utilities) requiring access to the ALSA sound interface.

%package        devel
Summary:        Header and development files
Requires:       %{name} = %{version}

%description    devel
It contains the libraries and header files to create applications.

%package  -n alsa-topology
Summary:   ALSA Topology configuration
BuildArch: noarch
Requires:  %{name} >= %{version}

%description -n alsa-topology
The Advanced Linux Sound Architecture (ALSA) topology configuration
contains alsa-lib configuration of SoC topology (widgets, mixers, pipelines).

%prep
%autosetup -p1

%build
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

# Create topology directory
mkdir -p %{buildroot}/%{_datadir}/alsa/topology

# Unpack topologies
tar xvjf %{SOURCE1} -C %{buildroot}/%{_datadir}/alsa --strip-components=1 --wildcards "*/topology"

%files
%defattr(-,root,root)
%license COPYING
%{_bindir}/*
%{_libdir}/*
%exclude %{_libdir}/debug/
%{_datadir}/*

%files devel
%defattr(-,root,root)
%{_includedir}/*

%files -n alsa-topology
%{_datadir}/alsa/topology/*

%changelog
* Mon Mar 16 2026 Lee Chee Yang <chee.yang.lee@intel.com> - 1.2.9-3
- merge from Azure Linux 3.0.20260304-3.0 
- Patch for CVE-2026-25068

* Tue Aug 26 2025 Basavaraj unniche<basavarajx.unniche@intel.com> - 1.2.9-2
- Generate alsa-topology, which is needed for alsa-sof-firmware
- Initial Edge Microvisor Toolkit import from Azure Linux (license: MIT). License verified.

* Fri Oct 27 2023 CBL-Mariner Servicing Account <cblmargh@microsoft.com> - 1.2.9-1
- Auto-upgrade to 1.2.9 - Azure Linux 3.0 - package upgrades

* Wed Sep 20 2023 Jon Slobodzian <joslobo@microsoft.com> - 1.2.6.1-2
- Recompile with stack-protection fixed gcc version (CVE-2023-4039)

* Tue Jan 4 2022 Nicolas Guibourge <nicolasg@microsoft.com> 1.2.6.1-1
- Update to version 1.2.6.1

* Wed May 26 2021 Thomas Crain <thcrain@microsoft.com> - 1.2.2-2
- Replace python2 dependencies with python3
- License verified

* Thu May 28 2020 Andrew Phelps <anphel@microsoft.com> - 1.2.2-1
- Update to version 1.2.2 to fix CVE-2009-0035

* Sat May 09 2020 Nick Samson <nisamson@microsoft.com> - 1.1.9-2
- Added %%license line automatically

* Mon Mar 16 2020 Andrew Phelps <anphel@microsoft.com> - 1.1.9-1
- Update to version 1.1.9. License verified.

* Tue Sep 03 2019 Mateusz Malisz <mamalisz@microsoft.com> - 1.1.7-2
- Initial CBL-Mariner import from Photon (license: Apache2).

* Mon Dec 10 2018 Alexey Makhalov <amakhalov@vmware.com> - 1.1.7-1
- initial version, moved from Vivace
