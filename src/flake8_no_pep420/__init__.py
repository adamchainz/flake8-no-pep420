import ast
import sys
from pathlib import Path
from typing import Any, Generator, Tuple, Type

if sys.version_info >= (3, 8):
    from importlib.metadata import version
else:
    from importlib_metadata import version


class NoPep420Checker:
    name = "flake8-no-pep420"
    version = version("flake8-no-pep420")

    def __init__(self, tree: ast.AST, filename: str) -> None:
        self._path = Path(filename)

    def run(self) -> Generator[Tuple[int, int, str, Type[Any]], None, None]:
        if self._path.name == "__init__.py":
            return

        if not (self._path.parent / "__init__.py").exists():
            yield (
                1,
                0,
                "INP001 File is part of an implicit namespace package.",
                type(self),
            )
