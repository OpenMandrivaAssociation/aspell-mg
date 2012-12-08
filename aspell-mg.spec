%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define src_ver 0.03-0
%define fname aspell5-%{languagecode}
%define aspell_ver 0.60
%define languageenglazy Malagasy
%define languagecode mg
%define lc_ctype mg_MG

Summary:       %{languageenglazy} files for aspell
Name:          aspell-%{languagecode}
Version:       0.03.0
Release:       %mkrel 10
Group:         System/Internationalization
Source:        http://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/%{fname}-%{src_ver}.tar.bz2
URL:		   http://aspell.net/
License:	   GPL
BuildRoot:     %{_tmppath}/%{name}-%{version}-root
Provides: spell-%{languagecode}

BuildRequires: aspell >= %{aspell_ver}
BuildRequires: make
Requires:      aspell >= %{aspell_ver}

# Mandriva stuff
Requires:      locales-%{languagecode}
# aspell = 1, myspell = 2, lang-specific = 3
Provides:      enchant-dictionary = 1
Provides:      aspell-dictionary
Provides:      aspell-%{lc_ctype}

Autoreqprov:   no

%description
A %{languageenglazy} dictionary for use with aspell, a spelling checker.

%prep
%setup -q -n %{fname}-%{src_ver}

%build
# don't use configure macro
./configure

%make

%install
rm -fr $RPM_BUILD_ROOT

%makeinstall_std

chmod 644 Copyright README* doc/*

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README* Copyright doc/*
%{_libdir}/aspell-%{aspell_ver}/*




%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 0.03.0-10mdv2011.0
+ Revision: 662847
- mass rebuild

* Tue Nov 30 2010 Oden Eriksson <oeriksson@mandriva.com> 0.03.0-9mdv2011.0
+ Revision: 603414
- rebuild

* Sun Mar 14 2010 Oden Eriksson <oeriksson@mandriva.com> 0.03.0-8mdv2010.1
+ Revision: 518940
- rebuild

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 0.03.0-7mdv2010.0
+ Revision: 413083
- rebuild

* Fri Mar 06 2009 Antoine Ginies <aginies@mandriva.com> 0.03.0-6mdv2009.1
+ Revision: 350057
- 2009.1 rebuild

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 0.03.0-5mdv2009.0
+ Revision: 220396
- rebuild

* Sun Mar 09 2008 Anssi Hannula <anssi@mandriva.org> 0.03.0-4mdv2008.1
+ Revision: 182483
- provide enchant-dictionary

* Fri Jan 11 2008 Thierry Vignaud <tv@mandriva.org> 0.03.0-3mdv2008.1
+ Revision: 148809
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Wed Feb 21 2007 Oden Eriksson <oeriksson@mandriva.com> 0.03.0-2mdv2007.0
+ Revision: 123295
- Import aspell-mg

* Wed Feb 21 2007 Oden Eriksson <oeriksson@mandriva.com> 0.03.0-2mdv2007.1
- use the mkrel macro
- disable debug packages

* Thu Jun 29 2006 Pablo Saratxaga <pablo@mandriva.com> 0.03.0-2mdv
- rebuild to require locales-mg now available

* Fri Dec 03 2004 Pablo Saratxaga <pablo@mandriva.com> 0.03.0-1mdk
- first version

