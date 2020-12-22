import re
import sys
import textwrap

import pytest

if sys.version_info >= (3, 8):
    from importlib.metadata import version
else:
    from importlib_metadata import version


@pytest.fixture
def flake8dir(flake8dir):
    flake8dir.make_setup_cfg(
        textwrap.dedent(
            """\
            [flake8]
            select = INP
            """
        )
    )
    yield flake8dir


def test_version(flake8dir):
    result = flake8dir.run_flake8(["--version"])
    version_regex = r"flake8-no-pep420:( )*" + version("flake8-no-pep420")
    unwrapped = "".join(result.out_lines)
    assert re.search(version_regex, unwrapped)


# INP001


def test_INP001_pass(flake8dir):
    flake8dir.make_file("dir/__init__.py", "")
    flake8dir.make_file("dir/example.py", "")
    result = flake8dir.run_flake8()
    assert result.out_lines == []


def test_INP001_fail_empty(flake8dir):
    flake8dir.make_file("dir/example.py", "")
    result = flake8dir.run_flake8()
    assert result.out_lines == [
        "./dir/example.py:1:1: INP001 File is part of an implicit namespace package."
    ]


def test_INP001_fail_nonempty(flake8dir):
    flake8dir.make_file("dir/example.py", "print('hi')")
    result = flake8dir.run_flake8()
    assert result.out_lines == [
        "./dir/example.py:1:1: INP001 File is part of an implicit namespace package."
    ]


def test_INP001_fail_shebang(flake8dir):
    flake8dir.make_file(
        "dir/example.py",
        """
        #!/bin/env/python
        print('hi')
        """,
    )
    result = flake8dir.run_flake8()
    assert result.out_lines == [
        "./dir/example.py:2:1: INP001 File is part of an implicit namespace package."
    ]


def test_INP001_ignored(flake8dir):
    flake8dir.make_file("dir/__init__.py", "")
    flake8dir.make_file("dir/example.py", "import os  # noqa: INP001")
    result = flake8dir.run_flake8()
    assert result.out_lines == []
