Summary:        Package for Mariner to meet Azure Security Baseline 
Name:           asc
Version:        %{emt}.0
Release:        2%{?dist}
License:        MIT
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit
Group:          System Environment/Base
URL:            https://aka.ms/mariner
Requires:       filesystem-asc

%description
Package for Mariner to meet Azure Security Baseline by adding multiple config files in /etc/modprobe.d

%prep

%build

%files
%defattr(-,root,root,0755)

%changelog
* Tue Sep 30 2025 Andy <andy.peng@intel.com> - 3.0-2
- Bump version for release

* Tue Feb 27 2024 Muhammad Falak <mwani@microsoft.com> - 3.0-1
- Bump version to 3.0 for AzureLiux 3.0

* Tue Aug 16 2022 Minghe Ren <mingheren@microsoft.com> - 1.0-1
- Initial CBL-Mariner import from Azure (license: MIT)
- License verified
