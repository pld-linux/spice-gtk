#
# Conditional build:
%bcond_without	smartcard	# Smartcard support
%bcond_without	usbredir	# USB redirection
%bcond_with	valgrind	# Valgrind tracing support

Summary:	A GTK+ client and libraries for SPICE remote desktop servers
Summary(pl.UTF-8):	Klient i biblioteki GTK+ dla serwerów zdalnych pulpitów SPICE
Name:		spice-gtk
Version:	0.42
Release:	1
License:	LGPL v2.1+
Group:		X11/Applications
Source0:	https://www.spice-space.org/download/gtk/%{name}-%{version}.tar.xz
# Source0-md5:	68becfc1192a61265e9981621e9d3dc6
URL:		https://spice-space.org/
BuildRequires:	cairo-devel >= 1.2.0
BuildRequires:	cyrus-sasl-devel >= 2.0
BuildRequires:	gcc >= 5:3.0
BuildRequires:	gettext-tools >= 0.19.8
BuildRequires:	glib2-devel >= 1:2.52
BuildRequires:	gobject-introspection-devel >= 0.9.4
BuildRequires:	gstreamer-devel >= 1.10
BuildRequires:	gstreamer-plugins-base-devel >= 1.10
BuildRequires:	gtk+3-devel >= 3.22
BuildRequires:	gtk-doc >= 1.14
BuildRequires:	json-glib-devel
%{?with_smartcard:BuildRequires:	libcacard-devel >= 2.5.1}
BuildRequires:	libepoxy-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libsoup3-devel >= 3.0
BuildRequires:	libstdc++-devel
BuildRequires:	libva-x11-devel
BuildRequires:	lz4-devel
BuildRequires:	meson >= 0.56
BuildRequires:	ninja >= 1.5
BuildRequires:	openssl-devel >= 1.0.0
BuildRequires:	opus-devel >= 0.9.14
BuildRequires:	perl-tools-pod
BuildRequires:	phodav3-devel >= 3.0
BuildRequires:	pixman-devel >= 0.17.7
BuildRequires:	pkgconfig
BuildRequires:	python3
BuildRequires:	python3-pyparsing
BuildRequires:	python3-six
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	sed >= 4.0
BuildRequires:	spice-protocol >= 0.14.3
BuildRequires:	tar >= 1:1.22
BuildRequires:	vala >= 0.14
# <valgrind/valgrind.h>
%{?with_valgrind:BuildRequires:	valgrind}
BuildRequires:	wayland-devel >= 1.17.0
BuildRequires:	wayland-protocols >= 1.17
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXrandr-devel
BuildRequires:	xz
BuildRequires:	zlib-devel
%if %{with usbredir}
BuildRequires:	acl-devel
BuildRequires:	libusb-devel >= 1.0.21
BuildRequires:	polkit-devel >= 0.101
BuildRequires:	usbredir-devel >= 0.7.1
%endif
Requires:	gtk+3 >= 3.22
Requires:	spice-glib = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A GTK+ client and libraries for SPICE remote desktop servers.

%description -l pl.UTF-8
Klient i biblioteki GTK+ dla serwerów zdalnych pulpitów SPICE.

%package devel
Summary:	Header files for SPICE GTK 3.0 client library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki klienckiej SPICE GTK 3.0
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+3-devel >= 3.22
Requires:	libepoxy-devel
Requires:	libva-x11-devel
Requires:	spice-glib-devel = %{version}-%{release}
Requires:	xorg-lib-libX11-devel

%description devel
Header files for SPICE GTK 3.0 client library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki klienckiej SPICE GTK 3.0.

%package static
Summary:	Static SPICE GTK 3.0 client library
Summary(pl.UTF-8):	Statyczna biblioteka kliencka SPICE GTK 3.0
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static SPICE GTK 3.0 client library.

%description static -l pl.UTF-8
Statyczna biblioteka kliencka SPICE GTK 3.0.

%package -n vala-spice-gtk
Summary:	Vala API for SPICE GTK client library
Summary(pl.UTF-8):	Interfejs języka Vala do biblioteki klienckiej SPICE GTK
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	vala >= 2:0.14
Requires:	vala-spice-glib = %{version}-%{release}
BuildArch:	noarch

%description -n vala-spice-gtk
Vala API for SPICE GTK client library.

%description -n vala-spice-gtk -l pl.UTF-8
Interfejs języka Vala do biblioteki klienckiej SPICE GTK.

%package apidocs
Summary:	SPICE GTK API documentation
Summary(pl.UTF-8):	Dokumentacja API bibliotek SPICE GTK
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for SPICE GTK libraries.

%description apidocs -l pl.UTF-8
Dokumentacja API bibliotek SPICE GTK.

%package -n spice-glib
Summary:	SPICE Client GLib library
Summary(pl.UTF-8):	Biblioteka kliencka SPICE GLib
Group:		Libraries
Requires:	cairo >= 1.2.0
Requires:	glib2 >= 1:2.52
%{?with_smartcard:Requires:	libcacard >= 2.5.1}
Requires:	libsoup3 >= 3.0
Requires:	gstreamer >= 1.10
Requires:	gstreamer-plugins-base >= 1.10
Requires:	openssl >= 1.0.0
Requires:	opus >= 0.9.14
Requires:	pixman >= 0.17.7
%if %{with usbredir}
Requires:	libusb >= 1.0.21
Requires:	usbredir >= 0.7.1
%endif

%description -n spice-glib
SPICE Client GLib library.

%description -n spice-glib -l pl.UTF-8
Biblioteka kliencka SPICE GLib.

%package -n spice-glib-devel
Summary:	Header files for SPICE Client GLib library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki klienckiej SPICE GLib
Group:		Development/Libraries
Requires:	cairo-devel >= 1.2.0
Requires:	cyrus-sasl-devel >= 2.0
Requires:	glib2-devel >= 1:2.52
Requires:	gobject-introspection-devel >= 0.9.4
Requires:	gstreamer-devel >= 1.10
Requires:	gstreamer-plugins-base-devel >= 1.10
Requires:	json-glib-devel
%{?with_smartcard:Requires:	libcacard-devel >= 2.5.1}
Requires:	libcap-ng-devel
Requires:	libjpeg-devel
Requires:	libsoup3-devel >= 3.0
Requires:	lz4-devel
Requires:	openssl-devel >= 1.0.0
Requires:	opus-devel >= 0.9.14
Requires:	phodav3-devel >= 3.0
Requires:	pixman-devel >= 0.17.7
Requires:	spice-glib = %{version}-%{release}
Requires:	spice-protocol >= 0.14.3
Requires:	zlib-devel
%if %{with usbredir}
Requires:	libusb-devel >= 1.0.21
Requires:	usbredir-devel >= 0.7.1
%endif

%description -n spice-glib-devel
Header files for SPICE Client GLib library.

%description -n spice-glib-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki klienckiej SPICE GLib.

%package -n spice-glib-static
Summary:	SPICE Client GLib static library
Summary(pl.UTF-8):	Statyczna biblioteka kliencka SPICE GLib
Group:		Development/Libraries
Requires:	spice-glib-devel = %{version}-%{release}

%description -n spice-glib-static
SPICE Client GLib static library.

%description -n spice-glib-static -l pl.UTF-8
Statyczna biblioteka kliencka SPICE GLib.

%package -n vala-spice-glib
Summary:	Vala API for SPICE GLib client library
Summary(pl.UTF-8):	Interfejs języka Vala do biblioteki klienckiej SPICE GLib
Group:		Development/Libraries
Requires:	spice-glib-devel = %{version}-%{release}
Requires:	vala >= 2:0.14
# versions 0.35 through 0.38-1 were actually spice-client-glib + spice-client-gtk vapis
Obsoletes:	vala-spice-protocol < 0.38-2
BuildArch:	noarch

%description -n vala-spice-glib
Vala API for SPICE GLib client library.

%description -n vala-spice-glib -l pl.UTF-8
Interfejs języka Vala do biblioteki klienckiej SPICE GLib.

%package -n spice-glib-usb
Summary:	USB redirection ACL helper for SPICE Client GLib library
Summary(pl.UTF-8):	Program pomocniczy ACL do przekierowań USB dla biblioteki klienckiej SPICE GLib
Group:		Applications/System
Requires:	polkit >= 0.101
Requires:	spice-glib = %{version}-%{release}

%description -n spice-glib-usb
USB redirection ACL helper for SPICE Client GLib library.

%description -n spice-glib-usb -l pl.UTF-8
Program pomocniczy ACL do przekierowań USB dla biblioteki klienckiej
SPICE GLib.

%prep
%setup -q

%build
%meson \
	-Dgtk_doc=enabled \
	-Dlz4=enabled \
	-Dpolkit=%{?with_usbredir:enabled}%{!?with_smartcard:usbredir} \
	-Dsmartcard=%{?with_smartcard:enabled}%{!?with_smartcard:disabled} \
	-Dusbredir=%{?with_usbredir:enabled}%{!?with_smartcard:usbredir} \
	-Dusb-ids-path=/lib/hwdata/usb.ids \
	%{?with_valgrind:-Dvalgrind=true} \
	-Dvapi=enabled

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	-n spice-glib -p /sbin/ldconfig
%postun	-n spice-glib -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS CHANGELOG.md README.md
%attr(755,root,root) %{_bindir}/spicy
%attr(755,root,root) %{_bindir}/spicy-screenshot
%attr(755,root,root) %{_bindir}/spicy-stats
%attr(755,root,root) %{_libdir}/libspice-client-gtk-3.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libspice-client-gtk-3.0.so.5
%{_libdir}/girepository-1.0/SpiceClientGtk-3.0.typelib
%{_mandir}/man1/spice-client.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libspice-client-gtk-3.0.so
%{_includedir}/spice-client-gtk-3.0
%{_pkgconfigdir}/spice-client-gtk-3.0.pc
%{_datadir}/gir-1.0/SpiceClientGtk-3.0.gir

%files static
%defattr(644,root,root,755)
%{_libdir}/libspice-client-gtk-3.0.a

%files -n vala-spice-gtk
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/spice-client-gtk-3.0.deps
%{_datadir}/vala/vapi/spice-client-gtk-3.0.vapi

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/spice-gtk

%files -n spice-glib
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libspice-client-glib-2.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libspice-client-glib-2.0.so.8
%{_libdir}/girepository-1.0/SpiceClientGLib-2.0.typelib

%files -n spice-glib-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libspice-client-glib-2.0.so
%{_includedir}/spice-client-glib-2.0
%{_pkgconfigdir}/spice-client-glib-2.0.pc
%{_datadir}/gir-1.0/SpiceClientGLib-2.0.gir

%files -n spice-glib-static
%defattr(644,root,root,755)
%{_libdir}/libspice-client-glib-2.0.a

%files -n vala-spice-glib
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/spice-client-glib-2.0.deps
%{_datadir}/vala/vapi/spice-client-glib-2.0.vapi

%if %{with usbredir}
%files -n spice-glib-usb
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/spice-client-glib-usb-acl-helper
%{_datadir}/polkit-1/actions/org.spice-space.lowlevelusbaccess.policy
%endif
