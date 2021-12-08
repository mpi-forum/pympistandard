"""
This module contains the definition of the ISOCProcedure and ISOCParameter.

Together these are responsible for emitting valid ISO C source code for any Procedure.
"""


# pylint: disable=too-few-public-methods


from typing import Mapping, Tuple, Union, List, Any
import logging


from .storage import KINDS
from .parameter import Parameter


class ISOCParameter(Parameter):
    """The ISOCParameter represents the entire expression of a Procedure in ISO C."""

    def __str__(self) -> str:
        """Get full expression of ISO C parameter."""

        if self.kind is KINDS.varargs:
            return self.type

        # const + type + pointer + name + array
        expression = "const " if self.constant else ""
        expression += str(self.type) + " "
        expression += self.name
        expression += self.array

        return expression

    @property
    def constant(self) -> bool:
        """Get a boolean about constness."""

        return self._parseset["constant"]

    @property
    def func_type(self) -> str:
        """Give access to the func_type for FUNCTION kinds."""

        # TODO this will be removed with the flattening of all function kinds
        #      into separate kinds

        assert self.kind in (KINDS.FUNCTION, KINDS.POLYFUNCTION, KINDS.FUNCTION_SMALL)

        return self._parseset["func_type"]

    @property
    def base_type(self) -> str:
        """Get the base type of the parameter in C."""

        if self._parseset["kind"] in ("FUNCTION", "FUNCTION_SMALL"):
            # TODO move all func_type into KINDs, this is really just a subspace of KINDs
            return f"{self._parseset['func_type']}"

        if self._parseset["kind"] == "POLYFUNCTION":
            # TODO move all func_type into KINDs, this is really just a subspace of KINDs
            return f"{self._parseset['func_type']}"

        return self.kind.express.iso_c

    @property
    def type(self, pointer_on_name: bool = False) -> str:
        """Get the entire type (derived included, pointers)."""

        return self.base_type + (" " if pointer_on_name else "") + ("*" * self.pointer_level)

    @property
    def pointer_level(self) -> int:
        """Get the pointer level of this parameter."""

        if self._parseset["pointer"] is not None and not self._parseset["pointer"]:
            return 0

        if self._parseset["kind"] == "STRING_2DARRAY":
            return 2

        if self._parseset["kind"] == "ARGUMENT_LIST":
            return 3

        # needed for MPI_UNPACK_EXTERNAL[_size]
        if (
            self._parseset["kind"] == "STRING"
            and self._parseset["length"] == "*"
            and not self._parseset["pointer"]
        ):
            return 0

        if self._parseset["kind"] in (
            "BUFFER",
            "C_BUFFER",
            "C_BUFFER2",
            "C_BUFFER3",
            "C_BUFFER4",
            "STRING",
            "EXTRA_STATE",
            "EXTRA_STATE2",
            "ATTRIBUTE_VAL",
            "STATUS",
            "ATTRIBUTE_VAL_10",
            "STRING_ARRAY",
            "FUNCTION",
            "FUNCTION_SMALL",
            "POLYFUNCTION",
            "TOOL_MPI_OBJ",
            "F08_STATUS",
            "F90_STATUS",
        ):
            return 1

        if (
            self._parseset["param_direction"] == "inout"
            or self._parseset["param_direction"] == "out"
            or self._parseset["pointer"]
        ) and self._parseset["length"] is None:
            return 1

        return 0

    @property
    def array(self) -> str:
        """Get the array symbols if required."""

        if self._parseset["kind"] == "C_BUFFER4":
            # length set on MPI_User_function
            return ""

        if (
            self._parseset["kind"] != "STRING"
            and self._parseset["length"] is not None
            and not isinstance(self._parseset["length"], list)
            and not self._parseset["pointer"]
        ):
            return "[]"

        # required by MPI_UNPACK_EXTERNAL, it uses array notation for a string.
        if (
            self._parseset["kind"] == "STRING"
            and self._parseset["length"] == "*"
            and not self._parseset["pointer"]
        ):
            return "[]"

        if self._parseset["kind"] == "STRING_ARRAY" or self._parseset["kind"] == "STRING_2DARRAY":
            return "[]"

        # As of MPI-4.0, we have array parameters with -- at most -- 2
        # dimensions.  Always print the first dimension as [] (above).
        # If we have a second dimension, print it (e.g.,
        # MPI_GROUP_RANGE_INCL & EXCL).
        if isinstance(self._parseset["length"], list):
            return f'[][{self._parseset["length"][1]}]'

        return ""


class EmbiggenedISOCParameter(ISOCParameter):
    """
    The EmbiggenedISOCParameter represents the entire expression of an embiggened
    Procedure in ISO C.
    """

    def __init__(self, parseset: Mapping, embiggening: str):
        super().__init__(parseset)

        self._embiggening = embiggening

    @property
    def type(self) -> str:
        """Get the type of the parameter in C."""

        if self._parseset["kind"] in ("FUNCTION", "FUNCTION_SMALL"):
            # TODO move all func_type into KINDs, this is really just a subspace of KINDs
            #      the func_type in the parameter function of the DSL actually moves Kind
            #      information out of the Kind, so this needs to be removed!
            return f"{self._parseset['func_type']}"

        if self._parseset["kind"] == "POLYFUNCTION":
            # TODO move all func_type into KINDs, this is really just a subspace of KINDs
            return f"{self._parseset['func_type']}{self._embiggening}"

        return self.kind.express.embiggen.iso_c or self.kind.express.iso_c


class ProfilingMixin:
    """The ProfilingMixin modifies the name to be prefixed with a _P_."""

    _parseset: Mapping[str, Any] = {}

    @property
    def name(self) -> str:
        """Fetch the PMPI naming."""

        return f"P{self._parseset['name']}"


class ISOCSymbol:
    """The base class for all ISO C expressions."""

    def __init__(self, parseset: Mapping) -> None:
        self._parseset = parseset

    def __str__(self) -> str:
        binding = f"{self.return_type} {self.name}("

        parameter_list = ", ".join(str(parameter) for parameter in self.parameters)

        if parameter_list:
            binding += parameter_list

        else:
            # exception for MPI_Finalize, MPI_Wtime, MPI_Wtick with zero parameters
            binding += "void"

        binding += ")"

        return binding

    @property
    def name(self) -> str:
        """Gives access to the ISO C name."""

        return f"{self._parseset['name']}"

    @property
    def parameters(self) -> Tuple[ISOCParameter, ...]:
        """Fetch all parameters of the ISOCProcedure."""

        def expressible(parameter: Mapping) -> bool:
            return "c_parameter" not in parameter["suppress"] and not parameter["large_only"]

        return tuple(
            ISOCParameter(parameter)
            for parameter in self._parseset["parameters"]
            if expressible(parameter)
        )

    @property
    def return_kind(self) -> "Kind":
        """Get the return kind."""

        return KINDS[self._parseset["return_kind"]]

    @property
    def return_type(self) -> str:
        """Get the return type as a vaid C type string."""

        return self.return_kind.express.iso_c


class EmbiggenedISOCSymbol(ISOCSymbol):
    """This class is base class for the embiggened expression of an ISO C Symbol."""

    def __init__(self, parseset: Mapping, embiggening: str) -> None:
        super().__init__(parseset)

        self._embiggening = embiggening

    @property
    def name(self) -> str:
        """Gives access to the ISO C name."""

        return f"{self._parseset['name']}{self._embiggening}"

    @property
    def parameters(self) -> Tuple[Union[ISOCParameter, EmbiggenedISOCParameter], ...]:
        """Fetch all parameters of the ISOCProcedure."""

        def expressible(parameter: Mapping) -> bool:
            return "c_parameter" not in parameter["suppress"]

        parameters: List[Union[ISOCParameter, EmbiggenedISOCParameter]] = []
        for parameter in self._parseset["parameters"]:
            if expressible(parameter):
                if parameter["kind"].startswith("POLY"):
                    parameters.append(EmbiggenedISOCParameter(parameter, self._embiggening))

                else:
                    parameters.append(ISOCParameter(parameter))

        return tuple(parameters)

    @property
    def return_type(self) -> str:
        """Get the return type as a vaid C type string."""

        return self.return_kind.express.embiggen.iso_c or self.return_kind.express.iso_c


class UppercaseIndexMixin:
    """
    The UppercaseIndexMixin provides the uppercase_index handling for ISOCProcedures.
    """

    _parseset: Mapping[str, Any] = {}

    def has_uppercase_index(self) -> bool:
        """Whether this procedure should be written capitalized in the function index."""

        return self._parseset["attributes"]["index_upper"]


class CallbackMixin:
    """
    The CallbackMixin provides the __str__ method and adds the typedef infront of the prototype.
    """

    def __str__(self) -> str:
        return "typedef " + super().__str__()


class ISOCProcedure(UppercaseIndexMixin, ISOCSymbol):
    """The ISOCProcedure represents the entire expression of a Procedure in ISO C."""


class EmbiggenedISOCProcedure(UppercaseIndexMixin, EmbiggenedISOCSymbol):
    """
    The EmbiggenedISOCProcedure represents the entire expression of an embiggened
    Procedure in ISO C.
    """


class ISOCCallback(CallbackMixin, ISOCSymbol):
    """This class is the ISO C Callback expression."""


class EmbiggenedISOCCallback(CallbackMixin, EmbiggenedISOCSymbol):
    """This class is the embiggened ISO C Callback expression."""


class ISOCPredefinedFunction(ISOCSymbol):
    """This class is the ISO C predefined function expression."""

    # TODO remove this, requires DSL changes
    #      needs removing of capitalized attribute, no need for it. Only used with
    #      MPI_CONVERSION_FN_NULL. All others are capitalized in the name
    @property
    def name(self) -> str:
        if self._parseset["name"].upper() != self._parseset["name"]:
            logging.critical("Lowercase name of predefined function. %s", self._parseset["name"])

        return f"{self._parseset['name']}".upper()


class EmbiggenedISOCPredefinedFunction(EmbiggenedISOCSymbol):
    """This class is the embiggened ISO C predefined function expression."""

    # TODO remove this, requires DSL changes
    # needs removing of capitalized attribute, no need for it. Only used with MPI_CONVERSION_FN_NULL
    @property
    def name(self) -> str:
        if self._parseset["name"].upper() != self._parseset["name"]:
            logging.critical("Lowercase name of predefined function. %s", self._parseset["name"])

        return f"{self._parseset['name']}{self._embiggening}".upper()


class ProfilingISOCProcedure(ProfilingMixin, ISOCProcedure):
    """This class is the PMPI expression of the ISO C procedure."""


class EmbiggenedProfilingISOCProcedure(ProfilingMixin, EmbiggenedISOCProcedure):
    """This class if the embiggened PMPI expression of the ISO C procedure."""
