#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : kcrash
Version  : 5.82.0
Release  : 43
URL      : https://download.kde.org/stable/frameworks/5.82/kcrash-5.82.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.82/kcrash-5.82.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/5.82/kcrash-5.82.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : CC0-1.0 LGPL-2.0
Requires: kcrash-data = %{version}-%{release}
Requires: kcrash-lib = %{version}-%{release}
Requires: kcrash-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : kcoreaddons-dev
BuildRequires : kwindowsystem-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86vm-dev
BuildRequires : qtbase-dev
BuildRequires : qtbase-dev mesa-dev
BuildRequires : qtx11extras-dev

%description
# KCrash
Graceful handling of application crashes
## Introduction
KCrash provides support for intercepting and handling application crashes.

%package data
Summary: data components for the kcrash package.
Group: Data

%description data
data components for the kcrash package.


%package dev
Summary: dev components for the kcrash package.
Group: Development
Requires: kcrash-lib = %{version}-%{release}
Requires: kcrash-data = %{version}-%{release}
Provides: kcrash-devel = %{version}-%{release}
Requires: kcrash = %{version}-%{release}

%description dev
dev components for the kcrash package.


%package lib
Summary: lib components for the kcrash package.
Group: Libraries
Requires: kcrash-data = %{version}-%{release}
Requires: kcrash-license = %{version}-%{release}

%description lib
lib components for the kcrash package.


%package license
Summary: license components for the kcrash package.
Group: Default

%description license
license components for the kcrash package.


%prep
%setup -q -n kcrash-5.82.0
cd %{_builddir}/kcrash-5.82.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1623262393
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1623262393
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kcrash
cp %{_builddir}/kcrash-5.82.0/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kcrash/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
cp %{_builddir}/kcrash-5.82.0/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kcrash/20079e8f79713dce80ab09774505773c926afa2a
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories5/kcrash.categories
/usr/share/qlogging-categories5/kcrash.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/KCrash/KCrash
/usr/include/KF5/KCrash/kcrash.h
/usr/include/KF5/KCrash/kcrash_export.h
/usr/include/KF5/kcrash_version.h
/usr/lib64/cmake/KF5Crash/KF5CrashConfig.cmake
/usr/lib64/cmake/KF5Crash/KF5CrashConfigVersion.cmake
/usr/lib64/cmake/KF5Crash/KF5CrashTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5Crash/KF5CrashTargets.cmake
/usr/lib64/libKF5Crash.so
/usr/lib64/qt5/mkspecs/modules/qt_KCrash.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5Crash.so.5
/usr/lib64/libKF5Crash.so.5.82.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kcrash/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kcrash/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
