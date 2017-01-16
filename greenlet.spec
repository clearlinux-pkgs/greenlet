#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : greenlet
Version  : 0.4.10
Release  : 26
URL      : http://pypi.debian.net/greenlet/greenlet-0.4.10.zip
Source0  : http://pypi.debian.net/greenlet/greenlet-0.4.10.zip
Summary  : Lightweight in-process concurrent programming
Group    : Development/Tools
License  : MIT Python-2.0
Requires: greenlet-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
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


%package python
Summary: python components for the greenlet package.
Group: Default

%description python
python components for the greenlet package.


%prep
%setup -q -n greenlet-0.4.10

%build
export LANG=C
export SOURCE_DATE_EPOCH=1484548604
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python2.7/site-packages python2 setup.py test
%install
export SOURCE_DATE_EPOCH=1484548604
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/python2.7/greenlet/greenlet.h
/usr/include/python3.6m/greenlet/greenlet.h

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
