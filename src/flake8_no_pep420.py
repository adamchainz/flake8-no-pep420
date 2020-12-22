import sys
from pathlib import Path

if sys.version_info >= (3, 8):
    from importlib.metadata import version
else:
    from importlib_metadata import version


class NoPep420Checker:
    name = "flake8-no-pep420"
    version = version("flake8-no-pep420")

    def __init__(self, tree, filename):
        self._tree = tree
        self._path = Path(filename)

    def run(self):
        if not (self._path.parent / "__init__.py").exists():
            if self._tree.body:
                lineno = self._tree.body[0].lineno
            else:
                lineno = 1
            yield (
                lineno,
                0,
                "INP001 File is part of an implicit namespace package.",
                type(self),
            )
