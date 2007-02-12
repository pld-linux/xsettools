Summary:	Tools for X Window settings
Summary(pl.UTF-8):   Narzędzia do ustawień X Window
Name:		xsettools
Version:	0.22
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://free.of.pl/a/adgor/%{name}-%{version}.tar.gz
# Source0-md5:	48dbc2920bffba079533aa710103a8ec
Requires:	XFree86
Requires:	dml
Requires:	grep
Requires:	sed
Requires:	textutils
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
A set of scripts to X Window settings manipulation and a script that can
receive settings while Window Manager starts.

%description -l pl.UTF-8
Zestaw skryptów do manipulowania ustawieniami środowiska X Window oraz
skrypt umożliwiający odtworzenie ustawień podczas startu Window
Managera.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir}}

install dpmsset mouseset rootset ssaverset xsetrcv $RPM_BUILD_ROOT%{_bindir}
install *.desktop .directory $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGELOG TODO
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop
