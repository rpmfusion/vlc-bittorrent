Name:           vlc-bittorrent
Version:        2.7
Release:        2%{?dist}
Summary:        Bittorrent plugin for VLC

License:        GPLv3+
URL:            https://github.com/johang/vlc-bittorrent
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  libtool
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
%autosetup
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
* Mon Oct 28 2019 Leigh Scott <leigh123linux@googlemail.com> - 2.7-2
- Rebuild for libtorrent SONAME bump

* Wed Aug 21 2019 Nicolas Chauvet <kwizart@gmail.com> - 2.7-1
- Update to 2.7

* Mon Jun 17 2019 Nicolas Chauvet <kwizart@gmail.com> - 2.6-1
- Initial spec file
