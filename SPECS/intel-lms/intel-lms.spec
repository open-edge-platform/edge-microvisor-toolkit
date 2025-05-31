%global lmsgitpath github.com/intel/lms

Summary:        Intel Local Manageability Service allows applications to access the Intel Active Management Technology (AMT) firmware via the Intel Management Engine Interface (MEI).
Name:           intel-lms
Version:        2506.0.0.0
Release:        1%{?dist}
Distribution:   Edge Microvisor Toolkit
Vendor:         Intel Corporation
License:        Apache-2.0
URL:            https://github.com/intel/lms
Source0:        https://%{lmsgitpath}/archive/v%{version}/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  ace-devel
BuildRequires:  glib2-devel
BuildRequires:  curl-devel
BuildRequires:  xerces-c-devel
BuildRequires:  libnl3-devel
BuildRequires:  libidn2-devel
BuildRequires:  libxml2-devel
BuildRequires:  intel-metee-devel
BuildRequires:  cmake >= 3.15
BuildRequires:  git
BuildRequires:  systemd-rpm-macros
Requires:       ace
Requires:       glib2
Requires:       curl
Requires:       xerces-c
Requires:       libnl3
Requires:       libxml2
Requires:       libidn2
Requires:       intel-metee

%description
Intel Local Manageability Service allows applications to access the Intel Active Management Technology (AMT) firmware via the Intel Management Engine Interface (MEI).

%prep
%autosetup -n lms-%{version}

%build
export LMS_ROOT=$(pwd)
mkdir -p build
pushd build
%cmake -Wno-dev -DBUILD_SHARED_LIBS=OFF $LMS_ROOT
%cmake_build
popd

%install
pushd build
%cmake_install
popd

mkdir -p %{buildroot}%{_datadir}/licenses/%{name}
cp COPYING %{buildroot}%{_datadir}/licenses/%{name}
cp -r Docs/Licenses/* %{buildroot}%{_datadir}/licenses/%{name}

# remove unpackaged files
rm -rf %{buildroot}%{_docdir}/lms

%post -f UNS/linux_scripts/post.rpm

%preun -f UNS/linux_scripts/preun.rpm

%files
%defattr(-,root,root,-)
%license COPYING
%{_bindir}/lms
%{_datadir}/dbus-1/system-services/com.intel.amt.lms.service
%config %{_sysconfdir}/dbus-1/system.d/com.intel.amt.lms.conf
%config /lib/systemd/system/lms.service
%config %{_libdir}/udev/rules.d/70-persistent-mei.rules
%config %{_libdir}/udev/rules.d/70-mei-wdt.rules
%config %{_sysconfdir}/rsyslog.d/20-lms.conf
%config %{_sysconfdir}/logrotate.d/lms
%{_datadir}/licenses/%{name}/*


%changelog
* Fri May 30 2025 Swee Yee Fonn <swee.yee.fonn@intel.com> - 2506.0.0.0-1
- Original version for Edge Microvisor Toolkit. (license: MIT). License verified.
