Summary:	Galago library
Summary(pl.UTF-8):	Biblioteka Galago
Name:		libgalago
Version:	0.5.2
Release:	2
License:	LGPL v2.1+
Group:		Applications/System
Source0:	http://www.galago-project.org/files/releases/source/libgalago/%{name}-%{version}.tar.bz2
# Source0-md5:	47f27f58dd8b0e46d9d2e037c51063ed
Patch0:		pkgconfig.patch
URL:		http://www.galago-project.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	dbus-devel >= 0.71
BuildRequires:	dbus-glib-devel >= 0.71
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-devel >= 0.18.1
BuildRequires:	glib2-devel >= 1:2.12.1
BuildRequires:	gtk-doc >= 1.7
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires:	dbus-glib >= 0.71
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libgalago is a part of Galago Project (D-BUS-based desktop presence
framework).

%description -l pl.UTF-8
libgalago jest częścią Projektu Galago (bazowany na D-BUSie szkielet
stanu obecności).

%package devel
Summary:	libgalago header files
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libgalago
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	dbus-glib-devel >= 0.71

%description devel
Header files for libgalago-based programs development.

%description devel -l pl.UTF-8
Pliki nagłówkowe do tworzenia programów opartych o libgalago.

%package static
Summary:	Static libgalago library
Summary(pl.UTF-8):	Statyczna biblioteka libgalago
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libgalago library.

%description static -l pl.UTF-8
Statyczna biblioteka libgalago.

%package apidocs
Summary:	libgalago API documentation
Summary(pl.UTF-8):	Dokumentacja API libgalago
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
libgalago API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API libgalago.

%prep
%setup -q
%patch0 -p1

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}

%configure \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_libdir}/galago

%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/autopackage
%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS
%attr(755,root,root) %{_libdir}/libgalago.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libgalago.so.3
%dir %{_libdir}/galago

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgalago.so
%{_pkgconfigdir}/libgalago.pc
%{_includedir}/libgalago

%files static
%defattr(644,root,root,755)
%{_libdir}/libgalago.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}
