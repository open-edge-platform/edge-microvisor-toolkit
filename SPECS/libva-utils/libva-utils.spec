#global pre_release .pre1

Name:		libva-utils
Version:	2.23.0
Release:	1%{?dist}
Summary:	Tools for VAAPI (including vainfo)
License:	LicenseRef-Callaway-MIT AND LicenseRef-Callaway-BSD
Distribution:   Edge Microvisor Toolkit
Vendor:         Intel Corporation
URL:		https://github.com/intel/libva-utils
Source0:	%{url}/archive/%{version}%{?pre_release}/%{name}-%{version}%{?pre_release}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc-c++

BuildRequires:	libXext-devel
BuildRequires:	libXfixes-devel
BuildRequires:	libdrm-devel
BuildRequires:  libva-devel
%{!?_without_wayland:
BuildRequires:  wayland-devel
BuildRequires:  pkgconfig(wayland-client) >= 1
BuildRequires:  pkgconfig(wayland-scanner) >= 1
}

%description
The libva-utils package contains tools that are provided as part
of libva, including the vainfo tool for determining what (if any)
libva support is available on a system.


%prep
%autosetup -p1 -n %{name}-%{version}%{?pre_release}

%build
%meson \
%{?_with_tests: -Dtests=true} \
%{?_without_wayland: -Dwayland=false}

%meson_build


%install
%meson_install


%files
%license COPYING
%doc CONTRIBUTING.md README.md
%{_bindir}/av1encode
%{_bindir}/vainfo
%{_bindir}/loadjpeg
%{_bindir}/jpegenc
%{_bindir}/avcenc
%{_bindir}/avcstreamoutdemo
%{_bindir}/h264encode
%{_bindir}/hevcencode
%{_bindir}/mpeg2vldemo
%{_bindir}/mpeg2vaenc
%{_bindir}/putsurface
%{_bindir}/sfcsample
%{?_with_tests:%{_bindir}/test_va_api}
%{_bindir}/vacopy
%{_bindir}/vavpp
%{_bindir}/vp8enc
%{_bindir}/vp9enc
%{_bindir}/vpp3dlut
%{_bindir}/vppblending
%{_bindir}/vppchromasitting
%{_bindir}/vppdenoise
%{_bindir}/vpphdr_tm
%{_bindir}/vppscaling_csc
%{_bindir}/vppscaling_n_out_usrptr
%{_bindir}/vppsharpness
%{!?_without_wayland:%{_bindir}/putsurface_wayland}


%changelog
* Wed Jul 1 2026 Lee Chee Yang <chee.yang.lee@intel.com> - 2.23.0-1
- upgrade to 2.23.0

* Mon Aug 18 2025 Rajesh Shanmugam <rajesh1x.shanmugam@intel.com> - 2.22.0-5
- Initial Edge Microvisor Toolkit import from Fedora 42 (license: MIT)
- License verified

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.22.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 2.22.0-3
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jun 20 2024 Nicolas Chauvet <kwizart@gmail.com> - 2.22.0-1
- Update to 2.22.0

* Tue Mar 19 2024 Nicolas Chauvet <kwizart@gmail.com> - 2.21.0-1
- Update to 2.21.0

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.20.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.20.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Dec 06 2023 Nicolas Chauvet <kwizart@gmail.com> - 2.20.1-1
- Update to 2.20.1

* Sun Sep 17 2023 Nicolas Chauvet <kwizart@gmail.com> - 2.20.0-1
- Update to 2.20.0

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.19.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 04 2023 Nicolas Chauvet <kwizart@gmail.com> - 2.19.0-1
- Update to 2.19.0

* Tue Apr 18 2023 Nicolas Chauvet <kwizart@gmail.com> - 2.18.2-1
- Update to 2.18.2

* Wed Mar 29 2023 Nicolas Chauvet <kwizart@gmail.com> - 2.18.1-1
- Update to 2.18.1

* Tue Mar 21 2023 Nicolas Chauvet <kwizart@gmail.com> - 2.18.0-1
- Update to 2.18.0

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.17.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan 09 2023 Nicolas Chauvet <kwizart@gmail.com> - 2.17.1-1
- Update to 2.17.1

* Wed Dec 28 2022 Nicolas Chauvet <kwizart@gmail.com> - 2.17.0-1
- Update to 2.17.0

* Fri Oct 14 2022 Nicolas Chauvet <kwizart@gmail.com> - 2.16.0-1
- Update to 2.16.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 01 2022 Nicolas Chauvet <kwizart@gmail.com> - 2.15.0-1
- Update to 2.15.0

* Thu Feb 17 2022 Nicolas Chauvet <kwizart@gmail.com> - 2.14.0-1
- Update to 2.14.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Oct 03 2021 Nicolas Chauvet <nchauvet@linagora.com> - 2.13.0-1
- Update to 2.13.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 22 2021 Nicolas Chauvet <kwizart@gmail.com> - 2.12.0-1
- Update to 2.12.0

* Wed May 05 2021 Nicolas Chauvet <kwizart@gmail.com> - 2.11.1-1
- Update to 2.11.1

* Wed Mar 24 2021 Nicolas Chauvet <kwizart@gmail.com> - 2.11.0-1
- Update to 2.11.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec 30 2020 Nicolas Chauvet <kwizart@gmail.com> - 2.10.0-1
- Update to 2.10.0

* Sun Oct 11 2020 Nicolas Chauvet <kwizart@gmail.com> - 2.9.1-1
- Update to 2.9.1

* Sun Sep 13 2020 Nicolas Chauvet <kwizart@gmail.com> - 2.9.0-1
- Update to 2.9.0

* Wed Sep 09 2020 Nicolas Chauvet <kwizart@gmail.com> - 2.9.0-0.1.pre1
- Update to 2.9.0.pre1

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 29 2020 Nicolas Chauvet <kwizart@gmail.com> - 2.8.0-1
- Update to 2.8.0

* Thu Apr 02 2020 Nicolas Chauvet <kwizart@gmail.com> - 2.7.1-1
- Update to 2.7.1

* Thu Mar 26 2020 Nicolas Chauvet <kwizart@gmail.com> - 2.6.0-1
- Update to 2.6.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 23 2019 Nicolas Chauvet <kwizart@gmail.com> - 2.5.0-1
- Update to 2.5.0

* Mon Sep 23 2019 Nicolas Chauvet <kwizart@gmail.com> - 2.4.1-1
- Update to 2.4.1

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 14 2019 Michael Cronenworth <mike@cchtml.com> - 2.4.0-1
- Update to 2.4.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 05 2018 Nicolas Chauvet <kwizart@gmail.com> - 2.3.0-1
- Update to 2.3.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Nicolas Chauvet <kwizart@gmail.com> - 2.2.0-1
- Update to 2.2.0

* Sat Jun 02 2018 Nicolas Chauvet <kwizart@gmail.com> - 2.1.1-0.1.pre1
- Update to 2.1.1.pre1-20180601

* Mon Mar 19 2018 Nicolas Chauvet <kwizart@gmail.com> - 2.1.0-2
- Switch to github.com/intel URL

* Mon Feb 12 2018 Nicolas Chauvet <kwizart@gmail.com> - 2.1.0-1
- Update to 2.1.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Oct 24 2017 Nicolas Chauvet <kwizart@gmail.com> - 2.0.0-1
- Update to 2.0.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 12 2017 Nicolas Chauvet <kwizart@gmail.com> - 1.8.3-1
- Update to 1.8.3

* Tue May 23 2017 Nicolas Chauvet <kwizart@gmail.com> - 1.8.2-1
- Update to 1.8.2

* Mon Apr 10 2017 Nicolas Chauvet <kwizart@gmail.com> - 1.8.1-1
- Update to 1.8.1

* Fri Mar 31 2017 Nicolas Chauvet <kwizart@gmail.com> - 1.8.0-1
- Initial spec file for libva-utils

