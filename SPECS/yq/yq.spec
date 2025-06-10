Name:           yq
Summary:        yq is a portable command-line YAML, JSON, XML, CSV, TOML and properties processor.
Version:        4.45.4
Release:        1%{?dist}
License:        MIT
Distribution:   Azure Linux
Vendor:         Microsoft Corporation
Group:          Applications/System
URL:            https://mikefarah.gitbook.io/yq
Source0:        https://github.com/mikefarah/yq/archive/refs/tags/v%{version}.tar.gz#/%{name}-v%{version}.tar.gz
Source1:        %{name}-vendor-v%{version}.tar.gz
BuildRequires:  golang

%description
yq is a portable command-line YAML, JSON, XML, CSV, TOML and properties processor.

%prep
%setup -n %{name}-%{version}
tar -xf %{SOURCE1} --no-same-owner

%build
go build

%install
mkdir -p %{buildroot}/usr/local/bin
install -m 0755 yq %{buildroot}/usr/local/bin/yq

%files
/usr/local/bin/yq

%changelog
* Sun May 11 2025 Mike Farah <mikefarah@gmail.com> - v4.45.4
- Initial Azure Linux import from the source project (license: same as "License" tag)
- License verified
