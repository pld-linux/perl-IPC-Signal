%include	/usr/lib/rpm/macros.perl
Summary:	IPC-Signal perl module
Summary(pl):	Modu³ perla IPC-Signal
Name:		perl-IPC-Signal
Version:	1.00
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/IPC/IPC-Signal-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
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
make

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/IPC/Signal
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README}.gz

%{perl_sitelib}/IPC/Signal.pm
%{perl_sitearch}/auto/IPC/Signal

%{_mandir}/man3/*
