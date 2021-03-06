%{!?__python2: %global __python2 /usr/bin/python2}
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

Summary:       A plugin to sosreport to collect data about Eucalyptus clouds
Name:          eucalyptus-sos-plugins
Version:       0.1.7
Release:       0%{?build_id:.%build_id}%{?dist}
License:       GPLv2+
Group:         Applications/System
Url:           http://github.com/eucalyptus/eucalyptus-sosreport-plugins
BuildArch:     noarch

BuildRequires: python2-devel
BuildRequires: python-setuptools
Requires:      sos

Source0:       %{tarball_basedir}.tar.xz


%description
Eucalyptus is open source software for building AWS-compatible
private and hybrid clouds. Sosreport is a set of tools that
gathers information about system hardware and configuration.
This package contains plugins for sosreport to gather
information on Eucalyptus clouds.


%prep
%setup -q -n %{tarball_basedir}


%build
%{__python2} setup.py build


%install
%{__python2} setup.py install --skip-build --root $RPM_BUILD_ROOT
rm $RPM_BUILD_ROOT/%{python_sitelib}/sos/__init__.py*
rm $RPM_BUILD_ROOT/%{python_sitelib}/sos/plugins/__init__.py*


%files
%defattr(-,root,root,-)
%{python_sitelib}/sos/plugins/*
%{python_sitelib}/*.egg-info


%changelog
* Tue Mar 10 2015 Garrett Holmstrom <gholms@fedoraproject.org> - 0.1.7
- Removed __init__.py files that conflict with the sos package
- Macro-ized tarball names and release numbers for use with rel-eng build system

* Fri Feb 13 2015 Garrett Holmstrom <gholms@fedoraproject.org> - 0.1.7-1
- Revamped build process
- Switched to noarch
- Add *.egg-info to files list
