"""
"""


from typing import Mapping, MutableMapping, Tuple, Optional
from collections import defaultdict


from .kind import Kind
from .storage import KINDS


_DEFAULT_DESCRIPTIONS: MutableMapping[str, str] = defaultdict(lambda: "")

_DEFAULT_DESCRIPTIONS.update(
    {
        "ERROR_CODE": "error code",
        "ERROR_CLASS": "error class",
        "COMMUNICATOR": "communicator",
        "ERRHANDLER": "\\MPI/ error handler",
        "INFO": "info argument",
        "FILE": "file",
        "REQUEST": "communication request",
        "STATUS": "status object",
        "WINDOW": "window object",
        "ASSERT": "program assertion",
    }
)


class LISParameter:
    """This class represents the LIS expression of a parameter."""

    def __init__(self, parseset: Mapping) -> None:
        self._parseset = parseset

    @property
    def name(self) -> str:
        """Get the name of the parameter."""

        return "\\ldots" if self.kind is KINDS.varargs else self._parseset["name"]

    @property
    def direction(self) -> str:
        """Get the semantic direction of the parameter."""

        return self._parseset["lis_direction"].upper()

    @property
    def description(self) -> str:
        """Get the description of the parameter."""

        desc = self._parseset["desc"]

        if not desc:
            assert self.kind is not None
            return _DEFAULT_DESCRIPTIONS[self.kind.name]

        # return desc.replace(r"\_", "_")
        # NOTE issue for later, descriptions should not have escaped underscores
        #      it is invalid input to have escaping underscores in the description from the DSL
        return desc

    @property
    def root_only(self) -> bool:
        """Access if the parameter is only important for the root of a collective operation."""

        return self._parseset["root_only"]

    @property
    def embiggened_only(self) -> bool:
        """Access if the parameter is only expressed in embiggened bindings."""

        return self._parseset["large_only"]

    @property
    def kind(self) -> Optional["Kind"]:
        """Get the Kind of this parameter."""

        kind = KINDS[self._parseset["kind"]]

        return None if kind.lis is None else kind

    @property
    def type(self) -> str:
        """Get the LIS type of this parameter."""

        if self.kind is None or self.kind.express.lis is None:
            return ""

        if "lis_paren" in self._parseset["suppress"] or "lis_kind" in self._parseset["suppress"]:
            return ""

        if self.kind in (KINDS.STRING, KINDS.STRING_2DARRAY):
            return self.kind.express.lis

        if self._parseset["length"] is not None:
            plural = "" if self._parseset["kind"] == "STATUS" else "s"

            return f"array of {self.kind.express.lis}{plural}"

        return self.kind.express.lis


class LISSymbol:
    """This class is the base class for all LIS callables."""

    def __init__(self, parseset: Mapping) -> None:
        self._parseset = parseset


class LISProcedure(LISSymbol):
    """This class is for the LIS procedure expression."""

    @property
    def name(self) -> str:
        """Access the name of the LIS expression."""

        return self._parseset["name"].upper()

    @property
    def parameters(self) -> Tuple[LISParameter, ...]:
        """Access all parameters shown in the LIS expression."""

        def expressible(parameter) -> bool:
            return "lis_parameter" not in parameter["suppress"]

        return tuple(
            LISParameter(parameter)
            for parameter in self._parseset["parameters"]
            if expressible(parameter)
        )
