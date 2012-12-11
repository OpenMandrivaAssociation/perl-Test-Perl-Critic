%define upstream_name    Test-Perl-Critic
%define upstream_version 1.02

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Use Perl::Critic in test programs
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Perl::Critic)
BuildArch:	noarch

%description 
Test::Perl::Critic wraps the Perl::Critic engine in a convenient subroutine
suitable for test programs written using the Test::More framework. This makes
it easy to integrate coding-standards enforcement into the build process. For
ultimate convenience (at the expense of some flexibility), see the criticism
pragma.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%check
%make test

%files
%doc INSTALL Changes LICENSE README
%{perl_vendorlib}/Test
%{_mandir}/*/*

%changelog
* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 1.20.0-1mdv2010.1
+ Revision: 461032
- update to 1.02

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 1.10.0-1mdv2010.0
+ Revision: 405590
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.01-4mdv2009.0
+ Revision: 258576
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.01-3mdv2009.0
+ Revision: 246547
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.01-1mdv2008.1
+ Revision: 140721
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Mon Feb 12 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.01-1mdv2007.0
+ Revision: 120201
- new version

* Wed Nov 15 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.08-1mdv2007.1
+ Revision: 84368
- new release

* Thu Nov 09 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.07-1mdv2007.0
+ Revision: 79420
- Import perl-Test-Perl-Critic

* Sun Nov 05 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.07-1mdv2007.1
- first mdv release

