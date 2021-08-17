import ast
import sys
from pathlib import Path
from typing import Any, Generator, List, Tuple, Type

if sys.version_info >= (3, 8):
    from importlib.metadata import version
else:
    from importlib_metadata import version


class NoPep420Checker:
    name = "flake8-no-pep420"
    version = version("flake8-no-pep420")

    def __init__(self, tree: ast.AST, lines: List[str], filename: str) -> None:
        self._lines = lines
        self._path = Path(filename)

    def run(self) -> Generator[Tuple[int, int, str, Type[Any]], None, None]:
        if self._path.name == "__init__.py":
            return

        if not (self._path.parent / "__init__.py").exists():
            if len(self._lines) > 0 and self._lines[0].startswith("#!"):
                lineno = 2
            else:
                lineno = 1
            yield (
                lineno,
                0,
                "INP001 File is part of an implicit namespace package.",
                type(self),
            )
