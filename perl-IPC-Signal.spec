#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	IPC
%define		pnam	Signal
Summary:	IPC::Signal perl module
Summary(pl.UTF-8):	Moduł perla IPC::Signal
Name:		perl-IPC-Signal
Version:	1.00
Release:	11
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4cebf17fdf1785eaf8c151bf2e8c360a
URL:		http://search.cpan.org/dist/IPC-Signal/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IPC::Signal module contains utility functions for dealing with
signals.

%description -l pl.UTF-8
Moduł IPC::Signal zawiera funkcje narzędziowe do operowania na
sygnałach.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/IPC/Signal.pm
%{_mandir}/man3/*
