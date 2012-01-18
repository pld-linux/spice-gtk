#
# Conditional build:
%bcond_without	gtk2		# GTK+ 2 interfaces
%bcond_without	gtk3		# GTK+ 3 interfaces
%bcond_without	smartcard	# Smartcard support
%bcond_without	usbredir	# USB redirection
#
Summary:	A GTK+ client and libraries for SPICE remote desktop servers
Summary(pl.UTF-8):	Klient i biblioteki GTK+ dla serwerów zdalnych pulpitów SPICE
Name:		spice-gtk
Version:	0.8
Release:	1
License:	LGPL v2.1+
Group:		X11/Applications
Source0:	http://spice-space.org/download/gtk/%{name}-%{version}.tar.bz2
# Source0-md5:	761b6c3d74d962d437bdd72f54292498
Patch0:		%{name}-sh.patch
Patch1:		%{name}-builddir.patch
Patch2:		%{name}-usbredir.patch
URL:		http://spice-space.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1.6
BuildRequires:	cairo-devel >= 1.2.0
BuildRequires:	celt051-devel >= 0.5.1.1
BuildRequires:	cyrus-sasl-devel >= 2.0
BuildRequires:	gettext-devel >= 0.17
BuildRequires:	gobject-introspection-devel >= 0.9.4
BuildRequires:	glib2-devel >= 1:2.22
BuildRequires:	gtk-doc >= 1.14
%{?with_gtk3:BuildRequires:	gtk+3-devel >= 3.0}
BuildRequires:	intltool >= 0.40.0
%{?with_smartcard:BuildRequires:	libcacard-devel >= 0.1.2}
BuildRequires:	libjpeg-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:2.0
BuildRequires:	openssl-devel
BuildRequires:	perl-Text-CSV
BuildRequires:	perl-base >= 1:5.8.1
BuildRequires:	pixman-devel >= 0.17.7
BuildRequires:	pkgconfig
BuildRequires:	pulseaudio-devel
BuildRequires:	spice-protocol >= 0.10.1
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXrandr-devel
BuildRequires:	zlib-devel
%if %{with gtk2}
BuildRequires:	gtk+2-devel >= 2:2.18.0
BuildRequires:	python-devel >= 2.0
BuildRequires:	python-pygtk-devel >= 2:2.0.0
%endif
%if %{with usbredir}
BuildRequires:	acl-devel
BuildRequires:	libusb-devel >= 1.0.9
BuildRequires:	polkit-devel >= 0.96
BuildRequires:	udev-glib-devel
BuildRequires:	usbredir-devel >= 0.3.3
%endif
%{?with_smartcard:Requires:	libcacard >= 0.1.2}
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
Requires:	spice-glib-devel = %{version}-%{release}
Requires:	gtk+3-devel >= 3.0

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

%package apidocs
Summary:	SPICE GTK API documentation
Summary(pl.UTF-8):	Dokumentacja API bibliotek SPICE GTK
Group:		Documentation

%description apidocs
API documentation for SPICE GTK libraries.

%description apidocs -l pl.UTF-8
Dokumentacja API bibliotek SPICE GTK.

%package -n spice-glib
Summary:	SPICE Client GLib library
Summary(pl.UTF-8):	Biblioteka kliencka SPICE GLib
Group:		Libraries
Requires:	celt051 >= 0.5.1.1
Requires:	glib2 >= 1:2.22
%{?with_smartcard:Requires:	libcacard >= 0.1.2}
Requires:	pixman >= 0.17.7
%if %{with usbredir}
Requires:	libusb >= 1.0.9
Requires:	usbredir >= 0.3.3
%endif

%description -n spice-glib
SPICE Client GLib library.

%description -n spice-glib -l pl.UTF-8
Biblioteka kliencka SPICE GLib.

%package -n spice-glib-devel
Summary:	Header files for SPICE Client GLib library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki klienckiej SPICE GLib
Group:		Development/Libraries
Requires:	celt051-devel >= 0.5.1.1
Requires:	cyrus-sasl-devel >= 2.0
Requires:	glib2-devel >= 1:2.22
%{?with_smartcard:Requires:	libcacard-devel >= 0.1.2}
Requires:	libjpeg-devel
Requires:	openssl-devel
Requires:	pixman-devel >= 0.17.7
Requires:	pulseaudio-devel
Requires:	spice-glib = %{version}-%{release}
Requires:	spice-protocol >= 0.10.1
%if %{with usbredir}
Requires:	libusb-devel >= 1.0.9
Requires:	udev-glib-devel
Requires:	usbredir-devel >= 0.3.3
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

%package -n spice-glib-usb
Summary:	USB redirection ACL helper for SPICE Client GLib library
Summary(pl.UTF-8):	Program pomocniczy ACL do przekierowań USB dla biblioteki klienckiej SPICE GLib
Group:		Applications/System
Requires:	spice-glib = %{version}-%{release}
Requires:	polkit >= 0.96

%description -n spice-glib-usb
USB redirection ACL helper for SPICE Client GLib library.

%description -n spice-glib-usb -l pl.UTF-8
Program pomocniczy ACL do przekierowań USB dla biblioteki klienckiej
SPICE GLib.

%package -n spice-gtk2
Summary:	SPICE Client GTK 2.0 library
Summary(pl.UTF-8):	Biblioteka kliencka SPICE GTK 2.0
Group:		X11/Libraries
Requires:	gtk+2 >= 2:2.18.0
Requires:	spice-glib = %{version}-%{release}

%description -n spice-gtk2
SPICE Client GTK 2.0 library.

%description -n spice-gtk2 -l pl.UTF-8
Biblioteka kliencka SPICE GTK 2.0.

%package -n spice-gtk2-devel
Summary:	Header files for SPICE Client GTK 2.0 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki klienckiej SPICE GTK 2.0
Group:		X11/Development/Libraries
Requires:	gtk+2-devel >= 2:2.18.0
Requires:	spice-glib-devel = %{version}-%{release}

%description -n spice-gtk2-devel
Header files for SPICE Client GTK 2.0 library.

%description -n spice-gtk2-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki klienckiej SPICE GTK 2.0.

%package -n spice-gtk2-static
Summary:	SPICE Client GTK 2.0 static library
Summary(pl.UTF-8):	Statyczna biblioteka kliencka SPICE GTK 2.0
Group:		X11/Development/Libraries
Requires:	spice-gtk2-devel = %{version}-%{release}

%description -n spice-gtk2-static
SPICE Client GTK 2.0 static library.

%description -n spice-gtk2-static -l pl.UTF-8
Statyczna biblioteka kliencka SPICE GTK 2.0.

%package -n python-spice-gtk
Summary:	Python interface to SPICE client GTK library
Summary(pl.UTF-8):	Pythonowy interfejs do biblioteki klienckiej SPICE GTK
Group:		Libraries/Python
Requires:	spice-gtk2 = %{version}-%{release}

%description -n python-spice-gtk
Python interface to SPICE client GTK library.

%description -n python-spice-gtk -l pl.UTF-8
Pythonowy interfejs do biblioteki klienckiej SPICE GTK.

%package -n vala-spice-protocol
Summary:	Vala API for SPICE client library
Summary(pl.UTF-8):	Interfejs języka Vala do biblioteki klienckiej SPICE
Group:		Development/Libraries
Requires:	spice-protocol >= 0.10.1
Requires:	vala >= 0.14

%description -n vala-spice-protocol
Vala API for SPICE client library.

%description -n vala-spice-protocol -l pl.UTF-8
Interfejs języka Vala do biblioteki klienckiej SPICE.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

mkdir %{?with_gtk2:gtk2} %{?with_gtk3:gtk3}

%build
%{__gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}

%if %{with gtk2}
cd gtk2
../%configure \
	--disable-silent-rules \
	%{!?with_smartcard:--disable-smartcard} \
	%{!?with_usbredir:--disable-usbredir} \
	--with-gtk=2.0 \
	--with-html-dir=%{_gtkdocdir}
%{__make}
cd ..
%endif

%if %{with gtk3}
cd gtk3
../%configure \
	--disable-silent-rules \
	%{!?with_smartcard:--disable-smartcard} \
	%{!?with_usbredir:--disable-usbredir} \
	--enable-gtk-doc \
	--with-gtk=3.0 \
	--with-html-dir=%{_gtkdocdir}
%{__make}
%endif

%install
rm -rf $RPM_BUILD_ROOT

# gtk2 first, so executables will use gtk3 libs
%if %{with gtk2}
%{__make} -C gtk2 install -j1 \
	DESTDIR=$RPM_BUILD_ROOT
%endif

%if %{with gtk3}
%{__make} -C gtk3 install -j1 \
	DESTDIR=$RPM_BUILD_ROOT
%endif

%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/SpiceClientGtk.{la,a}
# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/lib*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	-n spice-glib -p /sbin/ldconfig
%postun	-n spice-glib -p /sbin/ldconfig

%post	-n spice-gtk2 -p /sbin/ldconfig
%postun	-n spice-gtk2 -p /sbin/ldconfig

%if %{with gtk3}
%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/snappy
%attr(755,root,root) %{_bindir}/spicy
%attr(755,root,root) %{_bindir}/spicy-stats
%attr(755,root,root) %{_libdir}/libspice-client-gtk-3.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libspice-client-gtk-3.0.so.1
%{_libdir}/girepository-1.0/SpiceClientGtk-3.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libspice-client-gtk-3.0.so
%{_includedir}/spice-client-gtk-3.0
%{_pkgconfigdir}/spice-client-gtk-3.0.pc
%{_datadir}/gir-1.0/SpiceClientGtk-3.0.gir

%files static
%defattr(644,root,root,755)
%{_libdir}/libspice-client-gtk-3.0.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/spice-gtk
%endif

%files -n spice-glib
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libspice-client-glib-2.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libspice-client-glib-2.0.so.1
%attr(755,root,root) %{_libdir}/libspice-controller.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libspice-controller.so.0
%{_libdir}/girepository-1.0/SpiceClientGLib-2.0.typelib

%files -n spice-glib-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libspice-client-glib-2.0.so
%attr(755,root,root) %{_libdir}/libspice-controller.so
%{_includedir}/spice-client-glib-2.0
%{_includedir}/spice-controller
%{_pkgconfigdir}/spice-client-glib-2.0.pc
%{_pkgconfigdir}/spice-controller.pc
%{_datadir}/gir-1.0/SpiceClientGLib-2.0.gir

%files -n spice-glib-static
%defattr(644,root,root,755)
%{_libdir}/libspice-client-glib-2.0.a
%{_libdir}/libspice-controller.a

%if %{with usbredir}
%files -n spice-glib-usb
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/spice-client-glib-usb-acl-helper
%{_datadir}/polkit-1/actions/org.spice-space.lowlevelusbaccess.policy
%endif

%if %{with gtk2}
%files -n spice-gtk2
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libspice-client-gtk-2.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libspice-client-gtk-2.0.so.1
%{_libdir}/girepository-1.0/SpiceClientGtk-2.0.typelib

%files -n spice-gtk2-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libspice-client-gtk-2.0.so
%{_includedir}/spice-client-gtk-2.0
%{_pkgconfigdir}/spice-client-gtk-2.0.pc
%{_datadir}/gir-1.0/SpiceClientGtk-2.0.gir

%files -n spice-gtk2-static
%defattr(644,root,root,755)
%{_libdir}/libspice-client-gtk-2.0.a

%files -n python-spice-gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/SpiceClientGtk.so
%endif

%files -n vala-spice-protocol
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/spice-protocol.vapi
