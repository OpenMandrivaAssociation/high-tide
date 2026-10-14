%undefine _debugsource_packages
%global appid io.github.nokse22.high-tide

Name:		high-tide
Version:	1.5.0
Release:	1
Summary:	Libadwaita TIDAL client for Linux
Source0:    https://github.com/Nokse22/high-tide/archive/v%{version}/%{name}-%{version}.tar.gz
URL:		https://github.com/Nokse22/high-tide
License:	GPLv3
Group:		Music


BuildRequires:  appstream
BuildRequires:  gettext
BuildRequires:	python-blueprint-compiler
BuildRequires:  pkgconfig(blueprint-compiler)
BuildRequires:	python%{pyver}dist(pygobject)
BuildRequires:	python%{pyver}dist(tidalapi)
BuildRequires:	python%{pyver}dist(pypresence)
BuildRequires:	gtk4
BuildRequires:	libadwaita-common
BuildRequires:	pkgconfig(libadwaita-1)
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	typelib(Gtk) = 4.0
BuildRequires:	typelib(Adw) = 1
# gobject-introspection provides typelib(cairo) and typelib(freetype2) without
# shipping the files. Loading Gtk 4 needs those typelibs.
BuildRequires:	lib64cairo-gir1.0
BuildRequires:	lib64freetype-gir2.0
BuildSystem:	meson


Requires:	gstreamer1.0-plugins-base
# Requires:	libgstreamer1.0
# Requires:	gstreamer1.0-flac
# Requires:	gstreamer1.0-gtk
# Requires:	python-gstreamer1.0
# Requires:	gstreamer1.0-wayland
Requires:	lib64portal1
Requires:	lib64portal-gir1
Requires:	alsa-utils
Requires:	lib64asound2
Requires:	python%{pyver}dist(pypresence)
Requires:	python%{pyver}dist(tidalapi)


%description
Third party unofficial TIDAL music client. 

Listen to your favorite music from your desktop or 
mobile Linux device at the highest quality.

%prep
%autosetup -p1

%install
%meson_install
%find_lang %{name}
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{appid}.desktop

%post
%{_bindir}/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ]
then
    %{_bindir}/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    %{_bindir}/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
   
fi

%posttrans

%{_bindir}/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files -f %{name}.lang
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/glib-2.0/schemas/*
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/icons/hicolor/*/apps/io.github.nokse22.*
%{_datadir}/appdata/%{appid}.appdata.xml

