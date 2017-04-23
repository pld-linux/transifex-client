#
# Conditional build:
%bcond_with	tests	# do not perform "make test"

%define		module		txclib
%define		egg_name	transifex_client
%define		pypi_name	transifex-client
Summary:	Command line tool for Transifex translation management
Name:		transifex-client
Version:	0.12.4
Release:	1
License:	GPL v2
Group:		Development/Tools
Source0:	https://files.pythonhosted.org/packages/source/t/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
# Source0-md5:	a4eefdf7d29198bc8363e087d26712d1
URL:		https://www.transifex.com/
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Transifex Command-line Client is a command line tool that enables
you to easily manage your translations within a project without the
need of an elaborate UI system.

%prep
%setup -q

%build
%py_build %{?with_tests:test}

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%attr(755,root,root) %{_bindir}/tx
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
