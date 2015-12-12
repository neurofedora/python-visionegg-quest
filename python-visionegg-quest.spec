%global modname visionegg-quest
%global srcname Quest

Name:           python-%{modname}
Version:        1.1
Release:        1%{?dist}
Summary:        QUEST algorithm for finding threshold

License:        BSD
URL:            http://visionegg.readthedocs.org/en/latest/Quest.html
Source0:        http://downloads.sourceforge.net/visionegg/%{srcname}-%{version}.tar.gz
Patch0:         0001-Fix-tab-mixing.patch
Patch1:         0002-py3-print_function.patch
Patch2:         0003-py3-raw_input.patch
Patch3:         0004-rename-to-visionegg-quest.patch
Patch4:         0005-remove-bool-constants-hack.patch

BuildArch:      noarch

%description
%{summary}.

%package -n python2-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{modname}}
BuildRequires:  python2-devel
%if 0%{?fedora} > 23
Requires:       python2-numpy
%else
Requires:       numpy
%endif

%description -n python2-%{modname}
%{summary}.

Python 2 version.

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel
Requires:       python3-numpy

%description -n python3-%{modname}
%{summary}.

Python 3 version.

%prep
%autosetup -n %{srcname}-%{version} -p1

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

%files -n python2-%{modname}
%{python2_sitelib}/visionegg_quest-*.egg-info
%{python2_sitelib}/%{srcname}.py*

%files -n python3-%{modname}
%{python3_sitelib}/visionegg_quest-*.egg-info
%{python3_sitelib}/%{srcname}.py
%{python3_sitelib}/__pycache__/%{srcname}.*

%changelog
* Sat Dec 12 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.1-1
- Initial package
