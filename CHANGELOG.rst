=========
Changelog
=========

2.9.0 (2025-09-09)
------------------

* Support Python 3.14.

2.8.0 (2024-10-27)
------------------

* Drop Python 3.8 support.

* Support Python 3.13.

2.7.0 (2023-07-10)
------------------

* Drop Python 3.7 support.

2.6.0 (2023-06-15)
------------------

* Support Python 3.12.

2.5.0 (2023-06-15)
------------------

* Empty release, made by mistake.

2.4.0 (2023-04-27)
------------------

* Support ``.pyi`` files.

2.3.0 (2022-05-11)
------------------

* Support Python 3.11.

2.2.0 (2022-01-26)
------------------

* Extend message with “Add an ``__init__.py``?” to hint how to fix the issue.

2.1.0 (2022-01-10)
------------------

* Drop Python 3.6 support.

2.0.0 (2021-11-17)
------------------

* Remove the “first logical line” behaviour, which is fragile.
  Flake8’s ``per-file-ignores`` option provides an alternative for files with shebangs.
  The README provides more detail.

* Remove upper bound on Flake8 version.

1.2.0 (2021-10-11)
------------------

* Support Flake8 4.

1.1.1 (2021-08-17)
------------------

* Avoid checking the AST to determine the error line number.

1.1.0 (2021-05-10)
------------------

* Support Python 3.10.

* Stop distributing tests to reduce package size. Tests are not intended to be
  run outside of the tox setup in the repository. Repackagers can use GitHub's
  tarballs per tag.

1.0.1 (2020-12-22)
------------------

* Report ``INP001`` on the first logical line (skipping over comments/shebang).

1.0.0 (2020-12-19)
------------------

* Initial release.
