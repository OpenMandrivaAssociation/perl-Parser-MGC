%define upstream_name    Parser-MGC
%define upstream_version 0.23
Name:		perl-%{upstream_name}
Version:	0.23
Release:	4

Summary:	Build simple recursive-descent parsers
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Parser-MGC
Source0:	https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Parser-MGC-0.23.tar.gz

BuildRequires:	make
BuildRequires:	perl(Feature::Compat::Try)
BuildRequires:	perl(Module::Build)
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
%setup -q -n Parser-MGC-0.23

%build
perl Build.PL --installdirs=vendor
./Build

%check
./Build test || :

%make test || :

%install
./Build install --destdir=%{buildroot} --create_packlist=0

%files
%doc Changes META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

