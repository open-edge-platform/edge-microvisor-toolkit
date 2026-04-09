# X.org requires lazy relocations to work.
%undefine _hardened_build
%undefine _strict_symbol_defs_build

%global pkgname xorg-server

Summary:        X.Org X11 X server
Name:           xorg-x11-server
Version:        21.1.12
Release:        1%{?dist}
License:        X11 License Distribution Modification Variant
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit
URL:            https://www.x.org
Source0:        %{url}/archive/individual/xserver/%{pkgname}-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  git
BuildRequires:  kernel-headers
BuildRequires:  libX11-devel
BuildRequires:  libXau-devel
BuildRequires:  libXdmcp-devel
BuildRequires:  libXext-devel
BuildRequires:  libXfont2-devel
BuildRequires:  libxcvt-devel
BuildRequires:  libdrm-devel >= 2.4.0
BuildRequires:  libepoxy-devel
BuildRequires:  libfontenc-devel
BuildRequires:  libpciaccess-devel >= 0.13.1
BuildRequires:  libselinux-devel >= 2.0.86-1
BuildRequires:  libtool
BuildRequires:  libxkbfile-devel
BuildRequires:  make
BuildRequires:  mesa-libEGL-devel
BuildRequires:  mesa-libGL-devel >= 9.2
BuildRequires:  mesa-libgbm-devel
BuildRequires:  openssl-devel
BuildRequires:  pixman-devel >= 0.30.0
BuildRequires:  pkg-config
BuildRequires:  systemd-devel
BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols-devel
BuildRequires:  xorg-x11-font-utils >= 7.2-11
BuildRequires:  xorg-x11-proto-devel >= 7.7-10
BuildRequires:  xorg-x11-util-macros >= 1.17
BuildRequires:  xorg-x11-xtrans-devel >= 1.3.2
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(wayland-client) >= 1.3.0
BuildRequires:  pkgconfig(xshmfence) >= 1.1

%description
X.Org X11 X server

%package common
Summary:        Xorg server common files

Requires:       pixman >= 0.30.0
Requires:       xkbcomp
Requires:       xkeyboard-config

%description common
Common files shared among all X servers.

%package Xorg
Summary:        Xorg X server

Requires:       libEGL
Requires:       systemd
Requires:       xorg-x11-server-common >= %{version}-%{release}

Provides:       Xorg = %{version}-%{release}
Provides:       Xserver = %{version}-%{release}
# HdG: This should be moved to the wrapper package once the wrapper gets
# its own sub-package:
Provides:       xorg-x11-server-wrapper = %{version}-%{release}
Obsoletes:      xorg-x11-glamor < %{version}-%{release}
Provides:       xorg-x11-glamor = %{version}-%{release}
Obsoletes:      xorg-x11-drv-modesetting < %{version}-%{release}
Provides:       xorg-x11-drv-modesetting = %{version}-%{release}
# Dropped from F25
Obsoletes:      xorg-x11-drv-vmmouse < 13.1.0-4

%description Xorg
X.org X11 is an open source implementation of the X Window System.  It
provides the basic low level functionality which full fledged
graphical user interfaces (GUIs) such as GNOME and KDE are designed
upon.

%package Xnest
Summary:        A nested server

Requires:       xorg-x11-server-common >= %{version}-%{release}

Provides:       Xnest = %{version}-%{release}

%description Xnest
Xnest is an X server which has been implemented as an ordinary
X application.  It runs in a window just like other X applications,
but it is an X server itself in which you can run other software.  It
is a very useful tool for developers who wish to test their
applications without running them on their real X server.

%package Xvfb
Summary:        A X Windows System virtual framebuffer X server
# The "xvfb-run.sh" script is GPLv2, rest is MIT.
License:        GPLv2 AND MIT

Requires:       xorg-x11-server-common >= %{version}-%{release}
# Required for "xvfb-run.sh".
Requires:       xorg-x11-xauth

Provides:       Xvfb = %{version}-%{release}

%description Xvfb
Xvfb (X Virtual Frame Buffer) is an X server that is able to run on
machines with no display hardware and no physical input devices.
Xvfb simulates a dumb framebuffer using virtual memory.  Xvfb does
not open any devices, but behaves otherwise as an X display.  Xvfb
is normally used for testing servers.

%package Xwayland
Summary:        Wayland X Server

Requires:       libEGL
Requires:       xorg-x11-server-common >= %{version}-%{release}

%description Xwayland
Xwayland is an X server for running X clients under Wayland.

%package devel
Summary:        SDK for X server driver module development

Requires:       libXfont2-devel
Requires:       libpciaccess-devel
Requires:       pixman-devel
Requires:       pkg-config
Requires:       xorg-x11-proto-devel
Requires:       xorg-x11-util-macros

Provides:       xorg-x11-server-static = %{version}-%{release}
Obsoletes:      xorg-x11-glamor-devel < %{version}-%{release}
Provides:       xorg-x11-glamor-devel = %{version}-%{release}

%description devel
The SDK package provides the developmental files which are necessary for
developing X server driver modules, and for compiling driver modules
outside of the standard X11 source code tree.  Developers writing video
drivers, input drivers, or other X modules should install this package.

%prep
%autosetup -N -n %{pkgname}-%{version}
rm -rf .git
# ick
%global __scm git
%{expand:%__scm_setup_git -q}
%autopatch

%build

%global default_font_path "catalogue:%{_sysconfdir}/X11/fontpath.d,built-ins"

autoreconf -f -v --install || exit 1

%configure \
  --disable-static \
  --disable-systemd-logind \
  --disable-unit-tests \
  --enable-glamor \
  --enable-install-setuid \
  --enable-libunwind=no \
  --enable-suid-wrapper \
  --enable-xnest \
  --enable-xvfb \
  --enable-xwayland \
  --with-builderstring="Build ID: %{name} %{version}-%{release}" \
  --with-default-font-path=%{default_font_path} \
  --with-module-dir=%{_libdir}/xorg/modules \
  --with-pic \
  --with-os-name="$(hostname -s) $(uname -r)" \
  --with-vendor-name="%{vendor}" \
  --with-xkb-output=%{_localstatedir}/lib/xkb \
  --without-dtrace \
  ${CONFIGURE}

make V=1 %{?_smp_mflags}


%install
%make_install

mkdir -p %{buildroot}%{_libdir}/xorg/modules/{drivers,input}


# Remove unwanted files/dirs
{
find %{buildroot} -type f -name "*.la" -delete -print
}


%files common
%license COPYING
%{_mandir}/man1/Xserver.1*
%{_libdir}/xorg/protocol.txt
%dir %{_localstatedir}/lib/xkb
%{_localstatedir}/lib/xkb/README.compiled

%files Xorg
%{_bindir}/X
%{_bindir}/Xorg
%{_libexecdir}/Xorg
%attr(4755, root, root) %{_libexecdir}/Xorg.wrap
%{_bindir}/gtf
%dir %{_libdir}/xorg
%dir %{_libdir}/xorg/modules
%dir %{_libdir}/xorg/modules/drivers
%{_libdir}/xorg/modules/drivers/modesetting_drv.so
%dir %{_libdir}/xorg/modules/extensions
%{_libdir}/xorg/modules/extensions/libglx.so
%dir %{_libdir}/xorg/modules/input
%{_libdir}/xorg/modules/libfbdevhw.so
%{_libdir}/xorg/modules/libexa.so
%{_libdir}/xorg/modules/libglamoregl.so
%{_libdir}/xorg/modules/libshadow.so
%{_libdir}/xorg/modules/libshadowfb.so
%{_libdir}/xorg/modules/libvgahw.so
%{_libdir}/xorg/modules/libwfb.so
%ifarch %{arm} %{ix86} aarch64 x86_64
%{_libdir}/xorg/modules/libint10.so
%{_libdir}/xorg/modules/input/inputtest_drv.so
%endif
%{_mandir}/man1/gtf.1*
%{_mandir}/man1/Xorg.1*
%{_mandir}/man1/Xorg.wrap.1*
%{_mandir}/man4/fbdevhw.4*
%{_mandir}/man4/exa.4*
%{_mandir}/man4/modesetting.4*
%{_mandir}/man4/inputtestdrv.4*
%{_mandir}/man5/Xwrapper.config.5*
%{_mandir}/man5/xorg.conf.5*
%{_mandir}/man5/xorg.conf.d.5*
%dir %{_datadir}/X11/xorg.conf.d
%{_datadir}/X11/xorg.conf.d/10-quirks.conf

%files Xnest
%{_bindir}/Xnest
%{_mandir}/man1/Xnest.1*

%files Xvfb
%{_bindir}/Xvfb
%{_mandir}/man1/Xvfb.1*


%files devel
%license COPYING
%{_libdir}/pkgconfig/xorg-server.pc
%dir %{_includedir}/xorg
%{_includedir}/xorg/*.h
%{_datadir}/aclocal/xorg-server.m4

%changelog
* Thu Apr 9 2026 Lishan Liu <lishan.liu@intel.com> - 21.1.12-1
- Upgrade to 21.1.12

* Mon Apr 7 2025 Lishan Liu <lishan.liu@intel.com> - 21.1.11-1
- Upgrade to 21.1.11 to include fixes for CVE-2023-6816 CVE-2024-0408 CVE-2024-0409.

* Fri Feb 14 2025 Naveen Saini <naveen.kumar.saini@intel.com> - 21.1.9-3
- Fix source url.

* Tue Dec 24 2024 Naveen Saini <naveen.kumar.saini@intel.com> - 21.1.9-2
- Updated initial changelog entry having Fedora version and license info.

* Fri Oct 11 2024 Junxiao Chang <junxiao.chang@intel.com> - 21.1.9-1
- Initial Edge Microvisor Toolkit import from Fedora 41 (license: MIT). License verified.
