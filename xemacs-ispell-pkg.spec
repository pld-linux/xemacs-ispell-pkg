Summary:	Interactive spelling corrector with GNU ispell
Summary(pl):	Interakcyiny korektor pisowni u¿ywaj±cy GNU ispell-a
Name:		xemacs-ispell-pkg
%define 	srcname	ispell
Version:	1.22
Release:	1
License:	GPL
Group:		Applications/Editors/Emacs
Group(de):	Applikationen/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
Source0:	ftp://ftp.xemacs.org/xemacs/packages/%{srcname}-%{version}-pkg.tar.gz
Patch0:		%{name}-info.patch
URL:		http://www.xemacs.org/
Buildrequires:	texinfo
BuildArch:	noarch
Conflicts:	xemacs-sumo
Requires:	xemacs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Interactive spelling corrector with GNU ispell.

%description -l pl 
Interakcyiny korektor pisowni u¿ywaj±cy GNU ispell-a.

%prep
%setup -q -c
%patch -p1

%build
makeinfo man/ispell/ispell.texi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/xemacs-packages,%{_infodir}}

cp -a * $RPM_BUILD_ROOT%{_datadir}/xemacs-packages
install ispell.info* $RPM_BUILD_ROOT%{_infodir}

gzip -9nf lisp/ispell/ChangeLog 

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1 

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc lisp/ispell/ChangeLog.gz 
%dir %{_datadir}/xemacs-packages/lisp/*
%{_datadir}/xemacs-packages/lisp/*/*.elc
%{_infodir}/*info*
