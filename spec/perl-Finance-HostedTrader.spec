Name:           perl-Finance-HostedTrader
Version:        0.017
Release:        1%{?dist}
Summary:        Finance::HostedTrader Perl module
License:        MIT
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Finance-HostedTrader/
Source0:        http://www.cpan.org/modules/by-module/Finance/Finance-HostedTrader-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(Config::Any)
BuildRequires:  perl(Date::Calc)
BuildRequires:  perl(Date::Manip)
BuildRequires:  perl(DBI)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Finance::FXCM::Simple)
BuildRequires:  perl(Hash::Merge)
BuildRequires:  perl(HTML::Table)
BuildRequires:  perl(List::Compare::Functional)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Log::Log4perl)
BuildRequires:  perl(Math::Round)
BuildRequires:  perl(MIME::Lite)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(MooseX::Log::Log4perl)
BuildRequires:  perl(Params::Validate)
BuildRequires:  perl(Parse::RecDescent)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::ASCIITable)
BuildRequires:  perl(YAML::Tiny)
Requires:       perl(Config::Any)
Requires:       perl(Date::Calc)
Requires:       perl(Date::Manip)
Requires:       perl(DBI)
Requires:       perl(Finance::FXCM::Simple)
Requires:       perl(Hash::Merge)
Requires:       perl(HTML::Table)
Requires:       perl(List::Compare::Functional)
Requires:       perl(List::Util)
Requires:       perl(Log::Log4perl)
Requires:       perl(Math::Round)
Requires:       perl(MIME::Lite)
Requires:       perl(Moose)
Requires:       perl(Moose::Util::TypeConstraints)
Requires:       perl(MooseX::Log::Log4perl)
Requires:       perl(Params::Validate)
Requires:       perl(Parse::RecDescent)
Requires:       perl(Scalar::Util)
Requires:       perl(Test::Differences)
Requires:       perl(Test::More)
Requires:       perl(Text::ASCIITable)
Requires:       perl(YAML::Tiny)
BuildRequires:  libmysqludf_ta >= 0.1-3
Requires:       libmysqludf_ta >= 0.1-3
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Finance::HostedTrader Perl module

%prep
%setup -q -n Finance-HostedTrader-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
#Don't run the tests here because the environment is not setup
#dzil already runs them before cutting a release anyway
#make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes dist.ini howtos LICENSE README weaver.ini
%{perl_vendorlib}/*
%{_mandir}/man3/*
%{_mandir}/man1/*
/usr/bin/fx-all-tables.pl
/usr/bin/fx-build-synthetics.pl
/usr/bin/fx-create-db-schema.pl
/usr/bin/fx-data-up-2-date.pl
/usr/bin/fx-download-fxcm.pl
/usr/bin/fx-eval.pl
/usr/bin/fx-report.pl
/usr/bin/fx-score.pl
/usr/bin/fx-show-config.pl
/usr/bin/fx-test-data.pl
/usr/bin/fx-test-signal.pl
/usr/bin/fx-trader.pl
/usr/bin/fx-update-tf.pl


%changelog
* Tue Feb 26 2013 João Costa <joaocosta@zonalivre.org> 0.017-1
- New upstream version available
* Thu Dec 27 2012 João Costa <joaocosta@zonalivre.org> 0.016-1
- New upstream version available
* Tue Dec 16 2012 João Costa <joaocosta@zonalivre.org> 0.015-1
- New upstream version available

* Tue Dec 09 2012 João Costa <joaocosta@zonalivre.org> 0.014-1
- New upstream version available

* Tue Dec 04 2012 João Costa <joaocosta@zonalivre.org> 0.013-1
- New upstream version available

* Sat Nov 30 2012 João Costa <joaocosta@zonalivre.org> 0.011-1
- New upstream version available

* Sat Nov 24 2012 João Costa <joaocosta@zonalivre.org> 0.010-1
- New upstream version available

* Fri Nov 23 2012 João Costa <joaocosta@zonalivre.org> 0.009-2
- Add dependency on libmysqludf_ta

* Wed Nov 21 2012 João Costa <joaocosta@zonalivre.org> 0.009-1
- Specfile autogenerated by cpanspec 1.78.