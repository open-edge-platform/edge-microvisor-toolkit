# Macros needed by SELinux
%global selinuxtype targeted

Summary:        An agent for updating the OS and bare metal agents packages
Name:           platform-update-agent
Version:        1.4.3
Release:        1%{?dist}
License:        Apache-2.0
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit
Group:          Applications/Text
URL:            https://github.com/open-edge-platform/edge-node-agents
Source0:        %{url}/archive/refs/tags/%{name}/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}.service
Source2:        env_wrapper.sh
Source3:        %{name}.conf
Source4:        platform-update-agent.te
Source5:        platform-update-agent.fc
%global debug_package %{nil}
%global _build_id_links none
BuildRequires:  golang
BuildRequires:  systemd-rpm-macros
BuildRequires:  selinux-policy-devel
Requires(pre):  %{_bindir}/systemd-sysusers
Requires:       dmidecode
Requires:       (%{name}-selinux if selinux-policy-targeted)

%description
Platform Update Agent serves the purpose to update OS and bare metal agents packages.

%package        selinux
Summary:        SELinux security policy for platform-update-agent
Requires(post): platform-update-agent = %{version}-%{release}
Requires:       fluent-bit-selinux
Requires:       otelcol-contrib-selinux
BuildArch:      noarch
%{?selinux_requires}

%description    selinux
SELinux security policy for platform-update-agent.

%prep
%setup -q

%build
GOSUMDB=off GO_MOD_MODE=vendor BUILD_DIR=$(pwd)/build/artifacts make puabuild

mkdir selinux
cp -p %{SOURCE4} selinux/
cp -p %{SOURCE5} selinux/

make -f %{_datadir}/selinux/devel/Makefile %{name}.pp

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sysconfdir}/edge-node/node/confs
mkdir -p %{buildroot}%{_sysconfdir}/sudoers.d
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_sysusersdir}
cp build/artifacts/platform-update-agent %{buildroot}%{_bindir}/platform-update-agent
install -d -m 755 %{buildroot}%{_sysconfdir}/edge-node/node/confs
install -m 644 configs/platform-update-agent.yaml %{buildroot}%{_sysconfdir}/edge-node/node/confs/platform-update-agent.yaml
cp configs/sudoers.d/platform-update-agent %{buildroot}%{_sysconfdir}/sudoers.d/platform-update-agent
cp %{SOURCE1} %{buildroot}%{_unitdir}
install -m 744 %{SOURCE2} %{buildroot}%{_sysconfdir}/edge-node/node/confs/%{name}
cp %{SOURCE3} %{buildroot}%{_sysusersdir}/%{name}.conf
mkdir -p %{buildroot}%{_defaultlicensedir}/%{name}
cp copyright %{buildroot}%{_defaultlicensedir}/%{name}

mkdir -p %{buildroot}%{_datadir}/selinux/packages
install -m 644 %{name}.pp %{buildroot}%{_datadir}/selinux/packages/%{name}.pp

%files    selinux
%{_datadir}/selinux/packages/%{name}.pp

%post     selinux
%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/%{name}.pp
# Apply the file contexts
/sbin/restorecon -Rv /usr/bin/platform-update-agent
/sbin/restorecon -Rv /etc/edge-node/node/confs/platform-update-agent.yaml
/sbin/restorecon -Rv /etc/intel_edge_node/tokens/platform-update-agent/access_token

%postun   selinux
%selinux_modules_uninstall -s %{selinuxtype} %{name}

%files
%{_bindir}/platform-update-agent
%config(noreplace) %attr(-, -, bm-agents) %{_sysconfdir}/edge-node/node/confs
%config %attr(-, platform-update-agent, bm-agents) %{_sysconfdir}/edge-node/node/confs/%{name}.yaml
%config %attr(-, platform-update-agent, bm-agents) %{_sysconfdir}/edge-node/node/confs/%{name}
%{_sysconfdir}/sudoers.d/platform-update-agent
%{_unitdir}/platform-update-agent.service
%{_sysusersdir}/%{name}.conf
%license %{_defaultlicensedir}/%{name}/copyright

%pre
%sysusers_create_package %{name} %{SOURCE3}

%post
#!/bin/sh
set -e

# Commands to run after installation
echo "Running post-installation script..."

echo "Assigning permission..."
mkdir -p %{_var}/edge-node/pua
chmod 740 %{_var}/edge-node/pua
chown platform-update-agent:bm-agents %{_var}/edge-node/pua

mkdir -p %{_sysconfdir}/default/grub.d
touch %{_sysconfdir}/default/grub.d/90-platform-update-agent.cfg
chown platform-update-agent:bm-agents %{_sysconfdir}/default/grub.d/90-platform-update-agent.cfg

echo "Assigning permission complete."
echo "Post-installation complete."

# Reload systemd manager configuration
%systemd_post platform-update-agent.service

%preun
# Before uninstallation, stop the service
%systemd_preun platform-update-agent.service

%postun
#!/bin/sh  -e
echo "Running post-uninstallation script"
# If this is an uninstall (not an upgrade), disable the service
%systemd_postun platform-update-agent.service
userdel platform-update-agent
rm -f %{_sysconfdir}/default/grub.d/90-platform-update-agent.cfg %{_sysconfdir}/edge-node/node/confs/platform-update-agent.yaml
rm -rf %{_var}/edge-node/pua
echo "Successfully purged platform-update-agent"

%changelog
* Fri Apr 18 2025  Yeng Liong Wong <yeng.liong.wong@intel.com> - 1.4.3-1
- Upgrade agent version to 1.4.3
- Improve the PUA startup time

* Thu Apr 03 2025 Rajeev Ranjan <rajeev2.ranjan@intel.com> - 1.4.1-1
- Update common to 1.6.8

* Wed Apr 02 2025 Christopher Nolan <christopher.nolan@intel.com> - 1.4.0-1
- Upgrade agent version

* Tue Mar 25 2025 Christopher Nolan <christopher.nolan@intel.com> - 1.3.7-1
- Update configuration and agent binary paths to use edge-node/

* Mon Mar 24 2025 Rajeev Ranjan <rajeev2.ranjan@intel.com> - 1.3.6-1
- Conditional import on common.mk

* Fri Mar 21 2025 Anuj Mittal <anuj.mittal@intel.com> - 1.3.5-3
- Bump Release to rebuild

* Tue Mar 18 2025 Yeng Liong Wong <yeng.liong.wong@intel.com> - 1.3.5-2
- Fix PUA build error

* Mon Mar 17 2025 Gavin Lewis <gavin.b.lewis@intel.com> - 1.3.5-1
- Update PUA to v1.3.5

* Mon Mar 10 2025 Christopher Nolan <christopher.nolan@intel.com> - 1.2.20-4
- Fix typo in URL

* Fri Feb 28 2025 Christopher Nolan <christopher.nolan@intel.com> - 1.2.20-3
- Update URL for agents

* Wed Feb 19 2025 Yeng Liong Wong <yeng.liong.wong@intel.com> - 1.2.20-2
- Update service file for systemd hardening

* Wed Jan 22 2025 Yeng Liong Wong <yeng.liong.wong@intel.com> - 1.2.20-1
- Update PUA to v1.2.20

* Wed Jan 22 2025 Anuj Mittal <anuj.mittal@intel.com> - 1.2.19-19
- Revert systemd service hardening changes

* Tue Jan 21 2025 Yeng Liong Wong <yeng.liong.wong@intel.com> - 1.2.19-18
- Update service file for systemd hardening

* Fri Jan 17 2025 Jia Yong Tan <jia.yong.tan@intel.com> - 1.2.19-17
- Add SELinux policy for root access.

* Wed Jan 15 2025 Tadeusz Matenko <tadeusz.matenko@intel.com> - 1.2.19-16
- Fix SELinux policy

* Tue Jan 14 2025 Jia Yong Tan <jia.yong.tan@intel.com> - 1.2.19-15
- Update SELinux policy to connect to otelcol_contrib
- Update SELinux policy for etc_t, sysfs_t, urandom_device_t, var_run_t
- Add dependency for otelcol-contrib-selinux

* Mon Jan 13 2025 Christopher Nolan <christopher.nolan@intel.com> - 1.2.19-14
- Update ownership of agent configuration files

* Mon Jan 13 2025 Jia Yong Tan <jia.yong.tan@intel.com> - 1.2.19-13
- Update SELinux policy to read udp_socket, getattr fixed_disk_device_t and sys_admin capbility

* Fri Jan 10 2025 Yeng Liong Wong <yeng.liong.wong@intel.com> - 1.2.19-12
- Add write access to udp_socket

* Fri Jan 10 2025 Yeng Liong Wong <yeng.liong.wong@intel.com> - 1.2.19-11
- Add missing SELinux policy for accessing platform_update_agent_conf_rw_t

* Thu Jan 09 2025 Yeng Liong Wong <yeng.liong.wong@intel.com> - 1.2.19-10
- Update config file ownership
- Update SELinux policy for accessing platform_update_agent_conf_rw_t

* Wed Jan 08 2025 Yeng Liong Wong <yeng.liong.wong@intel.com> - 1.2.19-9
- Update env_wrapper to fix file permission issue

* Mon Jan 06 2025 Naveen Saini <naveen.kumar.saini@intel.com> - 1.2.19-8
- Update Source URL.

* Mon Dec 30 2024 Tan Jia Yong <jia.yong.tan@intel.com> - 1.2.19-7
- Add SELinux policy to allow root to read platform_update_agent_conf_rw_t

* Tue Dec 24 2024 Tan Jia Yong <jia.yong.tan@intel.com> - 1.2.19-6
- Update permission to allow write access for confs directory and platform-update-agent.yaml

* Mon Dec 23 2024 Anuj Mittal <anuj.mittal@intel.com> - 1.2.19-5
- Fix permissions for confs directory

* Fri Dec 20 2024 Tan Jia Yong <jia.yong.tan@intel.com> - 1.2.19-4
- Fix SELinux policy

* Thu Dec 19 2024 Yeng Liong Wong <yeng.liong.wong@intel.com> - 1.2.19-3
- Update file permission

* Thu Dec 19 2024 Yeng Liong Wong <yeng.liong.wong@intel.com> - 1.2.19-2
- Add missing SELinux policy for PUA

* Wed Dec 18 2024 Yeng Liong Wong <yeng.liong.wong@intel.com> - 1.2.19-1
- Update PUA to v1.2.19
- Set permission correctly for platform-update-agent.yaml

* Tue Dec 17 2024 Yeng Liong Wong <yeng.liong.wong@intel.com> - 1.2.18-3
- Add missing SELinux policy for PUA

* Wed Dec 4 2024 Yeng Liong Wong <yeng.liong.wong@intel.com> - 1.2.18-2
- Add SELinux policy for PUA

* Mon Dec 2 2024 Gavin Lewis <gavin.b.lewis@intel.com> - 1.2.18-1
- Update PUA to v1.2.18

* Wed Nov 20 2024 Yeng Liong Wong <yeng.liong.wong@intel.com> - 1.2.17-1
- Update PUA to v1.2.17

* Thu Nov 14 2024 Gavin Lewis <gavin.b.lewis@intel.com> - 1.2.16-1
- Update PUA to v1.2.16

* Fri Nov 8 2024 Gavin Lewis <gavin.b.lewis@intel.com> - 1.2.15-1
- Update PUA to v1.2.15

* Thu Nov 7 2024 Gavin Lewis <gavin.b.lewis@intel.com> - 1.2.14-1
- Update PUA to v1.2.14

* Wed Nov 6 2024 Gavin Lewis <gavin.b.lewis@intel.com> - 1.2.13-1
- Update PUA to v1.2.13

* Fri Oct 25 2024 Yeng Liong Wong <yeng.liong.wong@intel.com> - 1.2.12-1
- Update PUA to v1.2.12

* Fri Oct 18 2024 Gavin Lewis <gavin.b.lewis@intel.com> - 1.2.11-1
- Update PUA to v1.2.11

* Fri Oct 18 2024 Naveen Saini <naveen.kumar.saini@intel.com> - 1.2.10-3
- Remove missing dependency on cloud-init

* Tue Oct 15 2024 Naveen Saini <naveen.kumar.saini@intel.com> - 1.2.10-2
- Remove dependency on cloud-init

* Fri Oct 11 2024 Gavin Lewis <gavin.b.lewis@intel.com> - 1.2.10-1
- Update PUA to v1.2.10

* Tue Oct 08 2024 Gavin Lewis <gavin.b.lewis@intel.com> - 1.2.9-1
- Update PUA to v1.2.9

* Fri Oct 04 2024 Anuj Mittal <anuj.mittal@intel.com> - 1.2.7-2
- Add dependency on cloud-init before the service is started

* Fri Sep 06 2024 Yeng Liong Wong <yeng.liong.wong@intel.com> - 1.2.7-1
- Update PUA to v1.2.7
- Add copyright to license directory
- Add dmidecode to get the uuid

* Fri Sep 06 2024 Yeng Liong Wong <yeng.liong.wong@intel.com> - 1.2.6-4
- Update method to get uuid

* Thu Sep 05 2024 Yeng Liong Wong <yeng.liong.wong@intel.com> - 1.2.6-3
- Update postinst, add service file and environment wrapper
- Fix incorrect agent name

* Thu Sep 05 2024 Yeng Liong Wong <yeng.liong.wong@intel.com> - 1.2.6-2
- Enable and start PUA after installation. Stop and disable PUA during uninstallation.

* Wed Sep 04 2024 Yeng Liong Wong <yeng.liong.wong@intel.com> - 1.2.6-1
- Move binary to /usr/bin and update service file

* Thu Aug 29 2024 Tadeusz Matenko <tadeusz.matenko@intel.com> - 1.2.0-2
- Add sysusers

* Fri Jul 26 2024 Yeng Liong Wong <yeng.liong.wong@intel.com> - 1.2.0-1
- Original version for Edge Microvisor Toolkit. License verified.
