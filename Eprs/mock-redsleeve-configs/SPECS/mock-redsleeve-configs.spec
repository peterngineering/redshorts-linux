Name:       mock-redsleeve-configs
Version:    44.4
Release:    1%{?dist}
Summary:    Mock RedSleeve Linux config files basic chroots

License:    GPL-2.0-or-later
URL:        https://redsleeve.org/
Source:     %{name}-%{version}.tar.gz
BuildArch:  noarch

Provides: mock-redsleeve-configs

# distribution-gpg-keys contains GPG keys used by mock configs
Requires:   distribution-gpg-keys >= 1.117
# specify specific compatible version of mock for rsel
# newer versions HAVE NOT YET been tested
Requires:   mock >= 3.0-1
Requires:   mock-filesystem 
Requires:   mock-core-configs 
Requires:   redsleeve-release >= 9.8
Requires(post): coreutils
# to detect correct default.cfg
# python3-libdnf5 - Fedora and RHEL10+
# python3-dnf and python3-hawkey - older systems
Requires(post): (python3-libdnf5 or (python3-dnf and python3-hawkey))
Requires(post): system-release
Requires(post): python3

%description
Mock configuration files which allow you to create chroots for RedSleeve Linux

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{_sysconfdir}/mock/templates
cp -a etc/mock/redsleeve*.cfg %{buildroot}%{_sysconfdir}/mock
cp -a etc/mock/templates/redsleeve*.tpl %{buildroot}%{_sysconfdir}/mock/templates

%files
%{_sysconfdir}/mock/redsleeve*.cfg
%{_sysconfdir}/mock/templates/redsleeve*.tpl
%license COPYING
%doc README

%changelog
* Sat Aug 08 2026 mockbuild - 44.4-1
- create redsleeve armv6hl/armv7hl mock configs pkg for RSEL community

