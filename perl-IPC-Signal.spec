%include	/usr/lib/rpm/macros.perl
Summary:	IPC-Signal perl module
Summary(pl):	Modu³ perla IPC-Signal
Name:		perl-IPC-Signal
Version:	1.00
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/IPC/IPC-Signal-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IPC-Signal module contains utility functions for dealing with signals.

%description -l pl
Modu³ IPC-Signal zawiera funkcje narzêdziowe do operowania na
sygna³ach.

%prep
%setup -q -n IPC-Signal-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/IPC/Signal.pm
%{_mandir}/man3/*
