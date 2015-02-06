%define upstream_name    Parser-MGC
%define upstream_version 0.08

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Build simple recursive-descent parsers
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module//%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(File::Slurp)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Module::Build::Compat)
BuildArch:	noarch

%description
This base class provides a low-level framework for building
recursive-descent parsers that consume a given input string from left to
right, returning a parse structure. It takes its name from the 'm//gc'
regexps used to implement the token parsing behaviour.

It provides a number of token-parsing methods, which each extract a
grammatical token from the string. It also provides wrapping methods that
can be used to build up a possibly-recursive grammar structure, by applying
a structure around other parts of parsing code. Each method, both token and
structural, atomically either consumes a prefix of the string and returns
its result, or fails and consumes nothing. This makes it simple to
implement grammars that require backtracking.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README LICENSE META.yml
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.80.0-2mdv2011.0
+ Revision: 657461
- rebuild for updated spec-helper

* Sat Mar 26 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.80.0-1
+ Revision: 648577
- update to new version 0.08

* Mon Mar 21 2011 Shlomi Fish <shlomif@mandriva.org> 0.70.0-1
+ Revision: 647438
- import perl-Parser-MGC

