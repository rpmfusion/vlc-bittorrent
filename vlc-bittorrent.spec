Name:           vlc-bittorrent
Version:        2.11
Release:        3%{?dist}
Summary:        Bittorrent plugin for VLC

License:        GPLv3+
URL:            https://github.com/johang/vlc-bittorrent
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  autoconf-archive
BuildRequires:  desktop-file-utils

BuildRequires:  boost-devel
BuildRequires:  rb_libtorrent-devel
BuildRequires:  vlc-devel >= 3.0.0

Requires: vlc-core%{_isa}

# for compatibility
Provides: vlc-plugin-bittorrent = %{version}-%{release}


%description
With vlc-bittorrent, you can open a .torrent file or magnet link with
VLC and stream any media that it contains.


%prep
%autosetup -p1
autoreconf -vif

%build
%configure \
  --disable-static \
  --libdir=%{_libdir}/vlc/plugins/access

%make_build


%install
%make_install
find %{buildroot}%{_libdir} -name "*.la" -delete

# desktop validation
desktop-file-validate \
  %{buildroot}%{_datadir}/applications/vlc-plugin-bittorrent.desktop


%post
if [ $1 == 1 ] ; then
  %{_libdir}/vlc/vlc-cache-gen %{_libdir}/vlc/plugins &>/dev/null
fi || :

%postun
if [ $1 == 1 ] ; then
  %{_libdir}/vlc/vlc-cache-gen %{_libdir}/vlc/plugins &>/dev/null
fi || :


%files
%license LICENSE
%doc README.md
%{_libdir}/vlc/plugins/access/libaccess_bittorrent_plugin.so
%{_datadir}/applications/vlc-plugin-bittorrent.desktop


%changelog
* Thu Feb 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 18 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 21 2020 Leigh Scott <leigh123linux@gmail.com> - 2.11-1
- Update to 2.11

* Thu Jun 04 2020 Leigh Scott <leigh123linux@gmail.com> - 2.10-1
- Update to 2.10

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 29 2019 Leigh Scott <leigh123linux@gmail.com> - 2.7-3
- Add fix for rfbz#5433

* Mon Oct 28 2019 Leigh Scott <leigh123linux@googlemail.com> - 2.7-2
- Rebuild for libtorrent SONAME bump

* Wed Aug 21 2019 Nicolas Chauvet <kwizart@gmail.com> - 2.7-1
- Update to 2.7

* Mon Jun 17 2019 Nicolas Chauvet <kwizart@gmail.com> - 2.6-1
- Initial spec file
