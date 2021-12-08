"""
"""

from typing import Mapping


from .expressions import Expressions
from .storage import CALLBACKS
from .symbol import Symbol


class PredefinedFunction(Symbol):
    """ """

    def __repr__(self) -> str:
        return f"<{hex(id(self))} {self._name}>"

    def has_embiggenment(self) -> bool:
        """"""

        return any(
            parameter["kind"].startswith("POLY") for parameter in self._parseset["parameters"]
        ) or self._parseset["return_kind"].startswith("POLY")

    @property
    def callback(self) -> "Callback":
        """Access the Callback object which this PredefinedFunction implements."""

        return CALLBACKS[self._parseset["attributes"]["predefined_function"]]

