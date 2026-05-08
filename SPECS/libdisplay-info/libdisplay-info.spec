# See https://gitlab.freedesktop.org/emersion/libdisplay-info/-/merge_requests/149
# for library versioning explanation.
%global sover 3
 
Name:           libdisplay-info
Version:        0.3.0
Release:        1%{?dist}
Summary:        EDID and DisplayID library
 
# Main license: MIT
# test/data: CC-BY-4.0, MIT (see test/data/README.md).
License:        MIT
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit
URL:            https://gitlab.freedesktop.org/emersion/libdisplay-info
Source0:        %{url}/-/releases/%{version}/downloads/%{name}-%{version}.tar.xz
Source1:        %{url}/-/releases/%{version}/downloads/%{name}-%{version}.tar.xz.sig
# 0FDE7BE0E88F5E48: emersion <contact@emersion.fr>
Source2:        gpgkey-0FDE7BE0E88F5E48.gpg
 
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  meson >= 0.57
BuildRequires:  pkgconfig(hwdata)
 
%description
%{summary}.
 
%package        tools
Summary:        Command-line tools for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
 
%description    tools
%{summary}.
 
%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
 
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.
 
 
%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup
 
%build
%meson
%meson_build
 
%install
%meson_install
 
%check
%meson_test
 
%files
%license LICENSE
%doc README.md
%{_libdir}/%{name}.so.%{sover}
%{_libdir}/%{name}.so.%{version}
 
%files tools
%{_bindir}/di-edid-decode
 
%files devel
%{_includedir}/%{name}
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
 
 
%changelog
* Thu Apr 2 2026 Lishan Liu <lishan.liu@intel.com> - 0.3.0-1
- Initial Edge Microvisor Toolkit import from Fedora 44 (license: MIT). License verified.
