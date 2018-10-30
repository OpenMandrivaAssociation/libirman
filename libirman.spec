%define	major	0
%define libname	%mklibname irman %{major}
%define devname	%mklibname irman -d

Summary:	Library for accessing the IRMAN hardware
Name:		libirman
Version:	0.4.5
Release:	14
License:	GPLv2
Group:		System/Libraries
Url:		http://sourceforge.net/projects/lirc/files/
Source0:	http://downloads.sourceforge.net/project/lirc/libirman/%{version}/%{name}-%{version}.tar.bz2

%description
General purpose library for programs to use in order to receive infra
red signals via irman compatible hardware. It is designed to be portable
across Unices but is so far only known to work under Linux.

%package -n %{libname}
Group:		System/Libraries
Summary:	Library for accessing the IRMAN hardware

%description -n %{libname}
This package contains a shared library for %{name}.

%package -n %{devname}
Summary:	Header files and development library for development with libirman
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	irman-devel = %{version}-%{release}

%description -n %{devname}
This package includes the development libraries and header
files for the libirman package.

%prep
%setup -q

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std

%files
%doc COPYING COPYING.lib NEWS README TECHNICAL TODO
%config(noreplace) %{_sysconfdir}/irman.conf
%{_bindir}/*

%files -n %{libname}
%{_libdir}/libirman.so.%{major}*

%files -n %{devname}
%{_libdir}/*.so
%{_includedir}/*

