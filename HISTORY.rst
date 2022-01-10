=======
History
=======

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
