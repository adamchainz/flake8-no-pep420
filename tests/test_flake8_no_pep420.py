from __future__ import annotations

import re
import sys
from textwrap import dedent

import pytest

if sys.version_info >= (3, 8):
    from importlib.metadata import version
else:
    from importlib_metadata import version


@pytest.fixture
def flake8_path(flake8_path):
    (flake8_path / "setup.cfg").write_text(
        dedent(
            """\
            [flake8]
            select = INP
            filename = *.py,*.pyi
            """
        )
    )
    yield flake8_path


def test_version(flake8_path):
    result = flake8_path.run_flake8(["--version"])
    version_regex = r"flake8-no-pep420:( )*" + version("flake8-no-pep420")
    unwrapped = "".join(result.out_lines)
    assert re.search(version_regex, unwrapped)


# INP001


def test_INP001_pass(flake8_path):
    (flake8_path / "dir").mkdir()
    (flake8_path / "dir" / "__init__.py").write_text("\n")
    (flake8_path / "dir" / "example.py").write_text("\n")
    result = flake8_path.run_flake8()
    assert result.out_lines == []


def test_INP001_pass_pyi(flake8_path):
    (flake8_path / "dir").mkdir()
    (flake8_path / "dir" / "__init__.pyi").write_text("\n")
    (flake8_path / "dir" / "example.pyi").write_text("\n")
    result = flake8_path.run_flake8()
    assert result.out_lines == []


def test_INP001_fail(flake8_path):
    (flake8_path / "dir").mkdir()
    (flake8_path / "dir" / "example.py").write_text("\n")
    result = flake8_path.run_flake8()
    msg = "INP001 File is part of an implicit namespace package. Add an __init__.py?"
    assert result.out_lines == [f"./dir/example.py:1:1: {msg}"]


def test_INP001_fail_pyi(flake8_path):
    (flake8_path / "dir").mkdir()
    (flake8_path / "dir" / "example.pyi").write_text("\n")
    result = flake8_path.run_flake8()
    msg = "INP001 File is part of an implicit namespace package. Add an __init__.pyi?"
    assert result.out_lines == [f"./dir/example.pyi:1:1: {msg}"]


def test_INP001_ignored(flake8_path):
    (flake8_path / "dir").mkdir()
    (flake8_path / "dir" / "example.py").write_text("import os  # noqa: INP001")
    result = flake8_path.run_flake8()
    assert result.out_lines == []


def test_INP001_per_file_ignores(flake8_path):
    (flake8_path / "setup.cfg").write_text(
        dedent(
            """\
            [flake8]
            select = INP
            per-file-ignores =
                dir/example.py:INP001
            """
        )
    )
    (flake8_path / "dir").mkdir()
    (flake8_path / "dir" / "example.py").write_text("import os")
    result = flake8_path.run_flake8()
    assert result.out_lines == []
