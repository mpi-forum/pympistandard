"""
"""


from typing import Mapping


class ConstantExpression:
    def __init__(self, parseset) -> None:
        self._parseset = parseset


class Constant:
    """
    Constant is the class which represents a defined global constantwithin the
    MPI Standard.
    """

    def __init__(self, name: str, parseset: Mapping) -> None:
        self._name = name
        self._parseset = parseset

    @property
    def name(self) -> str:
        """Get the Constant name."""

        return self._name

    @property
    def express(self) -> ConstantExpression:
        """Get expressions of this Constant."""

        return ConstantExpression(self._parseset)
