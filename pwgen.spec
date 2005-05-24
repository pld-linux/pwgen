Summary:	Automatic Password Generator
Summary(pl):	Generator hase³
Name:		pwgen
Version:	2.03
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/pwgen/%{name}-%{version}.tar.gz
# Source0-md5:	1a73657a0a10f3c3d00933036369e702
URL:		http://sourceforge.net/projects/pwgen/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pwgen generates random, meaningless but pronounceable passwords.

%description -l pl
Program pwgen s³u¿y do generowania losowych hase³.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/pwgen
%{_mandir}/man1/pwgen.1*
