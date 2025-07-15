Summary:        Restart daemons after library updates
Name:           needrestart
Version:        3.6
Release:        16%{?dist}
License:        GPLv2+
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit
URL:            https://github.com/liske/%{name}
Source0:        https://github.com/liske/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        restart.d__auditd.service
Source2:        yum__plugin.py
Source3:        dnf__plugin.py
BuildArch:	noarch
Patch0:         CVE-2024-11003.patch 
Patch1:         CVE-2024-48990.patch
Patch2:         CVE-2024-48991.patch
Patch3:         CVE-2024-48992.patch
BuildRequires:	make
BuildRequires:     perl
BuildRequires:     perl-generators
BuildRequires:     gettext
BuildRequires:     perl(ExtUtils::MakeMaker)

%{?perl_default_filter}

%description
needrestart checks which daemons need to be restarted after library
upgrades. It is inspired by checkrestart from the debian-goodies
package.

%prep
%autosetup -n %{name}-%{version} -p 1

%build
%make_build

%install
%make_install
mkdir -p %{buildroot}/%{_mandir}/man1
cp man/needrestart.1 %{buildroot}/%{_mandir}/man1/
%find_lang %{name}
%find_lang needrestart-notify
# useless files
rm -rf %{buildroot}/%{perl_archlib}
# workaround for https://github.com/liske/needrestart/issues/75
mkdir -p %{buildroot}/%{_sysconfdir}/%{name}/restart.d
cp %{SOURCE1} %{buildroot}/%{_sysconfdir}/%{name}/restart.d/auditd.service
chmod a+x %{buildroot}/%{_sysconfdir}/%{name}/restart.d/auditd.service
mkdir -p %{buildroot}/%{_sysconfdir}/dnf/plugins %{buildroot}/%{python3_sitelib}/dnf-plugins
echo -e "[main]\nenabled=1\n" >%{buildroot}/%{_sysconfdir}/dnf/plugins/needrestart.conf
cp %{SOURCE3} %{buildroot}/%{python3_sitelib}/dnf-plugins/needrestart.py
# this calls the rpm command and breaks the RPM DB
# (I guess it's not closed yet in the close_hook)
# we use systemd for all services so this is not needed anyway
rm %{buildroot}/%{_sysconfdir}/%{name}/hook.d/20-rpm
# see https://github.com/liske/needrestart/issues/123
mkdir -p %{buildroot}/%{_sysconfdir}/default
echo "IUCODE_TOOL_EXTRA_OPTIONS=--ignore-broken" >%{buildroot}/%{_sysconfdir}/default/intel-microcode


# About executable files in the /etc directory:
#   The 'README.needrestart' files in /etc/needrestart/restart.d/ and
#   /etc/needrestart/notify.d/ explicitly say the files will only be
#   considered if they are executables. There's nothing said for
#   /etc/needrestart/hook.d/ but I guess this is the same logic.
%files -f %{name}.lang -f needrestart-notify.lang
%license COPYING
%doc README.md README.batch.md README.Cont.md README.Interp.md README.nagios.md README.uCode.md NEWS ChangeLog
%config(noreplace) %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/default/intel-microcode
%{_sbindir}/%{name}
%{perl_vendorlib}/*
# %%{_libdir} resolves to /usr/lib64 on 64-bits systems, but the software does not handle this
/usr/lib/%{name}
%{_datadir}/polkit-1
%{_mandir}/man1/needrestart.1*
%config(noreplace) %{_sysconfdir}/dnf/plugins/needrestart.conf
%pycached %{python3_sitelib}/dnf-plugins/needrestart.py


%changelog
* Thu July 10 2025 Tan Jia Yong <jia.yong.tan@intel.com> - 3.6-16
- Add patches for CVE-2024-11003, CVE-2024-48990, CVE-2024-48991, CVE-2024-48992

* Wed Jan 22 2025 Lee Chee Yang <chee.yang.lee@intel.com> - 3.6-15
- Add Vendor and Distribution

* Mon Jul 22 2024 Naveen Saini <naveen.kumar.saini@intel.com> - 3.6-14
- Initial Edge Microvisor Toolkit import from Fedora 40 (license: MIT). License verified.

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 3.6-12
- Rebuilt for Python 3.13

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 3.6-8
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 08 2022 Jitka Plesnikova <jplesnik@redhat.com> - 3.6-6
- Add BR perl-generators to automatically generates run-time dependencies
  for installed Perl files

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.6-4
- Rebuilt for Python 3.11

* Thu May 26 2022 Marc Dequènes (Duck) <duck@redhat.com> - 3.6-3
- fix changelog

* Thu May 26 2022 Marc Dequènes (Duck) <duck@redhat.com> - 3.6-2
- Fix debconf template

* Thu May 19 2022 Marc Dequènes (Duck) <duck@redhat.com> - 3.6-1
- NUR

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Sep 23 2021 Miro Hrončok <mhroncok@redhat.com> - 3.5-8
- Don't own /usr/lib/python3.X/site-packages

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.5-6
- Rebuilt for Python 3.10

* Mon Mar 15 2021 Marc Dequènes (Duck) <duck@redhat.com> - 3.5-5
- move 'iucode-tool' to Recommends as it is not available in all
  architectures

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 02 2020 Miro Hrončok <mhroncok@redhat.com> - 3.5-2
- Rebuilt for Python 3.9

* Fri May 29 2020 Marc Dequènes (Duck) <duck@redhat.com> - 3.5-1
- NUR: removed patch integrated upstream and update debconf template
- downgrade debconf to Recommends on systems supporting weak dependencies

-* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.4-5
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.4-3
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 24 2019 Marc Dequènes (Duck) <duck@redhat.com> - 3.4-1
- NUR
- backport patch to blacklist the network service; accepted
  upstream but not yet released
- remove workaround related to terminal size detection in
  a non-interractive situation, fixed upstream
  (see https://github.com/liske/needrestart/pull/110)
- update debconf templates

* Tue Apr 02 2019 Marc Dequènes (Duck) <duck@redhat.com> - 3.3-3
- limit Python files to the actual plugin, thus avoiding to embed Python
  bytecode and also owning the general Python lib path by mistake
  (fixes #1672094)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 19 2018 Marc Dequènes (Duck) <duck@redhat.com> - 3.3-1
- NUR
- YUM plugin: use subprocess32 as recommended by Python
  subprocess documentation, and catch all exceptions
- removes the `20-rpm` hook, this is breaking the RPM DB
- workaround needrestart#123
- add missing dependency on 'iucode-tool'
- install new documentation file 'README.uCode.md'
- update debconf templates
- NUR: removed all patches, integrated upstream
- added workaround for GetTerminalSize problem when used
  non-interractively (see needrestart#110)
- fix crash with YUM plugin when called by yum-cron

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.11-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.11-10
- Rebuilt for Python 3.7

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.11-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Dec 21 2017 Marc Dequènes (Duck) <duck@redhat.com> - 2.11-8
- fix 'check_needed' variable scope in YUM plugin
- fix YUM plugin Python encoding problem
- declare YUM plugin can be run non-interactively
- YUM/DNF plugins: run non-interactively if --assumeyes is used

* Thu Oct 05 2017 Marc Dequènes (Duck) <duck@redhat.com> - 2.11-7
- forgot the %%{?dist} release component

* Thu Sep 28 2017 Marc Dequènes (Duck) <duck@redhat.com> - 2.11-6
- Thanks Matthias Runge Mauchin for the review
- break description line too long

* Thu Sep 28 2017 Marc Dequènes (Duck) <duck@redhat.com> - 2.11-5
- add dependency on respective YUM/DNF packages to avoid unowned directories

* Wed Sep 27 2017 Marc Dequènes (Duck) <duck@redhat.com> - 2.11-4
- make the changelog more readable

* Fri Sep 22 2017 Marc Dequènes (Duck) <duck@redhat.com> - 2.11-3
- YUM plugin: call needrestart in close_hook to avoid RPMDB mess
- fix conditional to install DNF plugin instead of YUM plugin
- build depends on python3-devel to get the related macros
- fix DNF plugin directory creation

* Fri Sep 15 2017 Marc Dequènes (Duck) <duck@redhat.com> - 2.11-2
- update YUM and DNF plugins: don't crash when needrestart itself is being removed

* Thu Sep 07 2017 Marc Dequènes (Duck) <duck@redhat.com> - 2.11-1
- initial packaging

