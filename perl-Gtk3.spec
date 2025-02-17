#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : perl-Gtk3
Version  : 0.038
Release  : 24
URL      : https://cpan.metacpan.org/authors/id/X/XA/XAOC/Gtk3-0.038.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/X/XA/XAOC/Gtk3-0.038.tar.gz
Summary  : 'Perl interface to the 3.x series of the gtk+ toolkit'
Group    : Development/Tools
License  : LGPL-2.1
Requires: perl-Gtk3-license = %{version}-%{release}
Requires: perl-Gtk3-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : gtk3-dev
BuildRequires : perl(Cairo)
BuildRequires : perl(Cairo::GObject)
BuildRequires : perl(Glib)
BuildRequires : perl(Glib::Object::Introspection)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Gtk3
====
Perl bindings to the 3.x series of the gtk+ toolkit.  This module allows you to
write graphical user interfaces in a Perlish and object-oriented way, freeing
you from the casting and memory management in C, yet remaining very close in
spirit to original API.

%package dev
Summary: dev components for the perl-Gtk3 package.
Group: Development
Provides: perl-Gtk3-devel = %{version}-%{release}
Requires: perl-Gtk3 = %{version}-%{release}

%description dev
dev components for the perl-Gtk3 package.


%package license
Summary: license components for the perl-Gtk3 package.
Group: Default

%description license
license components for the perl-Gtk3 package.


%package perl
Summary: perl components for the perl-Gtk3 package.
Group: Default
Requires: perl-Gtk3 = %{version}-%{release}

%description perl
perl components for the perl-Gtk3 package.


%prep
%setup -q -n Gtk3-0.038
cd %{_builddir}/Gtk3-0.038

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Gtk3
cp %{_builddir}/Gtk3-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-Gtk3/9b07aad54a8e378c05f9c314cd48b32fdbf5f02d || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Gtk3.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Gtk3/9b07aad54a8e378c05f9c314cd48b32fdbf5f02d

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
