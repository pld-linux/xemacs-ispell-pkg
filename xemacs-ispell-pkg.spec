Summary:	Interactive spelling corrector with ispell
Summary(pl.UTF-8):	Interakcyjny korektor pisowni używający ispella
Name:		xemacs-ispell-pkg
%define 	srcname	ispell
Version:	1.32
Release:	1
License:	GPL
Group:		Applications/Editors/Emacs
Source0:	http://ftp.xemacs.org/xemacs/packages/%{srcname}-%{version}-pkg.tar.gz
# Source0-md5:	0eceb13fd90b388f744f04bbf83fe4a1
Patch0:		%{name}-info.patch
Patch1:		%{name}-xml.patch
URL:		http://www.xemacs.org/
BuildRequires:	texinfo
BuildRequires:	xemacs
Requires:	ispell
Requires:	xemacs
Conflicts:	xemacs-sumo
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Interactive spelling corrector with ispell.

%description -l pl.UTF-8
Interakcyjny korektor pisowni używający ispella.

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

# remove .el file if corresponding .elc file exists
find $RPM_BUILD_ROOT -type f -name "*.el" | while read i; do test ! -f ${i}c || rm -f $i; done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc lisp/ispell/ChangeLog
%dir %{_datadir}/xemacs-packages/lisp/*
%{_datadir}/xemacs-packages/lisp/*/*.el*
