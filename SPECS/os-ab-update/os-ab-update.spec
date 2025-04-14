Summary:        OS AB Update Tool for OS A and B swapping for image based update
Name:           os-ab-update
Version:        2.6
Release:        1%{?dist}
License:        MIT
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit
Group:          System Environment/Base
URL:            https://github.com/open-edge-platform/edge-microvisor-toolkit
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        ab-update.te
%global modulename  ab-update
%global selinuxtype targeted
%global debug_package %{nil}
BuildRequires:  selinux-policy-devel
Requires:       (%{name}-selinux if selinux-policy-targeted)

%description
Purpose of this module is to enable OS  A and B swapping for Day 2 Operation. Details on the
architecture can be found in the ADR.

%package        selinux
Summary:        SELinux security policy for os-ab-update
Requires(post): os-ab-update = %{version}-%{release}
BuildArch:      noarch
%{?selinux_requires}

%description    selinux
SELinux security policy for os-ab-update.

%prep
%setup -q

%build
mkdir selinux
cp -p %{SOURCE1} selinux/

make -f %{_datadir}/selinux/devel/Makefile %{modulename}.pp

%install
# Install the script files under /usr/bin
%make_install

mkdir -p %{buildroot}%{_datadir}/selinux/packages
install -m 644 %{modulename}.pp %{buildroot}%{_datadir}/selinux/packages/%{modulename}.pp

%files
%{_bindir}/os-update-tool.sh
%{_bindir}/ab-update-modules/*

%files selinux
%{_datadir}/selinux/packages/%{modulename}.pp

%post     selinux
%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/%{modulename}.pp

%postun   selinux
%selinux_modules_uninstall -s %{selinuxtype} %{modulename}

%changelog
* Thu Apr 10 2025 Suh Haw Teoh <suh.haw.teoh@intel.com> - 2.6-1
- Bump version to 2.6
- Add filesystem check before change UUID
- Fix dm verity only system not creating hash for b partition

* Fri Mar 21 2025 Suh Haw Teoh <suh.haw.teoh@intel.com> - 2.5-1
- Bump version to 2.5
- Split fde and dm verity
- Add --dev flag for create log in

* Tue Mar 11 2025 Lee Chee Yang <chee.yang.lee@intel.com> - 2.4-2
- update URL

* Fri Feb 07 2025 Suh Haw Teoh <suh.haw.teoh@intel.com> - 2.4-1
- Bump version to 2.4

* Mon Feb 03 2025 Suh Haw Teoh <suh.haw.teoh@intel.com> - 2.3-1
- Bump version to 2.3
- Transfer current hostname to B partition

* Mon Jan 20 2025 Suh Haw Teoh <suh.haw.teoh@intel.com> - 2.2-1
- Bump version to 2.2
- Fix AB update -c flag
- improve pattern matching for lsblk related operation
- Fix AB update not able to run in service.
- Add log in for B partition.

* Mon Jan 20 2025 Jia Yong Tan <jia.yong.tan@intel.com> - 2.0-3
- Update SELinux policy for cryptsetup and dmsetup.

* Mon Jan 13 2025 Jia Yong Tan <jia.yong.tan@intel.com> - 2.0-2
- Add SELinux subpackage.

* Mon Jan 06 2025 Suh Haw Teoh <suh.haw.teoh@intel.com> - 2.0-1
- Bump version to 2.0
- trigger selinux relabel all file in newly updated rootfs.

* Tue Dec 31 2024 Naveen Saini <naveen.kumar.saini@intel.com> - 1.9-2
- Update Source URL.

* Thu Dec 19 2024 Suh Haw Teoh <suh.haw.teoh@intel.com> - 1.9-1
- Bump version to 1.9
- Change temporary data folder to /opt.
- Remove unused function.

* Wed Dec 18 2024 Suh Haw Teoh <suh.haw.teoh@intel.com> - 1.8-1
- Bump version to 1.8
- Add input to check only sha256 for -s.
- Add error checking for check sha and download function.

* Mon Dec 16 2024 Suh Haw Teoh <suh.haw.teoh@intel.com> - 1.7-1
- Bump version to 1.7
- update functions for non FDE environment to match latest Edge Microvisor Toolkit image, add support for boot_uuid.
- Add checking for partition index to match current acceptable index in Edge Microvisor Toolkit, 2 and 6.
- Update auto-detection of FDE and non-FDE environment instead of manual input, replacing --nofde option.
- Change temporary folder from /opt to /tmp and auto expand it to fit raw image size, replacing -e option.
- Add checking for duplicated UUID in the system. Prevent tool from updating same image resulting in boot hang.
- Add security feature for binary full path and symlink checking.
- Remove temporary config usage, instead use .bak file to get previous target device.
- Add --debug flag for debugging, removing --var option.
- Remove -s option placeholder.
- Enhance target device searching function, replacing -t option.
- Updates some error message to show proper printing.
- Change all raw image mounting to read only.
- Change all temporary folder to under /tmp.
- Add logic to lock raw image while the tool is using them.
- Enhance clean up function to clean all temp folders and remove loop device.

* Thu Nov 28 2024 Suh Haw Teoh <suh.haw.teoh@intel.com> - 1.6-1
- Bump version to 1.6
- By default will operate as fde + dm verity.
- Added flag --nofde for backward compatibility, where it runs on non fde + dm verity.
- Fix bug where script will delete raw source file. should only happen if input is compress image.

* Wed Nov 27 2024 Suh Haw Teoh <suh.haw.teoh@intel.com> - 1.5-1
- Bump version to 1.5
- fix shellcheck on v1.4
- fix backward compatibility issue
- prevent commit multiple times
- Remove URL support
- Remove eval and run command directly
- Update permission bit for make install

* Thu Nov 07 2024 Suh Haw Teoh <suh.haw.teoh@intel.com> - 1.3-1
- Bump version to 1.3
- Remove dependency on systemd-bootx64.efi for secure boot support
- Add gz extension support

* Fri Oct 25 2024 Suh Haw Teoh <suh.haw.teoh@intel.com> - 1.2-1
- Bump version to 1.2
- Update install using make install

* Mon Oct 23 2024 Suh Haw Teoh <suh.haw.teoh@intel.com> - 1.1-1
- Bump version to 1.1
- Update to use tarball for source
- Update URL
- Remove ab-update conf file

* Fri Oct 16 2024 Samuel Taripin <samuel.taripin@intel.com> - 1.0-5
- Working Release Version for Latest Edge Microvisor Toolkit .

* Fri Oct 11 2024 Suh Haw Teoh <suh.haw.teoh@intel.com> - 1.0-4
- Update URL and signature

* Fri Oct 11 2024 Jing Hui Tham <jing.hui.tham@intel.com> - 1.0-3
- Update License.

* Thu Oct 10 2024 Yock Gen Mah <yock.gen.mah@intel.com> - 1.0-2
- Fix missing signature issue for config file.

* Thu Oct 10 2024 Yock Gen Mah <yock.gen.mah@intel.com> - 1.0-1
- Original version for Edge Microvisor Toolkit. License verified.
