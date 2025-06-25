Name:           yq
Summary:        yq is a portable command-line YAML, JSON, XML, CSV, TOML and properties processor.
Version:        4.45.4
Release:        1%{?dist}
License:        MIT
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit
Group:          Applications/System
URL:            https://mikefarah.gitbook.io/yq
Source0:        https://github.com/mikefarah/yq/archive/refs/tags/v%{version}.tar.gz#/%{name}-v%{version}.tar.gz
Source1:        %{name}-vendor-v%{version}.tar.gz
BuildRequires:  golang-1.24.1

%description
yq is a portable command-line YAML, JSON, XML, CSV, TOML and properties processor.

%prep
%setup -n %{name}-%{version}
tar -xf %{SOURCE1} --no-same-owner

%build
go build

%install
mkdir -p %{buildroot}%{_bindir}
install -m 0755 yq %{buildroot}%{_bindir}

%files
 %{_bindir}/yq

%changelog
* Sun May 11 2025 Mike Farah <mikefarah@gmail.com> - 4.45.4-1
- Initial Edge Microvisor Toolkit import from the source project (license: same as "License" tag)
- License verified
