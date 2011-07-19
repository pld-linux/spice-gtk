# TODO: build for gtk+3 or both? (spice-glib-*, spice-gtk-2-*, spice-gtk-3-* in such case?)
# NOTE: python requires gtk-2 version
Summary:	A GTK+ client and libraries for SPICE remote desktop servers
Summary(pl.UTF-8):	Klient i biblioteki GTK+ dla serwerów zdalnych pulpitów SPICE
Name:		spice-gtk
Version:	0.6
Release:	1
License:	LGPL v2.1+
Group:		X11/Applications
Source0:	http://spice-space.org/download/gtk/%{name}-%{version}.tar.bz2
# Source0-md5:	fe4b31a4e7b20ec53ff58d53957ab0b1
Patch0:		%{name}-sh.patch
Patch1:		%{name}-proto.patch
URL:		http://spice-space.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	cairo-devel >= 1.2.0
BuildRequires:	celt051-devel >= 0.5.1.1
BuildRequires:	cyrus-sasl-devel >= 2.0
BuildRequires:	gettext-devel >= 0.17
BuildRequires:	gobject-introspection-devel >= 0.9.4
BuildRequires:	glib2-devel >= 1:2.22
BuildRequires:	gtk-doc >= 1.14
BuildRequires:	gtk+2-devel >= 2:2.18.0
#BuildRequires:	gtk+3-devel >= 3.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libjpeg-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:2.0
BuildRequires:	openssl-devel
BuildRequires:	perl-Text-CSV
BuildRequires:	perl-base >= 1:5.8.1
BuildRequires:	pixman-devel >= 0.17.7
BuildRequires:	pkgconfig
BuildRequires:	pulseaudio-devel
BuildRequires:	python-devel >= 2.0
BuildRequires:	python-pygtk-devel >= 2:2.0.0
BuildRequires:	spice-protocol >= 0.6.3
BuildRequires:	xorg-lib-libXrandr-devel
BuildRequires:	zlib-devel
Requires:	celt051 >= 0.5.1.1
Requires:	glib2 >= 1:2.22
Requires:	pixman >= 0.17.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A GTK+ client and libraries for SPICE remote desktop servers.

%description -l pl.UTF-8
Klient i biblioteki GTK+ dla serwerów zdalnych pulpitów SPICE.

%package devel
Summary:	Header files for SPICE client libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek klienckich SPICE
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	celt051-devel >= 0.5.1.1
Requires:	glib2-devel >= 1:2.22
Requires:	openssl-devel
Requires:	pixman-devel >= 0.17.7
Requires:	spice-protocol >= 0.6.3

%description devel
Header files for SPICE client libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek klienckich SPICE.

%package static
Summary:	Static SPICE client libraries
Summary(pl.UTF-8):	Statyczne biblioteki klienckie SPICE
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static SPICE client libraries.

%description static -l pl.UTF-8
Statyczne biblioteki klienckie SPICE.

%package apidocs
Summary:	SPICE GTK API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki SPICE GTK
Group:		Documentation

%description apidocs
API documentation for SPICE GTK library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki SPICE GTK.

%package -n python-spice-gtk
Summary:	Python interface to SPICE client GTK library
Summary(pl.UTF-8):	Pythonowy interfejs do biblioteki klienckiej SPICE GTK
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description -n python-spice-gtk
Python interface to SPICE client GTK library.

%description -n python-spice-gtk -l pl.UTF-8
Pythonowy interfejs do biblioteki klienckiej SPICE GTK.

%package -n vala-spice-gtk
Summary:	Vala API for SPICE client GTK library
Summary(pl.UTF-8):	Interfejs języka Vala do biblioteki klienckiej SPICE GTK
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	vala >= 0.11.7

%description -n vala-spice-gtk
Vala API for SPICE client GTK library.

%description -n vala-spice-gtk -l pl.UTF-8
Interfejs języka Vala do biblioteki klienckiej SPICE GTK.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/SpiceClientGtk.{la,a}
# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/lib*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/snappy
%attr(755,root,root) %{_bindir}/spicy
%attr(755,root,root) %{_libdir}/libspice-client-glib-2.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libspice-client-glib-2.0.so.3
%attr(755,root,root) %{_libdir}/libspice-client-gtk-2.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libspice-client-gtk-2.0.so.1
%attr(755,root,root) %{_libdir}/libspice-controller.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libspice-controller.so.0
%{_libdir}/girepository-1.0/SpiceClientGLib-2.0.typelib
%{_libdir}/girepository-1.0/SpiceClientGtk-2.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libspice-client-glib-2.0.so
%attr(755,root,root) %{_libdir}/libspice-client-gtk-2.0.so
%attr(755,root,root) %{_libdir}/libspice-controller.so
%{_includedir}/spice-client-glib-2.0
%{_includedir}/spice-client-gtk-2.0
%{_includedir}/spice-controller
%{_pkgconfigdir}/spice-client-glib-2.0.pc
%{_pkgconfigdir}/spice-client-gtk-2.0.pc
%{_pkgconfigdir}/spice-controller.pc
%{_datadir}/gir-1.0/SpiceClientGLib-2.0.gir
%{_datadir}/gir-1.0/SpiceClientGtk-2.0.gir

%files static
%defattr(644,root,root,755)
%{_libdir}/libspice-client-glib-2.0.a
%{_libdir}/libspice-client-gtk-2.0.a
%{_libdir}/libspice-controller.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/spice-gtk

%files -n python-spice-gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/SpiceClientGtk.so

%files -n vala-spice-gtk
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/spice-protocol.vapi
