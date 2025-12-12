#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e 's,/,-,g')
%define stable %([ "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

Summary:	OSM opening hours expression parser and evaluator
Name:		kopeninghours
Version:	25.08.3
Release:	%{?git:0.%{git}.}2
Group:		Graphical desktop/KDE
License:	LGPLv2+
URL:		https://www.kde.org
%if 0%{?git:1}
Source0:	https://invent.kde.org/libraries/kopeninghours/-/archive/%{gitbranch}/kopeninghours-%{gitbranchd}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/kopeninghours-%{version}.tar.xz
%endif
BuildRequires:	cmake(ECM)
BuildRequires:	gettext
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	doxygen
BuildRequires:	boost-devel
BuildRequires:	cmake(KF6Holidays)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	pkgconfig(python)
BuildRequires:	qt6-qttools-assistant

BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON
BuildOption:	-DBUILD_TESTING:BOOL=OFF
BuildOption:	-DQT_MAJOR_VERSION=6

# Renamed after 6.0 2025-05-09
%rename plasma6-kopeninghours

%description
A library for parsing and evaluating OSM opening hours expressions.

%files -f kopeninghours.lang
%license LICENSES/*
%{_datadir}/qlogging-categories6/org_kde_kopeninghours.*categories
%{_libdir}/qt6/qml/org/kde/kopeninghours

#------------------------------------------------------------------------------

%define major %(echo %{version} |cut -d. -f1)
%define libname %mklibname KOpeningHours

%package -n %{libname}
Summary:	OSM opening hours expression parser and evaluator
Group:		System/Libraries
Requires:	%{name} >= %{EVRD}

%description -n %{libname}
A library for parsing and evaluating OSM opening hours expressions.

%files -n %{libname}
%license LICENSES/*
%{_libdir}/libKOpeningHours.so.%{major}*
%{_libdir}/libKOpeningHours.so.1

#------------------------------------------------------------------------------
%define develname %mklibname %{name} -d
# Renamed after 6.0 2025-07-18
%define olddevelname %mklibname plasma6-%{name} -d

%package -n %{develname}
Summary:	Development files for %{name}
Group:		Development/KDE and Qt
Requires:	%{libname} = %{EVRD}
%rename %{olddevelname}

%description -n %{develname}
Include files and libraries needed to build programs that use the KOpeningHours
library.

%files -n %{develname}
%license LICENSES/*
%{_includedir}/KOpeningHours
%{_includedir}/kopeninghours
%{_includedir}/*.h
%{_libdir}/cmake/KOpeningHours
%{_libdir}/libKOpeningHours.so

#------------------------------------------------------------------------------

%package -n python-%{name}
Summary:	Python3 bindings for %{name}
Group:		Development/Python
# Renamed after 6.0 2025-05-09
%rename python-plasma6-kopeninghours

%description -n python-%{name}
Python bindings for %{name}.

%files -n python-%{name}
%{python_sitelib}/PyKOpeningHours
