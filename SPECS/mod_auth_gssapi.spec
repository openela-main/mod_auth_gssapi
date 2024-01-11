Name:           mod_auth_gssapi
Version:        1.6.1
Release:        9%{?dist}
Summary:        A GSSAPI Authentication module for Apache

Group:          System Environment/Daemons
License:        MIT
URL:            https://github.com/modauthgssapi/mod_auth_gssapi
Source0:        https://github.com/modauthgssapi/%{name}/releases/download/v%{version}/%name-%{version}.tar.gz

Patch0: In-tests-show-the-exception-on-failure.patch
Patch1: Fix-tests-to-work-with-python3.patch
Patch2: tests-Test-suite-fixes-for-virtualenv-and-clang.patch
Patch3: Fix-integer-sizes-used-with-ap_set_flag_slot.patch
Patch4: Fix-mag_auth_basic-function-call.patch
Patch6: Fix-distcheck.patch
Patch7: Add-option-to-control-timeout-for-Basic-Auth.patch
Patch8: tests-Support-Debian-s-libfaketime.patch
Patch9: tests-Fixup-virtualenv-handling.patch
Patch10: tests-Don-t-override-the-specific-environment-by-the.patch
Patch11: Fix-PATH-handling-bug-in-test-suite.patch
Patch12: Move-to-python3-by-default.patch
Patch13: Fix-gss_localname-with-SPNEGO-wrapping.patch
Patch14: tests-add-test-for-gss_localname.patch
Patch15: Add-ability-to-expose-the-used-mechanism.patch
Patch16: Fix-gss-localname-test-to-work-with-older-gssapi-ver.patch

BuildRequires:  httpd-devel, krb5-devel, openssl-devel, autoconf, automake, libtool
BuildRequires:  gssntlmssp-devel
BuildRequires:  git
Requires:       httpd-mmn = %{_httpd_mmn}
Requires:       krb5-libs >= 1.11.5

%description
The mod_auth_gssapi module is an authentication service that implements the
SPNEGO based HTTP Authentication protocol defined in RFC4559.

%prep
%autosetup -S git

%build
export APXS=%{_httpd_apxs}
autoreconf -fi
%configure
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_httpd_moddir}
install -m 755 src/.libs/%{name}.so %{buildroot}%{_httpd_moddir}

# Apache configuration for the module
echo "LoadModule auth_gssapi_module modules/mod_auth_gssapi.so" > 10-auth_gssapi.conf
mkdir -p %{buildroot}%{_httpd_modconfdir}
install -m 644 10-auth_gssapi.conf %{buildroot}%{_httpd_modconfdir}

%files
%doc
%defattr(-,root,root)
%doc README COPYING
%config(noreplace) %{_httpd_modconfdir}/10-auth_gssapi.conf
%{_httpd_moddir}/mod_auth_gssapi.so

%changelog
* Thu Apr 28 2022 Francisco Trivino <ftrivino@redhat.com> 1.6.1-9
- Add missing repos to the osci tests
- Fix gss localname test to work with older gssapi version
- Resolves: #2083122
- Add ability to expose the used mechanism
- Resolves: #2046231

* Wed Apr 27 2022 Francisco Trivino <ftrivino@redhat.com> 1.6.1-8
- Add test for gss_localname
- Fix gss_localname with SPNEGO wrapping
- Resolves: #1787630

* Mon Oct 12 2020 Robbie Harwood <rharwood@redhat.com> 1.6.1-7.1
- Bang on gating until the environment gives up
- Resolves: #1866149

* Mon Oct 12 2020 Robbie Harwood <rharwood@redhat.com> - 1.6.1-7
- Backport basic auth timeout control
- Resolves: #1866149

* Fri Mar 22 2019 Robbie Harwood <rharwood@redhat.com> - 1.6.1-6
- Gating update
- Resolves: #1682259

* Mon Mar 18 2019 Robbie Harwood <rharwood@redhat.com> - 1.6.1-5
- Fix integer sizes used with ap_set_flag_slot()
- Resolves: #1674501

* Mon Mar 18 2019 Robbie Harwood <rharwood@redhat.com> - 1.6.1-4
- Fix virtualenv logic and add gating
- Resolves: #1682259

* Thu Mar 14 2019 Robbie Harwood <rharwood@redhat.com> - 1.6.1-3
- Fix tests to work with python3
- Resolves: #1661589

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 23 2018 Robbie Harwood <rharwood@redhat.com> - 1.6.1-1
- Release 1.6.1
- Resolves: #1570271

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Nov 06 2017 Robbie Harwood <rharwood@redhat.com> - 1.6.0-1
- Release 1.6.0

* Fri Oct 27 2017 Robbie Harwood <rharwood@redhat.com> - 1.5.1-6
- Document gssapi-no-negotiate

* Tue Oct 03 2017 Robbie Harwood <rharwood@redhat.com> - 1.5.1-5
- Handle extra large NSS entries
- Resolves: #1498175

* Mon Oct 02 2017 Robbie Harwood <rharwood@redhat.com> - 1.5.1-4
- Allow admins to selectively suppress negotiation
- Migrate to autosetup

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Mar  9 2017 Simo Sorce <simo@redhat.com> - 1.5.1-1
- Korabl-Sputnik 4 launch (1.5.1)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 16 2017 Simo Sorce <simo@redhat.com> - 1.5.0-1
- Last listoff of Space Shuttle Columbia release (1.5.0)

* Mon Nov 14 2016 Joe Orton <jorton@redhat.com> - 1.4.1-2
- rebuild for new OpenSSL

* Mon Aug 15 2016 Robbie Harwood <rharwood@redhat.com> 1.4.1-1
- Mishka & Chizhik fly on a rocket release (1.4.1)
- Fix bogus changelog date

* Fri Jun 17 2016 Simo Sorce <simo@redhat.com> 1.4.0-1
- Lunar Reconnaissance Orbiter (2009) release (1.4.0)

* Mon Feb 22 2016 Simo Sorce <simo@redhat.com> 1.3.2-1
- NEAR Shoemaker launch (1996) release (1.3.2)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Sep  3 2015 Simo Sorce <simo@redhat.com> 1.3.1-1
- Viking 2 landing (1976) release (1.3.1)

* Tue Jul  7 2015 Simo Sorce <simo@redhat.com> 1.3.0-2
- Fix annoying incorrect behavior with simple configuration where
  GssapiAllowedMech is not used.

* Sat Jul  4 2015 Simo Sorce <simo@redhat.com> 1.3.0-1
- US Independence Day Release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 21 2015 Simo Sorce <simo@redhat.com> 1.2.0-1
- New minor release 1.2.0
- Adds delegation support on Basic Auth
- Response fix, send last auth token on successful auth

* Tue Mar 31 2015 Simo Sorce <simo@redhat.com> 1.1.0-3
- Fix some authentication issues

* Thu Mar 26 2015 Simo Sorce <simo@redhat.com> 1.1.0-2
- Fix saving delegated credentials for SPNs

* Thu Mar 12 2015 Simo Sorce <simo@redhat.com> 1.1.0-1
- New minor release 1.1.0
- New feature: Basic Auth support
- Improvements: Better crypto for sesison cookies

* Sat Nov  8 2014 Simo Sorce <simo@redhat.com> 1.0.4-1
- Patch release 1.0.4
- logging initialization fixes
- additional build fixes

* Sat Oct 11 2014 Simo Sorce <simo@redhat.com> 1.0.3-1
- Patch release 1.0.3
- fixes some build issues on various distros

* Wed Aug 27 2014 Simo Sorce <simo@redhat.com> 1.0.2-1
- Adds documntation to README
- fixes bad bug that crippled configuration

* Thu Aug 14 2014 Simo Sorce <simo@redhat.com> 1.0.1-1
- Patch release 1.0.1

* Mon Aug  4 2014 Simo Sorce <simo@redhat.com> 1.0.0-1
- First release
