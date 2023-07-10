from __future__ import annotations

import ast
import os
from importlib.metadata import version
from typing import Any
from typing import Generator


class NoPep420Checker:
    name = "flake8-no-pep420"
    version = version("flake8-no-pep420")

    def __init__(self, tree: ast.AST, filename: str) -> None:
        self._filename = filename

    def run(self) -> Generator[tuple[int, int, str, type[Any]], None, None]:
        dirname, basename = os.path.split(self._filename)

        if basename == "__init__.py":
            return

        ext = os.path.splitext(basename)[1] or ".py"
        init = f"__init__{ext}"
        init_name = os.path.join(dirname, init)
        if not os.path.exists(init_name):
            yield (
                1,
                0,
                (
                    "INP001 File is part of an implicit namespace package."
                    + f" Add an {init}?"
                ),
                type(self),
            )
