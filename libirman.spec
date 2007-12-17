%define lib_name	%name

Name:		libirman
Version:	0.4.4
Release:	%mkrel 2
Summary:	Library for accessing the IRMAN hardware
License:	GPL
Group:		System/Libraries
URL:		http://www.evation.com/libirman/
Source0:	http://lirc.sourceforge.net/software/snapshots/%{name}-%{version}.tar.bz2

%description
General purpose library for programs to use in order to receive infra
red signals via irman compatible hardware. It is designed to be portable
across Unices but is so far only known to work under Linux.

%package -n %{lib_name}-devel
Summary:  Header files and static library for development with libirman
Group: Development/C
Provides: %{lib_name}-static-devel = %{version}-%{release}

%description -n %{lib_name}-devel
This package includes the static libraries and header
files for the libirman package.

%prep
%setup -q

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT

# Makefile doesn't create this:
install -d $RPM_BUILD_ROOT/%{_includedir}
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT/

%files
%defattr(-,root,root)
%doc COPYING COPYING.lib INSTALL NEWS README TECHNICAL TODO
%config(noreplace) %_sysconfdir/irman.conf
%{_bindir}/*

%files -n %{lib_name}-devel
%defattr(-,root,root)
%{_libdir}/*.a
%{_includedir}/*
