Summary:	Automatic Password Generator
Summary(pl):	Generator hase³
Name:		pwgen
Version:	1.0
Release:	4
License:	GPL
Group:		Applications/System
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pwgen generates random, meaningless but pronounceable passwords.

%description -l pl
Program pwgen s³u¿y do generowania losowych hase³.

%prep
%setup -q

%build
%{__make} CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{%{_bindir},%{_mandir}/man1}

%{__make} install \
	BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}

gzip -9nf README pgpkey.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/pwgen
%{_mandir}/man1/pwgen.1*
