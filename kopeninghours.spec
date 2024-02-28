%define stable %([ "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

Summary:	OSM opening hours expression parser and evaluator
Name:		kopeninghours
Version:	24.02.0
Release:	1
Group:		Graphical desktop/KDE
License:	LGPLv2+
URL:		https://www.kde.org
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:  gettext
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	doxygen
BuildRequires:	boost-devel
BuildRequires:	cmake(KF5Holidays)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(Qt5Core) >= 5.14
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	pkgconfig(python)
BuildRequires:	qt5-assistant

%description
A library for parsing and evaluating OSM opening hours expressions.

%files -f %{name}.lang
%license LICENSES/*
%doc %{_docdir}/qt5/KOpeningHours.*
%{_datadir}/qlogging-categories5/org_kde_kopeninghours.*categories
%{_libdir}/qt5/qml/org/kde/kopeninghours

#------------------------------------------------------------------------------

%define major %(echo %{version} |cut -d. -f1)
%define libname %mklibname KOpeningHours %{major}

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

%package -n %{develname}
Summary:	Development files for %{name}
Group:		Development/KDE and Qt
Requires:	%{libname} = %{EVRD}

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

%description -n python-%{name}
Python bindings for %{name}.

%files -n python-%{name}
%{python_sitelib}/PyKOpeningHours

#------------------------------------------------------------------------------

%prep
%autosetup -p1
%cmake_kde5 -DBUILD_TESTING=OFF

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang %{name} --with-man
