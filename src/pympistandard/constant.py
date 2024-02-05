"""
"""


from typing import Mapping, Optional, Tuple, TYPE_CHECKING

if TYPE_CHECKING:
    from .kind import Kind


from .storage import KINDS
from .version import Version


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

    @property
    def introduced(self) -> Version:
        # TODO
        raise NotImplementedError("Versions are not yet annotated in the Standard")

    @property
    def deprecated(self) -> Optional[Version]:
        # TODO
        # None is not deprecated
        # otherwise version

        raise NotImplementedError("constants don't have deprecation annotated")

    @property
    def removed(self) -> Optional[Version]:
        # TODO
        # None is not removed, otherwise version
        raise NotImplementedError("constants don't have removal annotated")
