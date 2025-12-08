# Glslang revision from packaged version
%global glslang_version 8c2e602ce440b7739c95ff3d69cecb1adf6becda
%global url https://github.com/google/shaderc

Name:           shaderc
Version:        2025.3
Release:        1%{?dist}
Distribution:   Edge Microvisor Toolkit
Vendor:         Intel Corporation
Summary:        Collection of tools, libraries, and tests for Vulkan shader compilation
 
License:        Apache-2.0
URL:            %{url}
Source:         %{url}/archive/%{glslang_version}.tar.gz
# Patch to unbundle 3rd party code
Patch:          0001-Drop-third-party-code-in-CMakeLists.txt.patch
Patch:          glslang_linker_flags.patch
 
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  sed
BuildRequires:  spirv-tools
 
BuildRequires:  glslang-devel
BuildRequires:  python3-devel
BuildRequires:  spirv-headers-devel
BuildRequires:  spirv-tools-devel
 
%description
A collection of tools, libraries and tests for shader compilation.
 
Shaderc aims to to provide:
 - a command line compiler with GCC- and Clang-like usage, for better
   integration with build systems
 - an API where functionality can be added without breaking existing clients
 - an API supporting standard concurrency patterns across multiple
   operating systems
 - increased functionality such as file #include support
 
%package    -n  glslc
Summary:        A command line compiler for GLSL/HLSL to SPIR-V
 
%description -n glslc
A command line compiler for GLSL/HLSL to SPIR-V.
 
%package    -n  libshaderc
Summary:        A library for compiling shader strings into SPIR-V
 
%description -n libshaderc
A library for compiling shader strings into SPIR-V.
 
%package -n     libshaderc-devel
Summary:        Development files for libshaderc
Requires:       libshaderc%{?_isa} = %{version}-%{release}
 
%description -n libshaderc-devel
A library for compiling shader strings into SPIR-V.
 
Development files for libshaderc.
 
%package -n     libshaderc-static
Summary:        A library for compiling shader strings into SPIR-V (static libraries)
 
%description -n libshaderc-static
A library for compiling shader strings into SPIR-V.
 
Static libraries for libshaderc.
 
%prep
%autosetup -p1 -n %{name}-%{glslang_version}
 
rm -r third_party
 
# Stolen from Gentoo
# Create build-version.inc since we want to use our packaged
# SPIRV-Tools and glslang
sed -i -e '/build-version/d' glslc/CMakeLists.txt
echo \"shaderc $(grep -m1 -o '^v[[:digit:]]\{4\}\.[[:digit:]]\(-dev\)\? [[:digit:]]\{4\}-[[:digit:]]\{2\}-[[:digit:]]\{2\}$' CHANGES)\" \
        > glslc/src/build-version.inc
echo \"spirv-tools $(grep -m1 -o '^v[[:digit:]]\{4\}\.[[:digit:]]\(-dev\)\? [[:digit:]]\{4\}-[[:digit:]]\{2\}-[[:digit:]]\{2\}$' /usr/share/doc/spirv-tools/CHANGES)\" \
        >> glslc/src/build-version.inc
echo \"glslang %{glslang_version}\" >> glslc/src/build-version.inc
 
# Point to correct include
sed -i 's|SPIRV/GlslangToSpv.h|glslang/SPIRV/GlslangToSpv.h|' libshaderc_util/src/compiler.cc || true

%build
# We disable the tests because they don't work with our unbundling of 3rd party.
# See https://github.com/google/shaderc/issues/470
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -DCMAKE_SKIP_RPATH=True \
       -DSHADERC_SKIP_TESTS=True \
       -DPYTHON_EXECUTABLE=%{python3} \
       -GNinja
%cmake_build
 
%install
%cmake_install
 
%check
%ctest
 
%files -n glslc
%doc glslc/README.asciidoc
%license LICENSE
%{_bindir}/glslc
 
%files -n libshaderc
%doc AUTHORS CHANGES CONTRIBUTORS README.md
%license LICENSE
%{_libdir}/libshaderc_shared.so.1*
 
%files -n libshaderc-devel
%{_includedir}/%{name}/
%{_libdir}/libshaderc_shared.so
%{_libdir}/pkgconfig/shaderc.pc
 
%files -n libshaderc-static
%license LICENSE
%{_libdir}/libshaderc.a
%{_libdir}/libshaderc_combined.a
%{_libdir}/pkgconfig/shaderc_static.pc
%{_libdir}/pkgconfig/shaderc_combined.pc
 
%changelog
* Fri Nov 21 2025 Polmoorx Shiva Kumar <polmoorx.shiva.kumar@intel.com> - 2025.3-1
- Initial Edge Microvisor Toolkit import from Fedora 43 (license: MIT). License verified.

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2021.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild
 
* Sun May 30 11:26:42 CEST 2021 Robert-André Mauchin <zebob.m@gmail.com> - 2021.0-2
- Update to 2021.0
- Fix changelog
- Close: rhbz#1952332
 
* Fri Mar  5 13:43:44 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 2020.5-1
- Update to 2020.5
- Close: rhbz#1931006
 
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2020.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild
 
* Sat Dec 26 15:21:39 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 2020.4-1
- Update to 2020.4
- Close: rhbz#1906260
 
* Sat Dec 05 2020 Robert-André Mauchin <zebob.m@gmail.com> - 2020.3-1
- Update to 2020.3
- Close: rhbz#1875183
 
* Sat Aug 08 2020 Robert-André Mauchin <zebob.m@gmail.com> - 2020.2-1
- Update to 2020.2
 
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2020.1-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild
 
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2020.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild
 
* Wed Jun 17 20:15:27 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 2020.1-1
- Update to 2020.1
 
* Sun Feb 02 20:53:01 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 2019.1-1
- Update to 2019.1
 
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2019.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild
 
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2019.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild
 
* Mon Jun 10 00:18:18 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 2019.0-1
- Release 2019.0
 
* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2018.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild
 
* Wed Oct 03 2018 Robert-André Mauchin <zebob.m@gmail.com> - 2018.0-1
- Release 2018.0
 
* Mon Sep 24 2018 Robert-André Mauchin <zebob.m@gmail.com> - 2017.2-1
- Initial build 
