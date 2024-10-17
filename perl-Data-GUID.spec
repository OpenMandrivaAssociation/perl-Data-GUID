%define upstream_name    Data-GUID
%define upstream_version 0.048

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Globally unique identifiers
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Data/Data-GUID-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Data::UUID)
BuildRequires:	perl(Sub::Exporter)
BuildRequires:	perl(Sub::Install)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
Data::GUID provides a simple interface for generating and using globally
unique identifiers.

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
%doc Changes LICENSE META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 0.46.0-2mdv2011.0
+ Revision: 654298
- rebuild for updated spec-helper

* Sun Jan 30 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.46.0-1
+ Revision: 634223
- update to new version 0.046

* Sat Dec 25 2010 Shlomi Fish <shlomif@mandriva.org> 0.45.0-1mdv2011.0
+ Revision: 624769
- import perl-Data-GUID



