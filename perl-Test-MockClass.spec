#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Test
%define	pnam	MockClass
Summary:	Test::MockClass - A module to provide mock classes and mock objects for testing
Summary(pl.UTF-8):	Test::MockClass - moduł udostępniający klasy pozorne i obiekty pozorne do testowania
Name:		perl-Test-MockClass
Version:	1.05
Release:	0.1
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	6b458a9458e535e92feb9df3df834ce7
URL:		http://search.cpan.org/dist/Test-MockClass/
BuildRequires:	perl-ExtUtils-AutoInstall >= 0.45
BuildRequires:	perl-Test-SimpleUnit >= 1.21
BuildRequires:	perl-Tie-Watch >= 1.1
BuildRequires:	perl-Hook-WrapSub
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a simple interface for creating mock classes and
mock objects with mock methods for mock purposes, I mean testing
purposes. It also provides a simple mechanism for tracking the
interactions to the mocked objects. I originally wrote this class to
help me test object factory methods, since then, I've added some more
features. This module is hopefully going to be the Date::Manip of
mock class/object creation, so email me with lots of ideas, everything
but the kitchen sink will go in!

%description -l pl.UTF-8
Ten moduł dostarcza prosty interfejs do tworzenia klas pozornych oraz
obiektów pozornych z metodami pozornymi do celów pozornych, to znaczy
do celów testowych. Dostarcza także prosty mechanizm do śledzenia
interakcji upozorowanych obiektów. Oryginalnie klasa ta została
napisana do pomocy przy testowaniu metod tworzących obiekty, ale od
tamtego czasu przybyło jej więcej możliwości. Ten moduł ma być
Date::Manip dla tworzenia klas/obiektów pozornych, więc autor zachęca
do wysyłania wielu pomysłów, co mogłoby się w nim znaleźć.

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
%doc README
%{perl_vendorlib}/Test/*.pm
%{perl_vendorlib}/Test/MockClass
%{_mandir}/man3/*
