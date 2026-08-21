# This is a firmware package, so binaries (which are not run on the host)
# in the end package are expected.
%define _binaries_in_noarch_packages_terminate_build   0
%global _firmwarepath  /usr/lib/firmware
%global _xz_opts -9 --check=crc32

%global sof_ver 2025.12
#global sof_ver_pre rc1
%global sof_ver_rel %{?sof_ver_pre:.%{sof_ver_pre}}
%global sof_ver_pkg0 %{sof_ver}%{?sof_ver_pre:-%{sof_ver_pre}}
%global sof_ver_pkg v%{sof_ver_pkg0}

%global with_sof_addon 0
%global sof_ver_addon 0

%global tplg_version 1.2.4

Summary:        Firmware and topology files for Sound Open Firmware project
Name:           alsa-sof-firmware
Version:        %{sof_ver}
Release:        2%{?dist}
License:        BSD-3-Clause AND Apache-2.0
Distribution:   Edge Microvisor Toolkit
Vendor:         Intel Corporation
URL:            https://github.com/thesofproject/sof-bin
Source:         https://github.com/thesofproject/sof-bin/releases/download/%{sof_ver_pkg}/sof-bin-%{sof_ver_pkg0}.tar.gz
%if 0%{?with_sof_addon}
Source3:        https://github.com/thesofproject/sof-bin/releases/download/v%{sof_ver_addon}/sof-tplg-v%{sof_ver_addon}.tar.gz
%endif
Source4:         https://github.com/thesofproject/sof-bin/releases/download/%{sof_ver_pkg}/sof-nvl-s.ri
Source5:         https://github.com/thesofproject/sof-bin/releases/download/%{sof_ver_pkg}/sof-nvl.ri
Source6:         https://github.com/thesofproject/sof-bin/releases/download/%{sof_ver_pkg}/sof-nvl-rt722.tplg
Source7:         https://github.com/thesofproject/sof-bin/releases/download/%{sof_ver_pkg}/sof-nvl-s-openmodules.ri
Source8:         https://github.com/thesofproject/sof-bin/releases/download/%{sof_ver_pkg}/sof-nvl-openmodules.ri
BuildRequires:  alsa-topology >= %{tplg_version}
BuildRequires:  alsa-utils >= %{tplg_version}
Conflicts:      alsa-firmware <= 1.2.1-6

# noarch, since the package is firmware
BuildArch:      noarch

%description
This package contains the firmware binaries for the Sound Open Firmware project.

%package debug
Requires:       alsa-sof-firmware
Summary:        Debug files for Sound Open Firmware project
License:        BSD-3-Clause

%description debug
This package contains the debug files for the Sound Open Firmware project.

%prep
%autosetup -n sof-bin-%{sof_ver_pkg0}

mkdir -p firmware/intel

for d in sof sof-ipc4 sof-ipc4-lib sof-ipc4-tplg sof-tplg; do \
  mv "${d}" firmware/intel; \
done

ln -s sof-ipc4-tplg firmware/intel/sof-ace-tplg

%if 0%{?with_sof_addon}
tar xvzf %{SOURCE3}
mv sof-tplg-v%{sof_ver_addon}/*.tplg firmware/intel/sof-tplg
%endif

# for nvl
mkdir -p firmware/intel/sof-ipc4/nvl-s
cp %{SOURCE4} firmware/intel/sof-ipc4/nvl-s
cp %{SOURCE7} firmware/intel/sof-ipc4/nvl-s
mkdir -p firmware/intel/sof-ipc4/nvl
cp %{SOURCE5} firmware/intel/sof-ipc4/nvl
cp %{SOURCE8} firmware/intel/sof-ipc4/nvl
mkdir -p firmware/intel/sof-ipc4-tplg
cp %{SOURCE6} firmware/intel/sof-ipc4-tplg

# remove NXP firmware files
rm Notice.NXP LICENCE.NXP
rm -rf firmware/intel/sof-tplg/sof-imx8*

# remove Mediatek firmware files
rm -rf firmware/intel/sof-tplg/sof-mt8*

# use xz compression
xz -z %{_xz_opts} manifest.txt
for d in sof sof-ipc4; do \
  find -P "firmware/intel/${d}" -type f -name "*.ri" -exec xz -z %{_xz_opts} {} \;
  for f in $(find -P "firmware/intel/${d}" -type l -name "*.ri"); do \
    l=$(readlink "${f}"); \
    n=$(dirname "${f}"); \
    b=$(basename "${f}"); \
    rm "${f}"; \
    pushd "${n}"; \
    ln -svf "${l}.xz" "${b}.xz"; \
    popd; \
  done; \
done
for d in sof-ipc4-lib; do \
  for e in bin llext; do \
    find -P "firmware/intel/${d}"  -type f -name "*.${e}" -exec xz -z %{_xz_opts} {} \;
    for f in $(find -P "firmware/intel/${d}" -type l -name "*.${e}"); do \
      l=$(readlink "${f}"); \
      n=$(dirname "${f}"); \
      b=$(basename "${f}"); \
      rm "${f}"; \
      pushd "${n}"; \
      ln -svf "${l}.xz" "${b}.xz"; \
      popd; \
    done; \
  done; \
done
for d in sof-tplg sof-ipc4-tplg; do \
  find -P "firmware/intel/${d}"  -type f -name "*.tplg" -exec xz -z %{_xz_opts} {} \;
done

%build
# SST topology files (not SOF related, but it's a Intel hw support
# and this package seems a good place to distribute them
alsatplg -c /usr/share/alsa/topology/hda-dsp/skl_hda_dsp_generic-tplg.conf \
         -o firmware/skl_hda_dsp_generic-tplg.bin
# use xz compression
xz -z %{_xz_opts} firmware/*.bin
chmod 0644 firmware/*.bin.xz

%install
mkdir -p %{buildroot}%{_firmwarepath}
cp -ra firmware/* %{buildroot}%{_firmwarepath}

# gather files and directories
FILEDIR=$(pwd)
pushd %{buildroot}/%{_firmwarepath}
find -P . -name "*.ri.xz" | sed -e '/^.$/d' >> $FILEDIR/alsa-sof-firmware.files
#find -P . -name "*.tplg" | sed -e '/^.$/d' >> $FILEDIR/alsa-sof-firmware.files
find -P . -name "*.llext.xz" | sed -e '/^.$/d' >> $FILEDIR/alsa-sof-firmware.files
find -P intel/sof-ipc4-lib -name "*.bin.xz" | sed -e '/^.$/d' >> $FILEDIR/alsa-sof-firmware.files
find -P . -name "*.ldc" | sed -e '/^.$/d' > $FILEDIR/alsa-sof-firmware.debug-files
find -P . -type d | sed -e '/^.$/d' > $FILEDIR/alsa-sof-firmware.dirs
popd
sed -i -e 's:^./::' alsa-sof-firmware.{files,debug-files,dirs}
sed -i -e 's!^!/usr/lib/firmware/!' alsa-sof-firmware.{files,debug-files,dirs}
sed -e 's/^/%%dir /' alsa-sof-firmware.dirs >> alsa-sof-firmware.files
cat alsa-sof-firmware.files

%files -f alsa-sof-firmware.files
%license LICENCE*
%doc README*
%doc manifest.txt.xz
%dir %{_firmwarepath}

# Licence: 3-clause BSD
%{_firmwarepath}/*.bin.xz

# Licence: 3-clause BSD
# .. for files with suffix .tplg
%{_firmwarepath}/intel/sof-tplg/*.tplg.xz
%{_firmwarepath}/intel/sof-ipc4-tplg/*.tplg.xz
%{_firmwarepath}/intel/sof-ace-tplg

# Licence: SOF (3-clause BSD plus others)
# .. for files with suffix .ri

%files debug -f alsa-sof-firmware.debug-files

%pretrans -p <lua>
path = "%{_firmwarepath}/intel/sof-tplg"
st = posix.stat(path)
if st and st.type == "link" then
  os.remove(path)
end

path1 = "%{_firmwarepath}/intel/sof-ace-tplg"
path2 = "%{_firmwarepath}/intel/sof-ipc4-tplg"
st = posix.stat(path1)
if st and st.type == "directory" then
  os.rename(path1, path2)
end

%changelog
* Wed Aug 13 2026 Andy <andy.peng@intel.com> - 2025.12-2
- Include NVL firmware files.

* Mon Jan 12 2026 Basavarajx unniche <basavarajx.unniche@intel.com> - 2025.12-1
- Update version to 2025.12.

* Tue Aug 26 2025 Rajesh Shanmugam<rajesh1x.shanmugam@intel.com> - 2025.05-3
- Initial Edge Microvisor Toolkit import from Fedora 43 (license: MIT)
- License verified.

* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2025.05-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Tue Jun 24 2025 Jaroslav Kysela <perex@perex.cz> - 2025.05-1
- Update to v2025.05

* Thu Apr  3 2025 Jaroslav Kysela <perex@perex.cz> - 2025.01.1-1
- Update to v2025.01.1

* Tue Feb 25 2025 Jaroslav Kysela <perex@perex.cz> - 2025.01-1
- Update to v2025.01

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2024.09.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Dec 18 2024 Jaroslav Kysela <perex@perex.cz> - 2024.09.2-2
- Add sof-ipc4-lib directory

* Fri Dec  6 2024 Jaroslav Kysela <perex@perex.cz> - 2024.09.2-1
- Update to v2024.09.2

* Mon Nov 11 2024 Jaroslav Kysela <perex@perex.cz> - 2024.09.1-1
- Update to v2024.09.1

* Fri Sep 27 2024 Jaroslav Kysela <perex@perex.cz> - 2024.09-1
- Update to v2024.09

* Tue Sep  3 2024 Jaroslav Kysela <perex@perex.cz> - 2024.06-1
- Update to v2024.06
- Remove AVS topology files (linux-firmware is the main source now)

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2024.03-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Apr  3 2024 Jaroslav Kysela <perex@perex.cz> - 2024.03-2
- Update to v2024.03

* Tue Mar  5 2024 Jaroslav Kysela <perex@perex.cz> - 2023.12.1-1
- Update to v2023.12.1
- Add AVS topology files v2024.02

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2023.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2023.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Dec 20 2023 Jaroslav Kysela <perex@perex.cz> - 2023.12-1
- Update to v2023.12

* Thu Nov 16 2023 Jaroslav Kysela <perex@perex.cz> - 2023.09.2-1
- Update to v2023.09.2

* Mon Nov  6 2023 Jaroslav Kysela <perex@perex.cz> - 2023.09.1-1
- Update to v2023.09.1

* Tue Oct 24 2023 Jaroslav Kysela <perex@perex.cz> - 2023.09-1
- Update to v2023.09

* Wed Aug  9 2023 Jaroslav Kysela <perex@perex.cz> - 2.2.6-1
- Update to v2.2.6

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun  6 2023 Jaroslav Kysela <perex@perex.cz> - 2.2.5-2
- SPDX license

* Mon May 15 2023 Jaroslav Kysela <perex@perex.cz> - 2.2.5-1
- Update to v2.2.5

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan  9 2023 Jaroslav Kysela <perex@perex.cz> - 2.2.4-2
- Update to v2.2.4

* Wed Dec  7 2022 Jaroslav Kysela <perex@perex.cz> - 2.2.3-1
- Update to v2.2.3

* Sat Sep 24 2022 Jaroslav Kysela <perex@perex.cz> - 2.2.2-1
- Update to v2.2.2

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 17 2022 Jaroslav Kysela <perex@perex.cz> - 2.1.1-1
- Update to v2.1.1 + v2.1.1a (topology)

* Fri Feb  4 2022 Jaroslav Kysela <perex@perex.cz> - 2.0-3
- Use CRC32 for the xz compression

* Thu Jan 27 2022 Jaroslav Kysela <perex@perex.cz> - 2.0-2
- Update to v2.0
- Use xz compression

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Dec 15 2021 Jaroslav Kysela <perex@perex.cz> - 1.9.3-1
- Update to v1.9.3

* Tue Nov 23 2021 Jaroslav Kysela <perex@perex.cz> - 1.9.2-1
- Update to v1.9.2

* Tue Oct  5 2021 Jaroslav Kysela <perex@perex.cz> - 1.9-2
- Update to v1.9

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 22 2021 Jaroslav Kysela <perex@perex.cz> - 1.8-1
- Update to v1.8

* Thu Jun  3 2021 Jaroslav Kysela <perex@perex.cz> - 1.7-1
- Update to v1.7

* Thu Mar 11 2021 Jaroslav Kysela <perex@perex.cz> - 1.6.1-4
- Add SST Skylake HDA topology binary (bug#1933423)

* Fri Mar  5 2021 Jaroslav Kysela <perex@perex.cz> - 1.6.1-3
- Add TGL-H firmware files

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan  3 2021 Jaroslav Kysela <perex@perex.cz> - 1.6.1-1
- Update to v1.6.1

* Thu Dec 10 2020 Jaroslav Kysela <perex@perex.cz> - 1.6-4
- Update to v1.6 (Dec 9)

* Thu Nov 19 2020 Jaroslav Kysela <perex@perex.cz> - 1.6-3
- Update to v1.6 (Nov 19)

* Wed Oct 14 2020 Jaroslav Kysela <perex@perex.cz> - 1.6-1
- Update to v1.6 (Oct 13)

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun  1 2020 Jaroslav Kysela <perex@perex.cz> - 1.5-1
- Update to v1.5

* Tue May 12 2020 Jaroslav Kysela <perex@perex.cz> - 1.4.2-6
- Fix the upgrade (make /usr/lib/firmware/intel/sof-tplg directory again)
- Remove the version from all paths

* Thu Apr 30 2020 Jaroslav Kysela <perex@perex.cz> - 1.4.2-5
- Add missing symlink for sof-cfl.ri

* Thu Mar 12 2020 Jaroslav Kysela <perex@perex.cz> - 1.4.2-4
- Add missing symlink for sof-cml.ri

* Mon Mar  2 2020 Jaroslav Kysela <perex@perex.cz> - 1.4.2-3
- Initial version, SOF firmware 1.4.2
