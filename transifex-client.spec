%define		module		txclib
%define		egg_name	transifex_client
%define		pypi_name	transifex-client
Summary:	Command line tool for Transifex translation management
Name:		transifex-client
Version:	0.10
Release:	0.1
License:	GPL v2
Group:		Development/Languages
Source0:	http://pypi.python.org/packages/source/t/transifex-client/%{name}-%{version}.tar.gz
# Source0-md5:	5549538d84b8eede6b254cd81ae024fa
URL:		http://transifex.org
Patch1:		%{name}-resource-creation.patch
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-backports-ssl_match_hostname
Requires:	python-setuptools
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Transifex Command-line Client is a command line tool that enables
you to easily manage your translations within a project without the
need of an elaborate UI system.

%prep
%setup -q
%patch1 -p1

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%attr(755,root,root) %{_bindir}/tx
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
