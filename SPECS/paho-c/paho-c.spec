## START: Set by rpmautospec
## (rpmautospec version 0.8.2)
## RPMAUTOSPEC: autorelease, autochangelog
%define autorelease(e:s:pb:n) %{?-p:0.}%{lua:
    release_number = 4;
    base_release_number = tonumber(rpm.expand("%{?-b*}%{!?-b:1}"));
    print(release_number + base_release_number - 1);
}%{?-e:.%{-e*}}%{?-s:.%{-s*}}%{!?-n:%{?dist}}
## END: Set by rpmautospec

Name:           paho-c
Version:        1.3.14
Release:        5%{?dist}
Summary:        MQTT C Client
License:        BSD-3-Clause AND EPL-2.0
Distribution:   Edge Microvisor Toolkit
Vendor:         Intel Corporation
URL:            https://eclipse.dev/paho/clients/c/
Source0:        https://github.com/eclipse/paho.mqtt.c/archive/v%{version}/paho.mqtt.c-%{version}.tar.gz
Source1:        unused.abignore

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  graphviz
BuildRequires:  doxygen
BuildRequires:  openssl-devel

%description
The Paho MQTT C Client is a fully fledged MQTT client written in C.

%package        devel
Summary:        MQTT C Client development kit
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files and samples for the the Paho MQTT C Client.

%package        doc
Summary:        MQTT C Client development kit documentation
BuildArch:      noarch

%description    doc
Development documentation files for the the Paho MQTT C Client.

%prep
%autosetup -n paho.mqtt.c-%{version}

%build
export CFLAGS="%{optflags} -std=gnu17"
%cmake \
    -GNinja \
    -DPAHO_WITH_SSL=ON \
    -DPAHO_BUILD_DOCUMENTATION=ON \
    -DPAHO_BUILD_SAMPLES=ON \
    -DPAHO_ENABLE_CPACK=OFF \
%cmake_build

%install
%cmake_install
install -pDm755 %{SOURCE1} %{buildroot}%{_datadir}/%{name}/abi/paho-c.abignore

# Move the man pages to the correct directory
mkdir -p %{buildroot}%{_mandir}/man3
mv -fv %{buildroot}%{_docdir}/Eclipse\ Paho\ C/doc/MQTTAsync/man/man3/* %{buildroot}%{_mandir}/man3/
mv -fv %{buildroot}%{_docdir}/Eclipse\ Paho\ C/doc/MQTTClient/man/man3/* %{buildroot}%{_mandir}/man3/
rm -rvf %{buildroot}%{_docdir}/Eclipse\ Paho\ C/doc/MQTTAsync/man %{buildroot}%{_docdir}/Eclipse\ Paho\ C/doc/MQTTClient/man

%files
%license LICENSE edl-v10 epl-v20
%{_bindir}/paho*
%{_libdir}/libpaho-mqtt*.so.1*
%{_datadir}/%{name}/abi/paho-c.abignore

%files devel
%{_bindir}/MQTT*
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/eclipse-paho-mqtt-c/
%{_mandir}/man3/*

%files doc
%license LICENSE edl-v10 epl-v20
%{_defaultdocdir}/*

%changelog
* Thu Aug 14 2025 Basavarajx unniche<basavarajx.unniche@intel.com> - 1.3.14-5
- Initial Edge Microvisor Toolkit import from Fedora 43 (license: MIT). License verified.

* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Thu Mar 13 2025 topazus <topazus@outlook.com> - 1.3.14-3
- Fix build with GCC 15

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Jan 07 2025 Packit <hello@packit.dev> - 1.3.14-1
- Update to 1.3.14 upstream release
- Resolves: rhbz#2336146

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Mar 08 2024 Felix Wang <topazus@outlook.com> - 1.3.13-6
- enable packit only on fedora-rawhide

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 16 2024 topazus <topazus@outlook.com> - 1.3.13-3
- add packit file

* Sun Dec 24 2023 topazus <topazus@outlook.com> - 1.3.13-2
- fix file format style

* Tue Dec 05 2023 topazus <topazus@outlook.com> - 1.3.13-1
- update to 1.3.13

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1.3.9-3
- Rebuilt with OpenSSL 3.0.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 29 15:25:48 CEST 2021 Robert-André Mauchin <zebob.m@gmail.com> - 1.3.9-1
- Update to 1.3.9
- Move the man pages to the correct directory

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 04 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 1.3.4-1
- Update to 1.3.4

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Apr 30 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 1.3.2-1
- Update to 1.3.2

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Oct 13 2018 Otavio R. Piske <opiske@redhat.com> - 1.3.0-0
- Upgrades paho to version 1.3.0 which supports MQTT 5

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 01 2018 Otavio R. Piske <opiske@redhat.com> - 1.2.1-3
- Adjust the location of the abignore file in a location that can be useful for the users

* Mon Apr 30 2018 Otavio R. Piske <opiske@redhat.com> - 1.2.1-2
- Adds ABI check suppression in the package

* Mon Apr 30 2018 Otavio R. Piske <opiske@redhat.com> - 1.2.1-1
- Ignores ABI changes due to unused symbols being removed

* Sat Apr 28 2018 Otavio R. Piske <opiske@redhat.com> - 1.2.1-0
- Updates paho-c package to the latest upstream version 1.2.1
- Adjust the location of the documentation within the documentation dir

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Oct 19 2017 Otavio R. Piske <opiske@redhat.com> - 1.2.0-10
- Renames the devel-doc package as suggested by reviewer

* Thu Oct 19 2017 Otavio R. Piske <opiske@redhat.com> - 1.2.0-9
- Reduce description size to less than 80 characters
- Install the Paho client/servers tools in the binary package
- Install the binary examples in the development package only

* Sat Aug 12 2017 Otavio R. Piske <opiske@redhat.com> - 1.2.0-8
- Added missing ldconfig on the postun section

* Sat Aug 12 2017 Otavio R. Piske <opiske@redhat.com> - 1.2.0-7
- Replaced build and install commands with respective macros
- Added license to the devel docs packages
- Removed explicit require on OpenSSL
- Move the shared library symlinks to the devel package

* Mon Jul 31 2017 Otavio R. Piske <opiske@redhat.com> - 1.2.0-6
- Fixed short description of the project license

* Sun Jul 30 2017 Otavio R. Piske <opiske@redhat.com> - 1.2.0-5
- Renamed the documentation package to -doc

* Sun Jul 30 2017 Otavio R. Piske <opiske@redhat.com> - 1.2.0-4
- Removed Group tag as required by packaging guidelines
- Prevent the devel package from being used with incompatible versions
- Replaced the doc tag with the license tag

* Thu Jul 27 2017 Otavio R. Piske <opiske@redhat.com> - 1.2.0-4
- Enabled generation of debuginfo package

* Thu Jul 27 2017 Otavio R. Piske <opiske@redhat.com> - 1.2.0-3
- Fixed changelog issues pointed by rpmlint

* Thu Jul 27 2017 Otavio R. Piske <opiske@redhat.com> - 1.2.0-2
- Updated changelog to comply with Fedora packaging guidelines

* Wed Jul 26 2017 Otavio R. Piske <opiske@redhat.com> - 1.2.0-1
- Fixed rpmlint warnings: replaced cmake call with builtin macro
- Fixed rpmlint warnings: removed buildroot reference from build section

* Fri Jun 30 2017 Otavio R. Piske <opiske@redhat.com> - 1.2.0
- Updated package to version 1.2.0

* Sat Dec 31 2016 Otavio R. Piske <opiske@redhat.com> - 1.1.0
- Initial packaging

## END: Generated by rpmautospec
