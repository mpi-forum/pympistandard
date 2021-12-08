"""
"""


from typing import Mapping
from enum import Enum


from .kind import Kind
from .storage import KINDS


class Direction(Enum):
    """The Direction enumeration is used to declare the semantic direction of a parameter."""

    IN = "IN"
    OUT = "OUT"
    INOUT = "INOUT"
    # NOTE is there one missing according to discuss with DanH?
    #      about MPI_Status
    #           in = use, no modify
    #           out = modify, no use
    #           inout = use and modify (must vs may)
    #           reading is usage?


class Parameter:
    """The Parameter class defines the base of a"""

    def __init__(self, parseset: Mapping) -> None:
        self._parseset = parseset

    @property
    def name(self) -> str:
        """Get name of the parameter."""

        return self._parseset["name"]

    @property
    def direction(self) -> Direction:
        """Get semantic direction of parameter."""

        return Direction(self._parseset["param_direction"].upper())

    @property
    def kind(self) -> Kind:
        """Get the Kind associated with the parameter."""

        return KINDS[self._parseset["kind"]]
