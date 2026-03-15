Summary:	Interactive spelling corrector with ispell
Summary(pl.UTF-8):	Interakcyjny korektor pisowni używający ispella
Name:		xemacs-ispell-pkg
%define 	srcname	ispell
Version:	1.37
Release:	1
License:	GPL
Group:		Applications/Editors/Emacs
Source0:	http://ftp.xemacs.org/pub/xemacs/packages/%{srcname}-%{version}-pkg.tar.gz
# Source0-md5:	ba7b50154f988d73f58cf769b62f2f1e
Patch0:		%{name}-info.patch
URL:		https://www.xemacs.org/
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
%patch -P0 -p1

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
%doc %{_datadir}/xemacs-packages/lisp/ispell/ChangeLog
%doc %{_datadir}/xemacs-packages/info/ispell.info
%doc %{_datadir}/xemacs-packages/man/ispell
%doc %{_datadir}/xemacs-packages/pkginfo/MANIFEST.ispell
%dir %{_datadir}/xemacs-packages/lisp/*
%{_datadir}/xemacs-packages/lisp/*/*.el*
