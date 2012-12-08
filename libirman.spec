%define	major	0
%define libname 	%mklibname irman %major
%define develname	%mklibname irman -d

Name:		libirman
Version:	0.4.5
Release:	%mkrel 5
Summary:	Library for accessing the IRMAN hardware
License:	GPL
Group:		System/Libraries
URL:		http://sourceforge.net/projects/lirc/files/
Source0:	http://downloads.sourceforge.net/project/lirc/libirman/%{version}/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	%{libname} = %{version}-%{release}

%description
General purpose library for programs to use in order to receive infra
red signals via irman compatible hardware. It is designed to be portable
across Unices but is so far only known to work under Linux.

%package -n %{libname}
Group: System/Libraries
Summary: Library for accessing the IRMAN hardware

%description -n %{libname}
General purpose library for programs to use in order to receive infra
red signals via irman compatible hardware. It is designed to be portable
across Unices but is so far only known to work under Linux.

%package -n %{develname}
Summary:  Header files and development library for development with libirman
Group: Development/C
Requires: %{libname} = %{version}-%{release}
Provides: %{name}-devel = %{version}-%{release}
Provides: irman-devel = %{version}-%{release}
Obsoletes: libirman-devel < 0.4.5

%description -n %{develname}
This package includes the development libraries and header
files for the libirman package.

%prep
%setup -q

%build
%configure2_5x --disable-static
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT/

%files
%defattr(-,root,root)
%doc COPYING COPYING.lib NEWS README TECHNICAL TODO
%config(noreplace) %_sysconfdir/irman.conf
%{_bindir}/*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/*.so
%{_includedir}/*


%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 0.4.5-4mdv2011.0
+ Revision: 661478
- mass rebuild

* Sun Nov 28 2010 Oden Eriksson <oeriksson@mandriva.com> 0.4.5-3mdv2011.0
+ Revision: 602564
- rebuild

* Sun Apr 04 2010 Funda Wang <fwang@mandriva.org> 0.4.5-2mdv2010.1
+ Revision: 531330
- fix obsoletes

* Sun Apr 04 2010 Funda Wang <fwang@mandriva.org> 0.4.5-1mdv2010.1
+ Revision: 531151
- new version 0.4.5

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 0.4.4-6mdv2010.1
+ Revision: 520873
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.4.4-5mdv2010.0
+ Revision: 425573
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.4.4-4mdv2009.0
+ Revision: 222890
- rebuild

* Sun Jan 13 2008 Thierry Vignaud <tv@mandriva.org> 0.4.4-3mdv2008.1
+ Revision: 150698
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Aug 31 2007 Oden Eriksson <oeriksson@mandriva.com> 0.4.4-2mdv2008.0
+ Revision: 76771
- rebuild


* Fri Dec 29 2006 Frederic Crozat <fcrozat@mandriva.com> 0.4.4-1mdv2007.0
+ Revision: 102606
- Release 0.4.4
- Remove patch0, merged upstream
- Import libirman

* Sun Jan 01 2006 Mandriva Linux Team <http://www.mandrivaexpert.com/> 0.4.2-4mdk
- Rebuild

* Tue Aug 09 2005 Gwenole Beauchesne <gbeauchesne@mandriva.com> 0.4.2-3mdk
- gcc4 & provides fixes

* Sat Sep 11 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 0.4.2-2mdk
- Rebuild

