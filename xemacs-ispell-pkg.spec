Summary:	Interactive spelling corrector with GNU ispell
Summary(pl):	Interakcyiny korektor pisowni u¿ywaj±cy GNU ispell-a
Name:		xemacs-ispell-pkg
%define 	srcname	ispell
Version:	1.22
Release:	2
License:	GPL
Group:		Applications/Editors/Emacs
Group(de):	Applikationen/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
Source0:	ftp://ftp.xemacs.org/xemacs/packages/%{srcname}-%{version}-pkg.tar.gz
Patch0:		%{name}-info.patch
URL:		http://www.xemacs.org/
BuildArch:	noarch
Conflicts:	xemacs-sumo
Requires:	xemacs
Requires:	ispell
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Interactive spelling corrector with GNU ispell.

%description -l pl 
Interakcyiny korektor pisowni u¿ywaj±cy GNU ispell-a.

%prep
%setup -q -c
%patch -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/xemacs-packages,%{_infodir}}

cp -a * $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

gzip -9nf lisp/ispell/ChangeLog 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc lisp/ispell/ChangeLog.gz 
%dir %{_datadir}/xemacs-packages/lisp/*
%{_datadir}/xemacs-packages/lisp/*/*.elc
