#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : kcrash
Version  : 5.52.0
Release  : 10
URL      : https://download.kde.org/stable/frameworks/5.52/kcrash-5.52.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.52/kcrash-5.52.0.tar.xz
Source99 : https://download.kde.org/stable/frameworks/5.52/kcrash-5.52.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: kcrash-data = %{version}-%{release}
Requires: kcrash-lib = %{version}-%{release}
Requires: kcrash-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : kcoreaddons-dev
BuildRequires : kwindowsystem-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86misc-dev libXxf86vm-dev
BuildRequires : qtbase-dev mesa-dev

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
%setup -q -n kcrash-5.52.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1542739653
mkdir -p clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags} VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1542739653
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kcrash
cp COPYING.LIB %{buildroot}/usr/share/package-licenses/kcrash/COPYING.LIB
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/xdg/kcrash.categories

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
/usr/lib64/libKF5Crash.so.5.52.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kcrash/COPYING.LIB
