Distribution:   Edge Microvisor Toolkit
Vendor:         Intel Corporation
Name:           spice
Version:        0.15.1
Release:        9%{?dist}
Summary:        Implements the SPICE protocol
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://www.spice-space.org/
Source0:        http://www.spice-space.org/download/releases/%{name}-%{version}.tar.bz2
Source1:        http://www.spice-space.org/download/releases/%{name}-%{version}.tar.bz2.sig
Source2:        victortoso-E37A484F.keyring

# https://bugzilla.redhat.com/show_bug.cgi?id=613529
%if 0%{?rhel} && 0%{?rhel} <= 7
ExclusiveArch:  x86_64
%else
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64 riscv64
%endif

BuildRequires: make
BuildRequires:  gcc gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  glib2-devel >= 2.22
BuildRequires:  spice-protocol >= 0.14.0
BuildRequires:  opus-devel
BuildRequires:  pixman-devel openssl-devel libjpeg-devel
BuildRequires:  libcacard-devel cyrus-sasl-devel
BuildRequires:  lz4-devel
BuildRequires:  gstreamer1-devel gstreamer1-plugins-base-devel
BuildRequires:  orc-devel
BuildRequires:  gnupg2
BuildRequires:  git-core

%description
The Simple Protocol for Independent Computing Environments (SPICE) is
a remote display system built for virtual environments which allows
you to view a computing 'desktop' environment not only on the machine
where it is running, but from anywhere on the Internet and from a wide
variety of machine architectures.


%package server
Summary:        Implements the server side of the SPICE protocol
Obsoletes:      spice-client < %{version}-%{release}

%description server
The Simple Protocol for Independent Computing Environments (SPICE) is
a remote display system built for virtual environments which allows
you to view a computing 'desktop' environment not only on the machine
where it is running, but from anywhere on the Internet and from a wide
variety of machine architectures.

This package contains the run-time libraries for any application that wishes
to be a SPICE server.


%package server-devel
Summary:        Header files, libraries and development documentation for spice-server
Requires:       %{name}-server%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description server-devel
This package contains the header files, static libraries and development
documentation for spice-server. If you like to develop programs
using spice-server, you will need to install spice-server-devel.


%prep
gpgv2 --quiet --keyring %{SOURCE2} %{SOURCE1} %{SOURCE0}
%autosetup -S git_am


%build
%define configure_client --disable-client
%configure --enable-smartcard --disable-client --enable-lz4 --enable-gstreamer=1.0 --disable-celt051 --disable-werror
make %{?_smp_mflags} WARN_CFLAGS='' V=1


%install
make DESTDIR=%{buildroot} install
rm -f %{buildroot}%{_libdir}/libspice-server.a
rm -f %{buildroot}%{_libdir}/libspice-server.la
mkdir -p %{buildroot}%{_libexecdir}


%ldconfig_scriptlets server


%files server
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc README CHANGELOG.md
%{_libdir}/libspice-server.so.1*

%files server-devel
%{_includedir}/spice-server
%{_libdir}/libspice-server.so
%{_libdir}/pkgconfig/spice-server.pc


%changelog
* Mon Oct 13 2025 Swee Yee Fonn <swee.yee.fonn@intel.com> - 0.15.1-9
- Initial Edge Microvisor Toolkit import from Fedora 32 (license: MIT).
- License verified.

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.15.1-7
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Feb 19 2024 Songsong Zhang <U2FsdGVkX1@gmail.com> - 0.15.1-5
- Add riscv64 support

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Oct 18 2022 Victor Toso <victortoso@redhat.com> - 0.15.1-1
- Update to 0.15.1
