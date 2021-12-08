"""
"""


from typing import Mapping


from .expressions import Expressions


class Symbol:
    """
    Symbol is the base class for Procedure, Callback, and PredefinedFunction. It holds
    access to the name and expressibility of the Symbol.
    """

    def __init__(self, name: str, apis: Mapping) -> None:
        self._name = name
        self._parseset = apis

    @property
    def name(self) -> str:
        """Get the Symbol name."""

        return self._name

    @property
    def express(self) -> Expressions:
        """Get expressions of this Symbol."""

        return Expressions(self._parseset, self.__class__.__name__.lower())
