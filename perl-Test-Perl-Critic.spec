%define module  Test-Perl-Critic
%define name    perl-%{module}
%define version 1.01
%define release %mkrel 3

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Use Perl::Critic in test programs
License:        GPL or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Test/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:  perl-devel
%endif
BuildRequires:  perl(Perl::Critic)
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description 
Test::Perl::Critic wraps the Perl::Critic engine in a convenient subroutine
suitable for test programs written using the Test::More framework. This makes
it easy to integrate coding-standards enforcement into the build process. For
ultimate convenience (at the expense of some flexibility), see the criticism
pragma.

%prep
%setup -q -n %{module}-%{version}

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


