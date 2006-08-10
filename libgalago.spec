Summary:	Galago library
Summary(pl):	Biblioteka Galago
Name:		libgalago
Version:	0.5.1
Release:	3
License:	LGPL v2.1+
Group:		Applications/System
Source0:	http://www.galago-project.org/files/releases/source/libgalago/%{name}-%{version}.tar.bz2
# Source0-md5:	9ace3f93505626773b852d2ebbc7d5d6
URL:		http://www.galago-project.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-glib-devel >= 0.71
BuildRequires:	glib2-devel >= 1:2.12.1
BuildRequires:	gtk-doc >= 1.7
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires:	dbus-glib >= 0.71
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libgalago is a part of Galago Project (D-BUS-based desktop presence
framework).

%description -l pl
libgalago jest cz�ci� Projektu Galago (bazowany na D-BUSie szkielet
stanu obecno�ci).

%package devel
Summary:	libgalago header files
Summary(pl):	Pliki nag��wkowe biblioteki libgalago
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	dbus-glib-devel >= 0.71

%description devel
Header files for libgalago-based programs development.

%description devel -l pl
Pliki nag��wkowe do tworzenia program�w opartych o libgalago.

%package static
Summary:	Static libgalago library
Summary(pl):	Statyczna biblioteka libgalago
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libgalago library.

%description static -l pl
Statyczna biblioteka libgalago.

%prep
%setup -q
%{__glib_gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%build

%configure \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_datadir}/autopackage

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_pkgconfigdir}/*
%{_includedir}/*
%{_gtkdocdir}/%{name}

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
