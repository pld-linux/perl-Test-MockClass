#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Test
%define	pnam	MockClass
Summary:	Test::MockClass - A module to provide mock classes and mock objects for testing
Summary(pl):	Test::MockClass - modu� udost�pniaj�cy klasy pozorne i obiekty pozorne do testowania
Name:		perl-Test-MockClass
Version:	1.04
Release:	0.1
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	821b94ea86e0c704723fe9bbdf180f57
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

%description -l pl
Ten modu� dostarcza prosty interfejs do tworzenia klas pozornych oraz
obiekt�w pozornych z metodami pozornymi do cel�w pozornych, to znaczy
do cel�w testowych. Dostarcza tak�e prosty mechanizm do �ledzenia
interakcji upozorowanych obiekt�w. Oryginalnie klasa ta zosta�a
napisana do pomocy przy testowaniu metod tworz�cych obiekty, ale od
tamtego czasu przyby�o jej wi�cej mo�liwo�ci. Ten modu� ma by�
Date::Manip dla tworzenia klas/obiekt�w pozornych, wi�c autor zach�ca
do wysy�ania wielu pomys��w, co mog�oby si� w nim znale��.

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
