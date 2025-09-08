================
flake8-no-pep420
================

.. image:: https://img.shields.io/github/actions/workflow/status/adamchainz/flake8-no-pep420/main.yml.svg?branch=main&style=for-the-badge
   :target: https://github.com/adamchainz/flake8-no-pep420/actions?workflow=CI

.. image:: https://img.shields.io/pypi/v/flake8-no-pep420.svg?style=for-the-badge
   :target: https://pypi.org/project/flake8-no-pep420/

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg?style=for-the-badge
   :target: https://github.com/psf/black

.. image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white&style=for-the-badge
   :target: https://github.com/pre-commit/pre-commit
   :alt: pre-commit

A `flake8 <https://flake8.readthedocs.io/en/latest/>`_ plugin to ban `PEP-420 <https://www.python.org/dev/peps/pep-0420/>`__ implicit namespace packages.

----

**Linting a Django project?**
Check out my book `Boost Your Django DX <https://adamchainz.gumroad.com/l/byddx>`__ which covers Flake8 and many other code quality tools.

----

Requirements
============

Python 3.9 to 3.14 supported.

Installation
============

First, install with ``pip``:

.. code-block:: sh

     python -m pip install flake8-no-pep420

Second, if you define Flake8’s ``select`` setting, add the ``INP`` prefix to it.
Otherwise, the plugin should be active by default.

Rationale
=========

Implicit namespace packages are directories of Python files without an ``__init__.py``.
They’re valid and importable, but they break some tools:

* unittest test discovery, unless |-s (--start-directory)|__ points to the namespace package.
  By extension, this affects Django’s test runner too.

  .. |-s (--start-directory)| replace:: ``-s`` (``--start-directory``)
  __ https://docs.python.org/3/library/unittest.html#cmdoption-unittest-discover-s

* Coverage.py, unless |report.include_namespace_packages|__ is enabled.

  .. |report.include_namespace_packages| replace:: ``report.include_namespace_packages``
  __ https://coverage.readthedocs.io/en/latest/config.html#report-include-namespace-packages

* pytest (`Issue #5147 <https://github.com/pytest-dev/pytest/issues/5147>`__)

In most cases, tools fail silently, which can lead to a false sense of security:

* Tests may look legitimate but never run
* Code may be untested but not appear in coverage statistics

PEP-420’s algorithm is non-trivial which is probably why such tools haven’t (yet) implemented it.

Rules
=====

INP001: File is part of an implicit namespace package. Add __init__.py?
-----------------------------------------------------------------------

flake8-no-pep420 will trigger this on the first line of any file that sits in a directory without an ``__init__.py`` file.

Often projects have a few root files *not* in packages, for which an ``__init__.py`` file should not be added.
For example, Django projects normally have a ``manage.py`` file in the root of their repository.
In these cases you can ignore the ``INP001`` error.
It’s possible to use ``# noqa: INP001`` to ignore the error in-line, but this isn’t possible if the first line is a `shebang <https://en.wikipedia.org/wiki/Shebang_(Unix)>`__, such as in Django’s ``manage.py``.
In such cases it’s preferable to use Flake8’s `per-file-ignores option <https://flake8.pycqa.org/en/latest/user/options.html#cmdoption-flake8-per-file-ignores>`__, for example in ``setup.cfg``:

.. code-block:: ini

    [flake8]
    # ...
    per-file-ignores =
        manage.py:INP001
