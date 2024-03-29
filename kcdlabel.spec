Summary:	KCDLabel - create covers, labels and booklets
Summary(pl.UTF-8):	KCDLabel - tworzenie okładek, etykiet i książeczek
Name:		kcdlabel
Version:	2.13
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://kcdlabel.sourceforge.net/download/%{name}-%{version}-KDE3.tar.gz
# Source0-md5:	a384147c5bdbe08f64356fe31eb12249
URL:		http://kcdlabel.sourceforge.net/
BuildRequires:	kdelibs-devel >= 3.1
BuildRequires:	qt-devel >= 6:3.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KCDLabel is a KDE program used to create covers, labels and booklets
for your CD cases.

%description -l pl.UTF-8
KCDLabel to program dla KDE służący do tworzenia okładek, etykiet i
książeczek do płyt CD.

%prep
%setup -q -n %{name}-%{version}-KDE3

%build
kde_appsdir="%{_desktopdir}"; export kde_appsdir
kde_htmldir="%{_htmldir}"; export kde_htmldir

# I'm not sure about this Category Utility

echo "Categories=Qt;KDE;Utility;">>kcdlabel/kcdlabel.desktop

mkdir linux
sed -e 's#slots\[CDROM_MAX_SLOTS\]#kde_slots\[CDROM_MAX_SLOTS\]#g' \
%{_includedir}/linux/cdrom.h > linux/cdrom.h

%configure \
        --disable-rpath

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# standardize paths ("medium" is 59x48 not 64x64 in fact...)
# XXX: check paths/kill unsupported icons
install -d $RPM_BUILD_ROOT%{_iconsdir}/locolor
mv -f $RPM_BUILD_ROOT%{_iconsdir}/small/locolor $RPM_BUILD_ROOT%{_iconsdir}/locolor/16x16
mv -f $RPM_BUILD_ROOT%{_iconsdir}/medium/locolor $RPM_BUILD_ROOT%{_iconsdir}/locolor/64x64
mv -f $RPM_BUILD_ROOT%{_desktopdir}/Multimedia/* $RPM_BUILD_ROOT%{_desktopdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog AUTHORS
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/kcdlabel.desktop
%{_iconsdir}/*/*/apps/*
