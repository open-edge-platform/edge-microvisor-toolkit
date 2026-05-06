%define         commit_hash d842d7719497cc3b774fd71620278ac9e17710e0
Summary:        CLI tool for spawning and running containers per OCI spec.
Name:           runc
# update "commit_hash" above when upgrading version
Version:        1.3.3
Release:        2%{?dist}
License:        ASL 2.0
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit
Group:          Tools/Container
URL:            https://github.com/opencontainers/runc
Source0:        https://github.com/opencontainers/runc/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

# Fix container startup failure: "open /proc/sys/kernel/cap_last_cap: no such file or directory"
# runc 1.3.3 switched from syndtr/gocapability to moby/sys/capability which
# lazily reads /proc/sys/kernel/cap_last_cap. When this read happens inside
# the container namespace before /proc is available, it fails. This patch adds
# a prctl(PR_CAPBSET_READ) fallback.
Patch0:         0001-last-cap-fallback.patch

BuildRequires:  git
BuildRequires:  go-md2man
BuildRequires:  golang < 1.25
BuildRequires:  libseccomp-devel
BuildRequires:  make
Requires:       glibc
Requires:       libgcc
Requires:       libseccomp
Provides:       moby-runc = %{version}-%{release}

%description
runc is a CLI tool for spawning and running containers according to the OCI specification. Containers are started as a child process of runC and can be embedded into various other systems without having to run a daemon.

%prep
%autosetup -p1 -n runc-%{version}

%build
export CGO_ENABLED=1
make %{?_smp_mflags} BUILDTAGS="seccomp" COMMIT="%{commit_hash}" man runc

%check
make %{?_smp_mflags} COMMIT="%{commit_hash}" localunittest

%install
make install DESTDIR=%{buildroot} PREFIX=%{_prefix} BINDIR=%{_bindir}
make install-man DESTDIR=%{buildroot} PREFIX=%{_prefix}

%files
%license LICENSE NOTICE
%{_bindir}/runc
%{_mandir}/*

%changelog
* Mon May 05 2026 Andy Peng <andy.peng@intel.com> - 1.3.3-2
- Add prctl fallback for cap_last_cap when /proc is unavailable in container namespace
- Fix container startup failure: open /proc/sys/kernel/cap_last_cap: no such file or directory

* Wed Nov 05 2025 Nan Liu <liunan@microsoft.com> - 1.3.3-1
- Upgrade to 1.3.3
- BR golang < 1.25

* Mon Nov 25 2024 Nan Liu <liunan@microsoft.com> - 1.2.2-1
- Bump version to 1.2.2
- Remove the golang version constraint

* Tue Oct 15 2024 Muhammad Falak <mwani@microsoft.com> - 1.1.12-2
- Pin golang version to <= 1.22

* Mon Feb 05 2024 Henry Beberman <henry.beberman@microsoft.com> - 1.1.12-1
- Bump version to 1.1.12
- Drop cgroups cpuset patch because it's included upstream now
- Rename spec and package to runc instead of moby-runc
