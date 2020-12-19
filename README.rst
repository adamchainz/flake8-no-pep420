================
flake8-no-pep420
================

.. image:: https://img.shields.io/github/workflow/status/adamchainz/flake8-no-pep420/CI/master?style=for-the-badge
   :target: https://github.com/adamchainz/flake8-no-pep420/actions?workflow=CI

.. image:: https://img.shields.io/pypi/v/flake8-no-pep420.svg?style=for-the-badge
   :target: https://pypi.org/project/flake8-no-pep420/

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg?style=for-the-badge
   :target: https://github.com/psf/black

.. image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white&style=for-the-badge
   :target: https://github.com/pre-commit/pre-commit
   :alt: pre-commit

A `flake8 <https://flake8.readthedocs.io/en/latest/index.html>`_ plugin to ban `PEP-420 <https://www.python.org/dev/peps/pep-0420/>`__ implicit namespace packages.

Requirements
============

Python 3.6 to 3.9 supported.

Installation
============

First, install with ``pip``:

.. code-block:: sh

     python -m pip install flake8-no-pep420

Second, check that ``flake8`` lists the plugin in its version line:

.. code-block:: sh

    $ flake8 --version
    3.8.4 (flake8-no-pep420: 1.0.0, mccabe: 0.6.1, pycodestyle: 2.5.0, pyflakes: 2.1.1) CPython 3.8.0 on Darwin

Third, add the ``INP`` prefix to your `select list <https://flake8.pycqa.org/en/latest/user/options.html#cmdoption-flake8-select>`__.
For example, if you have your configuration in ``setup.cfg``:

.. code-block:: ini

    [flake8]
    select = E,F,W,INP

----

**Linting a Django project?**
Check out my book `Speed Up Your Django Tests <https://gumroad.com/l/suydt>`__ which covers loads of best practices so you can write faster, more accurate tests.

----

Rationale
=========

Implicit namespace packages are folders of Python files without an ``__init__.py``.
They’re valid and importable, but unfortunately they’re not discovered by many code quality tools:

* `coverage.py <https://github.com/nedbat/coveragepy/issues/1024>`__
* Django’s test runner
* mypy without its `--namespace-packages option <https://mypy.readthedocs.io/en/latest/command_line.html#import-discovery>`__

Such silent failure leads to a false sense of security.
PEP-420’s algorithm is non-trivial which is probably why such tools haven’t (yet) implemented it.

Rules
=====

INP001: File is part of an implicit namespace package.
------------------------------------------------------

flake8-no-pep420 will trigger this on the first line of any file that sits in a folder without a `__init__.py` file.

Often projects have a few root files not in packages, for which an ``__init__.py`` file should not be added.
For example on a Django project there’s the ``manage.py`` file.
In these cases you should add ``# noqa: INP001`` on the first line of the file.
