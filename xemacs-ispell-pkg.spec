Summary:	Interactive spelling corrector with ispell
Summary(pl):	Interakcyjny korektor pisowni u¿ywaj±cy ispella
Name:		xemacs-ispell-pkg
%define 	srcname	ispell
Version:	1.26
Release:	2
License:	GPL
Group:		Applications/Editors/Emacs
Source0:	ftp://ftp.xemacs.org/xemacs/packages/%{srcname}-%{version}-pkg.tar.gz
# Source0-md5:	85a9da0fe8ed41199388b5f41a0f7769
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

%description -l pl
Interakcyjny korektor pisowni u¿ywaj±cy ispella.

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
