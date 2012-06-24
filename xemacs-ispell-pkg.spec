Summary:	Interactive spelling corrector with GNU ispell
Summary(pl):	Interakcyiny korektor pisowni u�ywaj�cy GNU ispell-a
Name:		xemacs-ispell-pkg
%define 	srcname	ispell
Version:	1.24
Release:	1
License:	GPL
Group:		Applications/Editors/Emacs
Group(cs):	Aplikace/Editory/Emacs
Group(da):	Programmer/Tekstbehandlere/Emacs
Group(de):	Applikationen/Editoren/Emacs
Group(es):	Aplicaciones/Editores/Emacs
Group(fr):	Applications/Editeurs/Emacs
Group(is):	Forrit/Ritlar/Emacs
Group(it):	Applicazioni/Editor/Emacs
Group(ja):	���ץꥱ�������/���ǥ���/Emacs
Group(no):	Applikasjoner/Editorer/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
Group(pt):	Aplica��es/Editores/Emacs
Group(ru):	����������/���������/Emacs
Group(sl):	Programi/Urejevalniki/Emacs
Group(sv):	Till�mpningar/Editorer/Emacs
Group(uk):	�������Φ ��������/���������/Emacs
Source0:	ftp://ftp.xemacs.org/xemacs/packages/%{srcname}-%{version}-pkg.tar.gz
Patch0:		%{name}-info.patch
Patch1:		%{name}-xml.patch
URL:		http://www.xemacs.org/
BuildArch:	noarch
Conflicts:	xemacs-sumo
BuildRequires:	xemacs
Requires:	xemacs
Requires:	ispell
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Interactive spelling corrector with GNU ispell.

%description -l pl 
Interakcyjny korektor pisowni u�ywaj�cy GNU ispell-a.

%prep
%setup -q -c
%patch0 -p1
%patch1 -p1

%build                                                      
xemacs -batch -q -no-site-file -f batch-byte-compile lisp/ispell/ispell.el

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
