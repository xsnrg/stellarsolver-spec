Name: stellarsolver
Version: 1.4.git
Release: %(date -u +%%Y%%m%%d%%H%%M%%S)%{?dist}
Summary: The Cross Platform Sextractor and Astrometry.net-Based Internal Astrometric Solver

License: LGPLv3

URL: https://github.com/rlancaste/stellarsolver
Source0: https://github.com/rlancaste/stellarsolver/archive/master.tar.gz

%global debug_package %{nil}
%define __find_requires %{nil}

Provides: stellarsolver.so(64-bit)
Provides: stellarsolver.so
Provides: stellarsolver.a

BuildRequires: cmake
BuildRequires: systemd

BuildRequires: pkgconfig(cfitsio)
BuildRequires: pkgconfig(gsl)
BuildRequires: pkgconfig(wcslib)


%description
An Astrometric Plate Solver for Mac, Linux, and Windows, built on Astrometry.net and SEP (sextractor)


%package devel
Summary: Libraries, includes, etc. used to develop an application with %{name}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: %{name}-static%{?_isa} = %{version}-%{release}

%description devel
These are the header files needed to develop a %{name} application

%package libs
Summary: %{name} shared libraries

%description libs
These are the shared libraries of %{name}.

%package static
Summary: Static libraries, includes, etc. used to develop an application with %{name}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description static
Static library needed to develop a %{name} application


%prep -v
%setup -n %{name}-master

%build

%cmake .
make VERBOSE=1 %{?_smp_mflags}

%install
find %buildroot -type f \( -name '*.so' -o -name '*.so.*' \) -exec chmod 755 {} +
make DESTDIR=%{buildroot} install

%files
%{_libdir}/*
%{_includedir}/libstellarsolver

%license LICENSE

%changelog
* Sun Oct 08 2020 Jim Howard <jh.xsnrg+fedora@gmail.com> 1.4.git
- introduction of spec file to build RPM packages from git
