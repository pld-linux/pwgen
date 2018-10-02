Summary:	Automatic Password Generator
Summary(pl.UTF-8):	Generator haseł
Name:		pwgen
Version:	2.08
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://vorboss.dl.sourceforge.net/project/pwgen/pwgen/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	6cfba450ac6ff72d11e88a6b0b049165
URL:		http://sourceforge.net/projects/pwgen/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pwgen generates random, meaningless but pronounceable passwords.

%description -l pl.UTF-8
Program pwgen służy do generowania losowych haseł.

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
%doc debian/changelog
%attr(755,root,root) %{_bindir}/pwgen
%{_mandir}/man1/pwgen.1*
