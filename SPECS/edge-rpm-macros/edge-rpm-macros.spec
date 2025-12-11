# WARNING: the directory '<dir>' in '%{_libdir}/rpm/<dir>' must match the value passed through '--with-vendor' when building the 'rpm' package.
%global rcdir %{_libdir}/rpm/azl
%global rcluadir %{_libdir}/rpm/lua/azl
# Turn off auto byte compilation since when building this spec in the toolchain the needed scripts are not installed yet.
# __brp_python_bytecompile
%global __brp_python_bytecompile %{nil}
Summary:        Edge Microvisor Toolkit specific rpm macro files
Name:           edge-rpm-macros
Version:        %{emt}.0
Release:        2%{?dist}
License:        GPL+ AND MIT
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit
Group:          Development/System
Source0:        macros
Source1:        rpmrc
Source2:        default-hardened-cc1
Source3:        default-hardened-ld
Source4:        default-annobin-cc1
Source5:        macros.check
Source6:        macros.openblas-srpm
Source7:        macros.nodejs-srpm
Source8:        macros.mono-srpm
Source9:        macros.perl-srpm
Source10:       gpgverify
Source11:       macros.forge
Source12:       common.lua
Source13:       forge.lua
# macros.rust-srpm is taken from https://pagure.io/fedora-rust/rust2rpm
Source14:       macros.rust-srpm
# macros.fonts is taken from the "fontpackages-devel" package.
Source15:       macros.fonts
Source16:       macros.suse
Source17:       gen-ld-script.sh
Source18:       generate-package-note.py
Source19:       verify-package-notes.sh
### The following files should eventually move to python-rpm-macros.spec
Source20:       https://src.fedoraproject.org/rpms/python-rpm-macros/blob/f40/f/macros.python
Source21:       https://src.fedoraproject.org/rpms/python-rpm-macros/blob/f40/f/macros.python3
Source22:       https://src.fedoraproject.org/rpms/python-rpm-macros/blob/f40/f/macros.python-srpm
Source23:       https://src.fedoraproject.org/rpms/python-rpm-macros/blob/f40/f/brp-python-bytecompile
Source24:       https://src.fedoraproject.org/rpms/python-rpm-macros/blob/f40/f/macros.pybytecompile
Source25:       https://src.fedoraproject.org/rpms/python-rpm-macros/blob/f40/f/compileall2.py
Source26:       https://src.fedoraproject.org/rpms/python-rpm-macros/blob/f40/f/python.lua
Source27:       https://src.fedoraproject.org/rpms/python-rpm-macros/blob/f40/f/clamp_source_mtime.py
Source28:       https://src.fedoraproject.org/rpms/python-rpm-macros/blob/f40/f/pathfix.py
Source29:       https://src.fedoraproject.org/rpms/python-rpm-macros/blob/f40/f/brp-fix-pyc-reproducibility
Source30:       https://src.fedoraproject.org/rpms/python-rpm-macros/blob/f40/f/brp-python-hardlink
Source31:       https://src.fedoraproject.org/rpms/python-rpm-macros/blob/f40/f/import_all_modules.py
Source32:       macros.grub2
###
Provides:       redhat-rpm-config
Provides:       openblas-srpm-macros
Provides:       perl-srpm-macros
Provides:       python-srpm-macros
Provides:       python-rpm-macros
Provides:       python3-rpm-macros
Provides:       rust-srpm-macros
Provides:       azurelinux-rpm-macros

Obsoletes:      mariner-rpm-macros <= 2.0-25
Provides:       mariner-rpm-macros = %{version}-%{release}

Obsoletes:      grub2-rpm-macros <= 2.06-19%{?dist}
Provides:       grub2-rpm-macros = %{version}-%{release}

BuildArch:      noarch

%description
Edge Microvisor Toolkit specific rpm macro files.

%package -n edge-check-macros
Summary:        Edge Microvisor Toolkit specific rpm macros to override default %%check behavior
Group:          Development/System

Obsoletes:      mariner-check-macros <= 2.0-25
Provides:       mariner-check-macros = %{version}-%{release}
Provides:       azurelinux-check-macros

%description -n edge-check-macros
Edge Microvisor Toolkit specific rpm macros to override default %%check behavior

%prep
%setup -q -c -T
cp -p %{sources} .

%install
mkdir -p %{buildroot}%{rcdir}
install -p -m 644 -t %{buildroot}%{rcdir} macros rpmrc
install -p -m 444 -t %{buildroot}%{rcdir} default-hardened-*
install -p -m 444 -t %{buildroot}%{rcdir} default-annobin-*
install -p -m 755 -t %{buildroot}%{rcdir} gpgverify
install -p -m 755 -t %{buildroot}%{rcdir} compileall2.py
install -p -m 755 -t %{buildroot}%{rcdir} brp-*
install -p -m 755 -t %{buildroot}%{rcdir} pathfix.py
install -p -m 755 -t %{buildroot}%{rcdir} import_all_modules.py
install -p -m 644 -t %{buildroot}%{rcdir} clamp_source_mtime.py
install -p -m 755 -t %{buildroot}%{rcdir} gen-ld-script.sh
install -p -m 755 -t %{buildroot}%{rcdir} generate-package-note.py
install -p -m 755 -t %{buildroot}%{rcdir} verify-package-notes.sh

mkdir -p %{buildroot}%{_rpmconfigdir}/macros.d
install -p -m 644 -t %{buildroot}%{_rpmconfigdir}/macros.d macros.*
mkdir -p %{buildroot}%{_fileattrsdir}

mkdir -p %{buildroot}%{rcluadir}/{rpm,srpm}
install -p -m 644 -t %{buildroot}%{rcluadir} common.lua
install -p -m 644 -t %{buildroot}%{rcluadir}/srpm forge.lua
install -p -m 644 -t %{buildroot}%{rcluadir}/srpm python.lua

%files
%defattr(-,root,root)
%{rcdir}/macros
%{rcdir}/rpmrc
%{rcdir}/default-hardened-*
%{rcdir}/default-annobin-*
%{rcdir}/gpgverify
%{rcdir}/brp-*
%{rcdir}/import_all_modules.py
%{rcdir}/pathfix.py
%{rcdir}/clamp_source_mtime.py
%{rcdir}/compileall2.py
%{rcdir}/gen-ld-script.sh
%{rcdir}/generate-package-note.py
%{rcdir}/verify-package-notes.sh
%{_rpmconfigdir}/macros.d/macros.openblas-srpm
%{_rpmconfigdir}/macros.d/macros.nodejs-srpm
%{_rpmconfigdir}/macros.d/macros.mono-srpm
%{_rpmconfigdir}/macros.d/macros.perl-srpm
%{_rpmconfigdir}/macros.d/macros.rust-srpm
%{_rpmconfigdir}/macros.d/macros.fonts
%{_rpmconfigdir}/macros.d/macros.forge
%{_rpmconfigdir}/macros.d/macros.grub2
%{_rpmconfigdir}/macros.d/macros.suse

%dir %{rcluadir}
%dir %{rcluadir}/srpm
%dir %{rcluadir}/rpm
%{rcluadir}/*.lua
%{rcluadir}/srpm/*.lua
%{_rpmconfigdir}/macros.d/macros.pybytecompile
%{_rpmconfigdir}/macros.d/macros.python*

%files -n edge-check-macros
%{_rpmconfigdir}/macros.d/macros.check

%changelog
* Tue Dec 24 2024 Naveen Saini <naveen.kumar.saini@intel.com> - 1.0-2
- Updated initial changelog entry.

* Fri Dec 13 2024 Mun Chun Yep <mun.chun.yep@intel.com> - 1.0-1
- Original version for Edge Microvisor Toolkit. License verified.
- Based on azurelinux-rpm-macros.
