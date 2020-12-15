#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : codecov
Version  : 2.1.9
Release  : 23
URL      : https://files.pythonhosted.org/packages/68/27/28aaa27789fec468684132e18222f3e58013b18473de1e6d776aff1662a2/codecov-2.1.9.tar.gz
Source0  : https://files.pythonhosted.org/packages/68/27/28aaa27789fec468684132e18222f3e58013b18473de1e6d776aff1662a2/codecov-2.1.9.tar.gz
Summary  : Hosted coverage reports for GitHub, Bitbucket and Gitlab
Group    : Development/Tools
License  : Apache-2.0
Requires: codecov-bin = %{version}-%{release}
Requires: codecov-license = %{version}-%{release}
Requires: codecov-python = %{version}-%{release}
Requires: codecov-python3 = %{version}-%{release}
Requires: coverage
Requires: requests
BuildRequires : buildreq-distutils3
BuildRequires : coverage
BuildRequires : requests

%description
Codecov Global Python Uploader
[![codecov.io](https://codecov.io/github/codecov/codecov-python/coverage.svg?branch=master)](https://codecov.io/github/codecov/codecov-python)
![PyPI](https://img.shields.io/pypi/v/codecov)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
=======
| [Support][1] | [Documentation][2] | [Community Boards][3] | [Twitter][4] |
| ------------ | ------------------ | --------------------- | ------------ |

%package bin
Summary: bin components for the codecov package.
Group: Binaries
Requires: codecov-license = %{version}-%{release}

%description bin
bin components for the codecov package.


%package license
Summary: license components for the codecov package.
Group: Default

%description license
license components for the codecov package.


%package python
Summary: python components for the codecov package.
Group: Default
Requires: codecov-python3 = %{version}-%{release}

%description python
python components for the codecov package.


%package python3
Summary: python3 components for the codecov package.
Group: Default
Requires: python3-core
Provides: pypi(codecov)
Requires: pypi(coverage)
Requires: pypi(requests)

%description python3
python3 components for the codecov package.


%prep
%setup -q -n codecov-2.1.9
cd %{_builddir}/codecov-2.1.9

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1598281102
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/codecov
cp %{_builddir}/codecov-2.1.9/LICENSE %{buildroot}/usr/share/package-licenses/codecov/061f495252a8a118c79bd9ace27758087c69f9d8
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/codecov

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/codecov/061f495252a8a118c79bd9ace27758087c69f9d8

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
