Name: hunspell-mr
Summary: Marathi hunspell dictionaries
Version: 20060920 
Release: 15%{?dist}
Source: http://downloads.sourceforge.net/project/openofficeorg.mirror/contrib/dictionaries/mr_IN.zip
Patch0: hunspell-mr-get-rid-of-broken-line.patch 
Group: Applications/Text
URL: http://wiki.services.openoffice.org/wiki/Dictionaries
License: LGPLv2+
BuildArch: noarch

Requires: hunspell

%description
Marathi hunspell dictionaries.

%prep
%setup -q -c -n mr-IN
%patch0 -p1

# Remove ^M and trailing whitespace characters
sed -i 's/\r//;s/[ \t]*$//' mr_IN.dic

%build
#nothing to do here

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p mr_IN.dic mr_IN.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

%files
%doc README_mr_IN.txt LICENCE
%{_datadir}/myspell/*

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 20060920-15
- Mass rebuild 2013-12-27

* Tue May 28 2013 Parag Nemade <pnemade AT redhat DOT com> - 20060920-14
- Removed BR:dos2unix and instead use sed (rh# 967639)

* Tue May 28 2013 Parag Nemade <pnemade AT redhat DOT com> - 20060920-13
- Resolves:rh# 967639: mr_IN.dic contains both CRLF and LF line terminators

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20060920-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Aug 23 2012 Parag Nemade <pnemade AT redhat.com> - 20060920-11
- Resolves:rh#848846:-Source URL not working

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20060920-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Parag <pnemade AT redhat DOT com> - 20060920-9
- spec cleanup

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20060920-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20060920-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Feb 18 2010 Parag <pnemade AT redhat.com> - 20060920-6
- Resolves: rh#566395:- Improvements to get rid of the broken line

* Mon Jan 11 2010 Parag <pnemade AT redhat.com> - 20060920-5
- Change Source URL to new mirror.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20060920-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Jun 28 2009 Caolán McNamara <caolanm@redhat.com> - 20060920-3
- bring wordlist encoding issue fix from F-11 into devel

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20060920-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jan 03 2008 Parag <pnemade@redhat.com> - 20060920-1
- Initial Fedora release
