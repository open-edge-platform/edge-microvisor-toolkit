# Macros needed by SELinux
%global selinuxtype targeted

Summary:        An agent to manage systems via in-band connection
Name:           inbm
Version:        4.2.8.6
Release:        2%{?dist}
Distribution:   Edge Microvisor Toolkit
Vendor:         Intel Corporation
License:        Apache-2.0
URL:            https://github.com/intel/intel-inb-manageability
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        intel_manageability.conf
Source2:        inbm-configuration-replace-FQDN.sh
Source3:        inbm.te
Source4:        inbm.fc
BuildRequires:  golang >= 1.24.4
BuildRequires:  python3-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  selinux-policy-devel
Requires:       mosquitto
Requires:       python3 >= 3.12
Requires:       python3-apscheduler
Requires:       python3-certifi
Requires:       python3-chardet
Requires:       python3-cryptography
Requires:       python3-defusedxml
Requires:       python3-jsonschema
Requires:       python3-netifaces
Requires:       python3-paho-mqtt
Requires:       python3-pysocks
Requires:	      python3-psutil
Requires:       python3-requests
Requires:       python3-shortuuid
Requires:       python3-snoop
Requires:       python3-untangle
Requires:       python3-url-normalize
Requires:       python3-urllib3
Requires:       python3-xmlschema
Requires:       tpm2-tools
Requires:       (%{name}-selinux if selinux-policy-targeted)

%description
The Intel In-Band Manageability Framework is software which enables an
administrator to perform critical Device Management operations over-the-air
remotely from the cloud.

%package        selinux
Summary:        SELinux security policy for inbm
Requires(post): inbm = %{version}-%{release}
BuildArch:      noarch
%{?selinux_requires}

%description    selinux
SELinux security policy for inbm.

%prep
%setup -q -n %{name}-%{version}

%build
# Build SELinux policy
mkdir selinux
cp -p %{SOURCE3} selinux/
cp -p %{SOURCE4} selinux/
make -f %{_datadir}/selinux/devel/Makefile %{name}.pp

# No build step needed for Python
# For golang, build inb-provision-certs
cd %{_builddir}/%{name}-%{version}/inbm/fpm/inb-provision-certs
CGO_ENABLED=0 go build -trimpath -mod=readonly -gcflags="all=-spectre=all -l" -asmflags="all=-spectre=all" -o inb-provision-certs


%install
find %{_builddir}/%{name}-%{version} -type d -name "test*" -exec rm -rf {} +
find %{_builddir}/%{name}-%{version} -name "test_*.py" -exec rm -f {} +

# Set up bindir
install -d %{buildroot}%{_bindir}

# Install inb-provision-certs
install -m 755 %{_builddir}/%{name}-%{version}/inbm/fpm/inb-provision-certs/inb-provision-certs %{buildroot}%{_bindir}/inb-provision-certs

# Install agents and associated files
for i in dispatcher configuration diagnostic ; do
  install -d %{buildroot}%{python3_sitelib}/"$i"
  cp -R %{_builddir}/%{name}-%{version}/inbm/"$i"-agent/"$i"/* %{buildroot}%{python3_sitelib}/"$i"
  install -m 755 %{_builddir}/%{name}-%{version}/inbm/"$i"-agent/"$i"/"$i".py %{buildroot}%{_bindir}/inbm-"$i"
  cp -R %{_builddir}/%{name}-%{version}/inbm/"$i"-agent/fpm-template/* %{buildroot}
done

# Modify dispatcher service file to add it into bm-agents group
sed -i '/^Group=dispatcher-agent$/a SupplementaryGroups=bm-agents' %{buildroot}%{_unitdir}/inbm-dispatcher.service

# Install provision-tc script
install -D -m 0755 %{_builddir}/%{name}-%{version}/inbm/cloudadapter-agent/fpm-template/usr/bin/provision-tc %{buildroot}%{_bindir}/provision-tc

# Configure INBM for Edge Microvisor Toolkit specific needs

# Copy intel_manageability.conf over the existing one
install -D -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/intel_manageability.conf
# Copy inbm-configuration-replace-FQDN.sh 
FQDN_REPLACE_SCRIPT_PATH_TARGET=%{_bindir}/inbm-configuration-replace-FQDN.sh
FQDN_REPLACE_SCRIPT_PATH_BUILD=%{buildroot}$FQDN_REPLACE_SCRIPT_PATH_TARGET
install -D -m 0755 %{SOURCE2} "$FQDN_REPLACE_SCRIPT_PATH_BUILD"
# Modify configuration service file to add ExecStartPre to customize config file at runtime for FQDN
sed -i "/^ExecStart/i ExecStartPre=$FQDN_REPLACE_SCRIPT_PATH_TARGET" %{buildroot}%{_unitdir}/inbm-configuration.service
# and also inject LP agent variables
sed -i '/^ExecStart/i EnvironmentFile=/etc/edge-node/node/agent_variables' %{buildroot}%{_unitdir}/inbm-configuration.service
# above changes are modeled after the platform update agent service file and its `env_wrapper.sh`.


# Skip checking OS as we know it's EMT
sed -i '/^function provision {/,/^}/{ /check_requirements/d; }' %{buildroot}%{_bindir}/provision-tc

# On EMT, do not try to disable telemetry or cloudadapter as we're not including them.
sed -i '/^function enable_mqtt {/,/^}/{
    s/systemctl disable --now mqtt inbm inbm-dispatcher inbm-telemetry inbm-configuration inbm-cloudadapter inbm-diagnostic/systemctl disable --now mqtt inbm inbm-dispatcher inbm-configuration inbm-diagnostic/
}' %{buildroot}%{_bindir}/provision-tc

# On EMT, do not try to enable telemetry or cloudadapter as we're not including them.
sed -i '/^function enable_agents {/,/^}/{
    s/systemctl enable --now inbm inbm-dispatcher inbm-telemetry inbm-configuration inbm-cloudadapter inbm-diagnostic/systemctl enable --now inbm inbm-dispatcher  inbm-configuration  inbm-diagnostic/
}' %{buildroot}%{_bindir}/provision-tc

# INBM runs a custom mosquitto agent to communicate between services and uses the path /var/persistent-log/mosquitto to store logs
install -d %{buildroot}%{_var}/persistent-log/mosquitto

# Do not interact with apparmor as not currently available on Edge Microvisor Toolkit
sed -i '/systemctl restart apparmor/d' %{buildroot}%{_bindir}/provision-tc

# Install inbc-program
install -d %{buildroot}%{python3_sitelib}/inbc
cp -R %{_builddir}/%{name}-%{version}/inbc-program/inbc/* %{buildroot}%{python3_sitelib}/inbc
install -m 755 %{_builddir}/%{name}-%{version}/inbc-program/inbc/inbc.py %{buildroot}%{_bindir}/inbc
cp -R %{_builddir}/%{name}-%{version}/inbc-program/fpm-template/* %{buildroot}

# Install inbm-lib
install -d %{buildroot}%{python3_sitelib}/inbm_lib
cp -R %{_builddir}/%{name}-%{version}/inbm-lib/inbm_lib/* %{buildroot}%{python3_sitelib}/inbm_lib
install -d %{buildroot}%{python3_sitelib}/inbm_common_lib
cp -R %{_builddir}/%{name}-%{version}/inbm-lib/inbm_common_lib/* %{buildroot}%{python3_sitelib}/inbm_common_lib

# Install everything in inbm/fpm/mqtt/template/ to buildroot
cp -R %{_builddir}/%{name}-%{version}/inbm/fpm/mqtt/template/* %{buildroot}

# make new files/directories so they can be persisted

mkdir %{buildroot}%{_var}/intel-manageability
mkdir %{buildroot}%{_var}/log
touch %{buildroot}%{_var}/log/inbm-update-status.log
echo '"UpdateLog": []' > %{buildroot}%{_var}/log/inbm-update-log.log
touch %{buildroot}%{_sysconfdir}/intel_manageability.conf_bak

# set all INBM agent log levels to DEBUG
for i in dispatcher-agent configuration-agent diagnostic-agent 
do 
  sed -i 's/ERROR/DEBUG/g' %{buildroot}%{_sysconfdir}/intel-manageability/public/"$i"/logging.ini
done

# Modify mqtt service to no longer depend on tpm2-abrmd
sed -i '/^\(Wants\|After\)=tpm2-abrmd\.service$/d' "%{buildroot}%{_unitdir}/mqtt.service"

# Install SELinux policy
mkdir -p %{buildroot}%{_datadir}/selinux/packages
install -m 644 %{name}.pp %{buildroot}%{_datadir}/selinux/packages/%{name}.pp

# drop already installed documentation, we will use an RPM macro to install it
rm -rf %{buildroot}%{_docdir}

%files    selinux
%{_datadir}/selinux/packages/%{name}.pp

%post     selinux
%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/%{name}.pp
# Apply the file contexts
/sbin/restorecon -Rv /usr/bin/inbm-dispatcher
/sbin/restorecon -Rv /usr/bin/inbm-diagnostic
/sbin/restorecon -Rv /usr/bin/inbm-configuration
/sbin/restorecon -Rv /etc/intel_manageability.conf

%postun   selinux
%selinux_modules_uninstall -s %{selinuxtype} %{name}


%files

%config(noreplace) %{_sysconfdir}/*
%{_bindir}/*
%{python3_sitelib}/*
%{_unitdir}/*
%{_datadir}/configuration-agent/*
%{_datadir}/dispatcher-agent/*
%license LICENSE
%{_datadir}/intel-manageability/*
%{_var}/cache/manageability/*
%{_sharedstatedir}/dispatcher/*
%{_var}/persistent-log/mosquitto
%{_var}/intel-manageability
%{_var}/log/*

%pre
    # Create groups and users for agents and programs
    %define items cloudadapter-agent cmd-program configuration-agent diagnostic-agent dispatcher-agent inbc-program mqtt-ca telemetry-agent
    
    # Create docker group if it doesn't exist
    getent group docker >/dev/null || groupadd -r docker
    
    # Iterate over each item to create group and user
    for i in %{items}; do
        getent group $i >/dev/null || groupadd -r $i
        getent passwd $i >/dev/null || \
            useradd -r -g $i -d /nonexistent -s /usr/sbin/nologin \
            -c "$i user" $i
    done
    
    # Ensure mqtt-broker group and user exist with specific home directory
    getent group mqtt-broker >/dev/null || groupadd -r mqtt-broker
    getent passwd mqtt-broker >/dev/null || \
        useradd -r -g mqtt-broker -d %{_sharedstatedir}/mqtt-broker -s /usr/sbin/nologin \
        -c "MQTT Broker user" mqtt-broker


%post
%preun
%postun

%changelog
* Tue Sep 2 2025 Polmoorx shiva kumar <polmoorx.shiva.kumar@intel.com> - 4.2.8.6-2
- Update go version to use above 1.24.4

* Thu Apr 03 2025 Yeng Liong Wong <yeng.liong.wong@intel.com> - 4.2.8.6-1
- Update INBM to v4.2.8.6

* Tue Mar 25 2025 Christopher Nolan <christopher.nolan@intel.com> - 4.2.8.5-3
- Update configuration and agent binary paths to use edge-node/

* Fri Mar 21 2025 Anuj Mittal <anuj.mittal@intel.com> - 4.2.8.5-2
- Bump Release to rebuild

* Mon Mar 17 2025 Gavin Lewis <gavin.b.lewis@intel.com> - 4.2.8.5-1
- Update INBM to v4.2.8.5

* Fri Mar 14 2025 Yeng Liong Wong <yeng.liong.wong@intel.com> - 4.2.8.4-4
- Update files for rebranding.

* Mon Mar 3 2025 Jia Yong Tan <jia.yong.tan@intel.com> - 4.2.8.4-3
- Update SELinux policy.

* Mon Feb 24 2025 Yeng Liong Wong <yeng.liong.wong@intel.com> - 4.2.8.4-2
- Fix SELinux policy to access os-update-tool lock.

* Fri Feb 14 2025 Gavin Lewis <gavin.b.lewis@intel.com> - 4.2.8.4-1
- Rename Emt references

* Tue Jan 21 2025 Yeng Liong Wong <yeng.liong.wong@intel.com> - 4.2.8.2-7
- Add SELinux policy for access os-update-tool lock.

* Fri Jan 17 2025 Jia Yong Tan <jia.yong.tan@intel.com> - 4.2.8.2-6
- Add SELinux policy for root access.

* Tue Jan 07 2025 Naveen Saini <naveen.kumar.saini@intel.com> - 4.2.8.2-5
- Fix license installation.

* Mon Jan 06 2025 Naveen Saini <naveen.kumar.saini@intel.com> - 4.2.8.2-4
- Update Source URL.

* Mon Dec 30 2024 Jia Yong Tan <jia.yong.tan@intel.com> - 4.2.8.2-3
- Add SELinux policy to allow root to read inbm_conf_rw_t

* Fri Dec 20 2024 Jia Yong Tan <jia.yong.tan@intel.com> - 4.2.8.2-2
- Fix SELinux policy

* Wed Dec 18 2024 Yeng Liong Wong <yeng.liong.wong@intel.com> - 4.2.8.2-1
- Update inbm to v4.2.8.2

* Tue Dec 17 2024 Yeng Liong Wong <yeng.liong.wong@intel.com> - 4.2.8-4
- Add missing SELinux policy for INBM

* Wed Dec 4 2024 Yeng Liong Wong <yeng.liong.wong@intel.com> - 4.2.8-3
- Add SELinux policy for INBM

* Wed Dec 4 2024 Gavin Lewis <gavin.b.lewis@intel.com> - 4.2.8-2
- Remove tpm2-abrmd dependency from both INBM and INBM's mqtt service

* Mon Dec 2 2024 Gavin Lewis <gavin.b.lewis@intel.com> - 4.2.8-1
- Update INBM to v4.2.8

* Mon Nov 25 2024 Andy <andy.peng@intel.com> - 4.2.7-2
- Update go build flag to reduce binary size
- -N to enable compiler optimization 

* Tue Nov 19 2024 Gavin Lewis <gavin.b.lewis@intel.com> - 4.2.7-1
- Update INBM version
- Customize INBM config file for Edge Microvisor Toolkit

* Mon Nov 18 2024 Gavin Lewis <gavin.b.lewis@intel.com> - 4.2.6.2-2
- Update INBM config and logging config files

* Fri Oct 25 2024 Yeng Liong Wong <yeng.liong.wong@intel.com> - 4.2.6.2-1
- Update inbm to v4.2.6.2

* Fri Oct 18 2024 Gavin Lewis <gavin.b.lewis@intel.com> - 4.2.6.1-2
- Add psutil as dependency

* Fri Oct 18 2024 Yeng Liong Wong <yeng.liong.wong@intel.com> - 4.2.6.1-1
- Update inbm to v4.2.6.1
- Add inbm-dispatcher to bm-agents group

* Thu Oct 17 2024 Yeng Liong Wong <yeng.liong.wong@intel.com> - 4.2.6-2
- Fix iteration warning during groupadd

* Tue Oct 1 2024 Gavin Lewis <gavin.b.lewis@inteloc.m> - 4.2.6-1
- Pull in latest INBM
- Update dependency list
- Create some files meant to be runtime-persistent at install time

* Wed Sep 4 2024 Gavin Lewis <gavin.b.lewis@intel.com> - 4.2.5-1
- Original version for Edge Microvisor Toolkit. License verified.
