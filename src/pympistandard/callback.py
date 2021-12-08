"""
"""


from typing import Mapping, Set


from .storage import PREDEFINED_FUNCTIONS
from .predefined_function import PredefinedFunction
from .expressions import Expressions
from .symbol import Symbol


class Callback(Symbol):
    """ """

    def has_proxy_render(self) -> bool:
        return self._parseset["attributes"]["proxy_render"]

    def has_embiggenment(self) -> bool:
        return any(
            parameter["kind"].startswith("POLY") for parameter in self._parseset["parameters"]
        ) or self._parseset["return_kind"].startswith("POLY")

    @property
    def predefined_functions(self) -> Set[PredefinedFunction]:
        """ """

        return set(predef for predef in PREDEFINED_FUNCTIONS if predef.callback == self)
