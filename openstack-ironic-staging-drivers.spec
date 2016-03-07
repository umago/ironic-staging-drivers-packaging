%global orig_name ironic-staging-drivers
%global module ironic_staging_drivers

Name:       openstack-%{orig_name}
Version:    0.1.0
Release:    1
Summary:    Staging drivers for OpenStack Ironic
License:    ASL 2.0
URL:        http://launchpad.net/%{orig_name}/

Source0:    https://pypi.python.org/packages/source/i/%{orig_name}/%{orig_name}-%{version}.tar.gz

BuildArch:  noarch

BuildRequires:  python2-devel
BuildRequires:  python-pbr
BuildRequires:  python-setuptools
BuildRequires:  git

Requires:   python-oslo-i18n
Requires:   python-oslo-utils

%description
The Ironic Staging Drivers is used to hold out-of-tree Ironic drivers
which doesn't have means to provide a 3rd Party CI at this point in
time which is required by Ironic.

%prep
%setup -q -n %{orig_name}-%{version}
# Remove bundled egg-info
rm -rf %{orig_name}.egg-info
# Let RPM handle the dependencies
rm -f {test-,}requirements.txt

%build
%py2_build

%install
%py2_install

%files -n openstack-%{orig_name}
%license LICENSE
%{python2_sitelib}/%{module}
%{python2_sitelib}/%{module}-*.egg-info
%exclude %{python2_sitelib}/%{module}/tests

%changelog
* Mon Mar 7 2016 Lucas Alvares Gomes <lucasagomes@gmail.com> 0.1.0-1
– Initial Packaging
