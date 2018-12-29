#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : greenlet
Version  : 0.4.15
Release  : 49
URL      : https://files.pythonhosted.org/packages/f8/e8/b30ae23b45f69aa3f024b46064c0ac8e5fcb4f22ace0dca8d6f9c8bbe5e7/greenlet-0.4.15.tar.gz
Source0  : https://files.pythonhosted.org/packages/f8/e8/b30ae23b45f69aa3f024b46064c0ac8e5fcb4f22ace0dca8d6f9c8bbe5e7/greenlet-0.4.15.tar.gz
Summary  : Lightweight in-process concurrent programming
Group    : Development/Tools
License  : MIT Python-2.0
Requires: greenlet-python3
Requires: greenlet-license
Requires: greenlet-python
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python3-dev
BuildRequires : tox
BuildRequires : virtualenv

%description
.. image:: https://secure.travis-ci.org/python-greenlet/greenlet.png
:target: http://travis-ci.org/python-greenlet/greenlet

%package dev
Summary: dev components for the greenlet package.
Group: Development
Provides: greenlet-devel

%description dev
dev components for the greenlet package.


%package license
Summary: license components for the greenlet package.
Group: Default

%description license
license components for the greenlet package.


%package python
Summary: python components for the greenlet package.
Group: Default
Requires: greenlet-python3

%description python
python components for the greenlet package.


%package python3
Summary: python3 components for the greenlet package.
Group: Default
Requires: python3-core

%description python3
python3 components for the greenlet package.


%prep
%setup -q -n greenlet-0.4.15

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1536423644
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.7/site-packages python3 setup.py test
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/greenlet
cp LICENSE %{buildroot}/usr/share/doc/greenlet/LICENSE
cp LICENSE.PSF %{buildroot}/usr/share/doc/greenlet/LICENSE.PSF
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/python3.7m/greenlet/greenlet.h

%files license
%defattr(-,root,root,-)
/usr/share/doc/greenlet/LICENSE
/usr/share/doc/greenlet/LICENSE.PSF

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
