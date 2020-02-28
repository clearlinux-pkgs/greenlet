#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : greenlet
Version  : 0.4.15
Release  : 55
URL      : https://files.pythonhosted.org/packages/f8/e8/b30ae23b45f69aa3f024b46064c0ac8e5fcb4f22ace0dca8d6f9c8bbe5e7/greenlet-0.4.15.tar.gz
Source0  : https://files.pythonhosted.org/packages/f8/e8/b30ae23b45f69aa3f024b46064c0ac8e5fcb4f22ace0dca8d6f9c8bbe5e7/greenlet-0.4.15.tar.gz
Summary  : Lightweight in-process concurrent programming
Group    : Development/Tools
License  : MIT Python-2.0
Requires: greenlet-license = %{version}-%{release}
Requires: greenlet-python = %{version}-%{release}
Requires: greenlet-python3 = %{version}-%{release}
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

The greenlet package is a spin-off of Stackless, a version of CPython
that supports micro-threads called "tasklets". Tasklets run
pseudo-concurrently (typically in a single or a few OS-level threads)
and are synchronized with data exchanges on "channels".

A "greenlet", on the other hand, is a still more primitive notion of
micro-thread with no implicit scheduling; coroutines, in other
words. This is useful when you want to control exactly when your code
runs. You can build custom scheduled micro-threads on top of greenlet;
however, it seems that greenlets are useful on their own as a way to
make advanced control flow structures. For example, we can recreate
generators; the difference with Python's own generators is that our
generators can call nested functions and the nested functions can
yield values too. Additionally, you don't need a "yield" keyword. See
the example in tests/test_generator.py.

Greenlets are provided as a C extension module for the regular
unmodified interpreter.

Greenlets are lightweight coroutines for in-process concurrent
programming.

Who is using Greenlet?
======================

There are several libraries that use Greenlet as a more flexible
alternative to Python's built in coroutine support:

 - `Concurrence`_
 - `Eventlet`_
 - `Gevent`_

.. _Concurrence: http://opensource.hyves.org/concurrence/
.. _Eventlet: http://eventlet.net/
.. _Gevent: http://www.gevent.org/

Getting Greenlet
================

The easiest way to get Greenlet is to install it with pip or
easy_install::

  pip install greenlet
  easy_install greenlet


Source code archives and windows installers are available on the
python package index at https://pypi.python.org/pypi/greenlet

The source code repository is hosted on github:
https://github.com/python-greenlet/greenlet

Documentation is available on readthedocs.org:
https://greenlet.readthedocs.io

%package dev
Summary: dev components for the greenlet package.
Group: Development
Provides: greenlet-devel = %{version}-%{release}
Requires: greenlet = %{version}-%{release}
Requires: greenlet = %{version}-%{release}

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
Requires: greenlet-python3 = %{version}-%{release}

%description python
python components for the greenlet package.


%package python3
Summary: python3 components for the greenlet package.
Group: Default
Requires: python3-core
Provides: pypi(greenlet)

%description python3
python3 components for the greenlet package.


%prep
%setup -q -n greenlet-0.4.15
cd %{_builddir}/greenlet-0.4.15

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1582932319
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/greenlet
cp %{_builddir}/greenlet-0.4.15/LICENSE %{buildroot}/usr/share/package-licenses/greenlet/9562371a57ed564c4e61c368f355fa43cf665e2e
cp %{_builddir}/greenlet-0.4.15/LICENSE.PSF %{buildroot}/usr/share/package-licenses/greenlet/c0710216ad228c4f1738a3212542f827d6fec097
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/python3.8/greenlet/greenlet.h

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/greenlet/9562371a57ed564c4e61c368f355fa43cf665e2e
/usr/share/package-licenses/greenlet/c0710216ad228c4f1738a3212542f827d6fec097

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
