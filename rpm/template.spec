%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/rolling/.*$
%global __requires_exclude_from ^/opt/ros/rolling/.*$

Name:           ros-rolling-ament-cmake-pep257
Version:        0.12.3
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS ament_cmake_pep257 package

License:        Apache License 2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-rolling-ament-cmake-test
Requires:       ros-rolling-ament-pep257
Requires:       ros-rolling-ros-workspace
BuildRequires:  ros-rolling-ament-cmake-copyright
BuildRequires:  ros-rolling-ament-cmake-core
BuildRequires:  ros-rolling-ament-cmake-lint-cmake
BuildRequires:  ros-rolling-ament-cmake-test
BuildRequires:  ros-rolling-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
The CMake API for ament_pep257 to check code against the docstring style
conventions in PEP 257.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/rolling" \
    -DAMENT_PREFIX_PATH="/opt/ros/rolling" \
    -DCMAKE_PREFIX_PATH="/opt/ros/rolling" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/rolling

%changelog
* Fri Apr 08 2022 Michael Jeronimo <michael.jeronimo@openrobotics.org> - 0.12.3-1
- Autogenerated by Bloom

* Mon Mar 28 2022 Michael Jeronimo <michael.jeronimo@openrobotics.org> - 0.12.2-1
- Autogenerated by Bloom

* Tue Mar 01 2022 Michael Jeronimo <michael.jeronimo@openrobotics.org> - 0.12.1-1
- Autogenerated by Bloom

* Fri Feb 18 2022 Michael Jeronimo <michael.jeronimo@openrobotics.org> - 0.12.0-1
- Autogenerated by Bloom

* Tue Feb 08 2022 Michael Jeronimo <michael.jeronimo@openrobotics.org> - 0.11.4-2
- Autogenerated by Bloom

