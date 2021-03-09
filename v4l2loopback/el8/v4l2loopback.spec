Name:           v4l2loopback
Summary:        Utils for V4L2 loopback devices
Version:        0.12.5
Release:        4%{?dist}
License:        GPLv2+

URL:            https://github.com/umlaeute/v4l2loopback
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        modprobe-d-98-v4l2loopback.conf
Source2:        modules-load-d-v4l2loopback.conf

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  help2man
BuildRequires:  systemd-rpm-macros
# For kmod package
# Provides:       %{name}-kmod-common = %{version}-%{release}
Requires:       kmod-%{name} >= %{version}
# For compatibility with older name
# Provides:       %{name}-utils = %{version}-%{release}
# Obsoletes:      %{name}-utils < 0.12.5-3

BuildArch:      noarch

%description
This allows you to create "virtual video devices". Normal (v4l2)
applications will read these devices as if they were ordinary video
devices, but the video will not be read from e.g. a capture card but
instead it is generated by another application.

This package contains the utilties for %{name}.


%prep
%autosetup -p1

%build
# Nothing to build

%install
make V=1 %{?_smp_mflags} install-utils DESTDIR=%{buildroot} PREFIX=%{_prefix}
make V=1 %{?_smp_mflags} install-man DESTDIR=%{buildroot} PREFIX=%{_prefix}

install -D -m 0644 %{SOURCE1} %{buildroot}%{_modprobedir}/98-v4l2loopback.conf
install -D -m 0644 %{SOURCE2} %{buildroot}%{_modulesloaddir}/v4l2loopback.conf

%files
%doc README.md AUTHORS NEWS
%license COPYING
%attr(0755,root,root) %{_bindir}/v4l2loopback-ctl
%attr(0644,root,root) %{_mandir}/man1/v4l2loopback-ctl.1*
%{_modprobedir}/98-v4l2loopback.conf
%{_modulesloaddir}/v4l2loopback.conf


%changelog
* Sun Mar 07 2021 Akemi Yagi <toracat@elrepo.org> - 0.12.5-4
- Rebuilt for elrepo from the rpmfusion package

* Sat Feb 27 2021 Nicolas Chauvet <kwizart@gmail.com> - 0.12.5-3
- Fix v4l2loopback-kmod deps

* Mon Feb 15 2021 Nicolas Chauvet <kwizart@gmail.com> - 0.12.5-2
- Rename to v4l2loopback

* Sat Dec 26 2020 Neal Gompa <ngompa13@gmail.com> - 0.12.5-1
- Initial packaging
