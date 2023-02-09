"""
"""


from typing import Mapping, Optional


from .storage import KINDS


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
    def kind(self) -> "Kind":
        """Get the Kind of the constant."""

        return KINDS[self._parseset["constant_kind"]]

    @property
    def is_opaque(self) -> bool:
        return "value" not in self._parseset and "queryable" not in self._parseset

    @property
    def value(self) -> Optional[str]:
        if "value" not in self._parseset:
            return None

        else:
            # TODO deal with equal_to
            # TODO deal with atleast
            raise NotImplementedError("atleast or equal_to not yet implemented")

    @property
    def queryable(self) -> None:
        # TODO ...
        raise NotImplementedError("queryable not implemented")
