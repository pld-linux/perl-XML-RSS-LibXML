#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	XML
%define	pnam	RSS-LibXML
Summary:	XML::RSS::LibXML - XML::RSS with XML::LibXML
Summary(pl.UTF-8):	XML::RSS::LibXML - XML::RSS z XML::LibXML
Name:		perl-XML-RSS-LibXML
Version:	0.30_02
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/D/DM/DMAKI/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	5fcf799fea80268817a268d14519459f
URL:		http://search.cpan.org/dist/XML-RSS-LibXML/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Class-Accessor
BuildRequires:	perl-DateTime-Format-Mail
BuildRequires:	perl-DateTime-Format-W3CDTF
BuildRequires:	perl-UNIVERSAL-require
BuildRequires:	perl-XML-LibXML
BuildRequires:	perl-XML-LibXML-XPathContext
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML::RSS::LibXML uses XML::LibXML (libxml2) for parsing RSS instead of
XML::RSS' XML::Parser (expat), while trying to keep interface
compatibility with XML::RSS.

XML::RSS is an extremely handy tool, but it is unfortunately not
exactly the most lean or efficient RSS parser, especially in a
long-running process. So for a long time I had been using my own
version of RSS parser to get the maximum speed and efficiency - this
is the re-packaged version of that module, such that it adheres to the
XML::RSS interface.

Use this module when you have severe performance requirements working
with RSS files.

%description -l pl.UTF-8
XML::RSS::LibXML do przetwarzania RSS wykorzystuje XML::LibXML
(libxml2) zamiast używanego przez XML::RSS XML::Parser (expat),
próbując zachować interfejs kompatybilny z XML::RSS.

XML::RSS to bardzo podręczne narzędzie, ale niestety nie jest
najlżejszym ani najbardziej wydajnym analizatorem RSS, zwłaszcza przy
długo działających procesach. Natomiast ten pakiet zawiera
przepakowaną wersję własnego analizatora RSS używanego od dawna przez
autora.

Tego modułu można używać jeśli mamy ostre wymagania co do wydajności
przy pracy z plikami RSS.

%prep
%setup -q -n %{pdir}-%{pnam}-0.30

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/XML/RSS/*.pm
%{perl_vendorlib}/XML/RSS/LibXML
%{_mandir}/man3/*
