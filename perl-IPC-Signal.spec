%include	/usr/lib/rpm/macros.perl
%define	pdir	IPC
%define	pnam	Signal
Summary:	IPC::Signal perl module
Summary(pl):	Modu³ perla IPC::Signal
Name:		perl-IPC-Signal
Version:	1.00
Release:	9
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4cebf17fdf1785eaf8c151bf2e8c360a
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IPC::Signal module contains utility functions for dealing with signals.

%description -l pl
Modu³ IPC::Signal zawiera funkcje narzêdziowe do operowania na
sygna³ach.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/IPC/Signal.pm
%{_mandir}/man3/*
