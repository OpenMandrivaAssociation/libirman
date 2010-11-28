%define	major	0
%define libname 	%mklibname irman %major
%define develname	%mklibname irman -d

Name:		libirman
Version:	0.4.5
Release:	%mkrel 3
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
%{_libdir}/*.la
%{_libdir}/*.so
%{_includedir}/*
