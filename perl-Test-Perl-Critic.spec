%define upstream_name    Test-Perl-Critic
%define upstream_version 1.02

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Use Perl::Critic in test programs
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

%if %{mdkversion} < 1010
BuildRequires:  perl-devel
%endif
BuildRequires:  perl(Perl::Critic)
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

%description 
Test::Perl::Critic wraps the Perl::Critic engine in a convenient subroutine
suitable for test programs written using the Test::More framework. This makes
it easy to integrate coding-standards enforcement into the build process. For
ultimate convenience (at the expense of some flexibility), see the criticism
pragma.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%check
%make test

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc INSTALL Changes LICENSE README
%{perl_vendorlib}/Test
%{_mandir}/*/*
