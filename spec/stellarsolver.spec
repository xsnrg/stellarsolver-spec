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


%prep -v
%setup

%build

# Disable LTO
%define _lto_cflags %{nil}

%cmake .
%cmake_build

%install
#find %buildroot -type f \( -name '*.so' -o -name '*.so.*' \) -exec chmod 755 {} +
%cmake_install
%ldconfig_scriptlets libs

%files
%{_libdir}/*
%{_includedir}/*

%license LICENSE

%changelog
* Thu Oct 08 2020 Jim Howard <jh.xsnrg+fedora@gmail.com> 1.4.git
- introduction of spec file to build RPM packages from git
