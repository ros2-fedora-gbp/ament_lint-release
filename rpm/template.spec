%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/rolling/.*$
%global __requires_exclude_from ^/opt/ros/rolling/.*$

Name:           ros-rolling-ament-pclint
Version:        0.13.2
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS ament_pclint package

License:        Apache License 2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-rolling-ros-workspace
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  ros-rolling-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  ros-rolling-ament-copyright
BuildRequires:  ros-rolling-ament-flake8
BuildRequires:  ros-rolling-ament-pep257
%endif

%description
The ability to perform static code analysis on C/C++ code using PC-lint and
generate xUnit test result files.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%py3_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%py3_install -- --prefix "/opt/ros/rolling"

%if 0%{?with_tests}
%check
# Look for a directory with a name indicating that it contains tests
TEST_TARGET=$(ls -d * | grep -m1 "\(test\|tests\)" ||:)
if [ -n "$TEST_TARGET" ] && %__python3 -m pytest --version; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%__python3 -m pytest $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/rolling

%changelog
* Tue Sep 13 2022 Michael Jeronimo <michael.jeronimo@openrobotics.org> - 0.13.2-1
- Autogenerated by Bloom

* Mon May 09 2022 Michael Jeronimo <michael.jeronimo@openrobotics.org> - 0.13.1-1
- Autogenerated by Bloom

* Fri Apr 29 2022 Michael Jeronimo <michael.jeronimo@openrobotics.org> - 0.13.0-1
- Autogenerated by Bloom

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

