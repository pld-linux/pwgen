Summary:	Automatic Password Generator
Summary(pl):	Generator hase³
Name:		pwgen
Version:	1.0
Release:	4
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
License:	GPL
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System

%description
pwgen generates random, meaningless but pronounceable passwords.

%description -l pl
Program pwgen s³u¿y do generowania losowych hasel.

%prep
%setup -q

%build
%{__make} CFLAGS="%{?debug:-O -g}%{!?debug:$RPM_OPT_FLAGS}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{%{_bindir},%{_mandir}/man1}

%{__make} install \
BINDIR=$RPM_BUILD_ROOT%{_bindir} \
MANDIR=$RPM_BUILD_ROOT%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING INSTALL README pgpkey.txt

%attr(755, root, root) %{_bindir}/pwgen
%attr(644, root, root) %{_mandir}/man1/pwgen.1*
