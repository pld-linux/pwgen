Summary: Password Generator
Name: pwgen
Version: 1.0
Release: 3
Source: pwgen-1.0.tar.gz
BuildRoot: /var/tmp/pwgen-1.0
Copyright: GPL
URL: http://kaputt.home.ml.org
Group: Utilities/System

%description
Password Generator is a password generator (surprise!).

%prep
%setup
rm -rf $RPM_BUILD_ROOT/*
mkdir -p $RPM_BUILD_ROOT/usr/{bin,man/man1}

%build
make CFLAGS="$RPM_OPT_FLAGS"

%install
make install \
BINDIR=$RPM_BUILD_ROOT/usr/bin \
MANDIR=$RPM_BUILD_ROOT/usr/man
gzip -9nf $RPM_BUILD_ROOT/usr/man/man1/pwgen.1

%clean
cd ..
rm -rf pwgen-1.0 $RPM_BUILD_ROOT/*

%files
%attr(644, root, root) %doc COPYING INSTALL README pgpkey.txt
%attr(644, root, root) /usr/man/man1/pwgen.1.gz
%attr(755, root, root) /usr/bin/pwgen
