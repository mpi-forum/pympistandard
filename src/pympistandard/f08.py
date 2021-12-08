"""
"""


from typing import Mapping, Tuple, Union, Optional, List
from collections import defaultdict


from .storage import KINDS
from .parameter import Parameter, Direction


class IntentMixin:
    """This mixin contains the functionality for the intent stating of a Fortran 2008 parameter."""

    @property
    def intent(self) -> Optional[str]:
        """ """

        if self.kind is KINDS.error_code_show_intent:
            # conflict between ignore_intent and this
            return f"INTENT({self.direction.value})"

        if "f08_intent" in self._parseset["suppress"]:
            return None

        if self.kind is KINDS.status and self.direction == Direction.OUT:
            # Do not issue an intent for OUT status because the
            # user may pass MPI_STATUS[ES]_IGNORE, and therefore
            # it's also an IN parameter, too.
            return None

        if self.kind is KINDS.buffer and self.direction == Direction.OUT:
            # Similar to above, do not issue an intent for OUT
            # buffer because the user may pass MPI_BOTTOM, and
            # therefore it's also an IN parameter, too.
            return None

        if self.kind is KINDS.buffer and self.direction == Direction.INOUT:
            # Similar to above, do not issue an intent for INOUT
            # see MPI_Sendrecv_replace
            return None

        if self.kind is KINDS.function and self.direction == Direction.IN:
            # ...Jeff does not remember why we do not specify
            # INTENT for FUNCTION (i.e., PROCEDURE) types, but we
            # don't...
            return None

        if self.kind is KINDS.polyfunction and self.direction == Direction.IN:
            # ...Dan (for issue 396) duplicated the suppression of
            # INTENT for POLYFUNCTION (i.e., PROCEDURE) types
            return None

        if "f08_intent" not in self._parseset["suppress"]:
            # Otherwise, unless the binding specifically asked us
            # to suppress the F08 intent (e.g.,
            # MPI_BUFFER_ATTACH), emit it.
            return f"INTENT({self.direction.value})"

        return None

    @property
    def descriptor(self) -> str:
        """ """

        return ", ".join(
            filter(
                lambda attr: attr is not None,
                (f"{self.type}{self.type_length}", self.optional, self.intent, self.asynchronous),
            )
        )


class EmbiggenedMixin:
    """"""

    def __init__(self, parseset: Mapping, embiggening: str) -> None:
        super().__init__(parseset)

        self._embiggening = embiggening

    @property
    def type(self) -> str:
        """ """

        # TODO the function except will be removed soon

        if self.kind in (KINDS.FUNCTION, KINDS.FUNCTION_SMALL, KINDS.POLYFUNCTION):
            return (
                f"{self.kind.express.embiggen.f08}"
                f"({self._parseset['func_type']}{self._embiggening})"
            )

        return self.kind.express.embiggen.f08 or self.kind.express.f08


class F08ParameterBase(Parameter):
    """This class is the base class for all Fortran 2008 parameters."""

    def __str__(self) -> str:
        """ """

        return self.name + self.name_length

    @property
    def intrinsic(self) -> Optional[str]:
        """ """

        if self.kind in (KINDS.c_buffer, KINDS.c_buffer2, KINDS.c_buffer3, KINDS.c_buffer4):
            return r"USE, INTRINSIC\ ::\ ISO_C_BINDING, ONLY : C_PTR \\ "

        return None

    @property
    def descriptor(self) -> str:
        """ """

        return ", ".join(
            filter(
                lambda attr: attr is not None,
                (f"{self.type}{self.type_length}", self.optional, self.asynchronous),
            )
        )

    @property
    def type(self) -> str:
        """ """

        # TODO the function except will be removed soon

        if self.kind in (KINDS.FUNCTION, KINDS.FUNCTION_SMALL, KINDS.POLYFUNCTION):
            return f"{self.kind.express.f08}({self._parseset['func_type']})"

        return self.kind.express.f08

    @property
    def intent(self) -> Optional[str]:
        """ """

        if self.kind is KINDS.error_code_show_intent:
            # conflict between ignore_intent and this
            return f"INTENT({self.direction.value})"

        if "f08_intent" in self._parseset["suppress"]:
            return None

        if self.kind is KINDS.status and self.direction == Direction.OUT:
            # Do not issue an intent for OUT status because the
            # user may pass MPI_STATUS[ES]_IGNORE, and therefore
            # it's also an IN parameter, too.
            return None

        if self.kind is KINDS.buffer and self.direction == Direction.OUT:
            # Similar to above, do not issue an intent for OUT
            # buffer because the user may pass MPI_BOTTOM, and
            # therefore it's also an IN parameter, too.
            return None

        if self.kind is KINDS.buffer and self.direction == Direction.INOUT:
            # Similar to above, do not issue an intent for INOUT
            # see MPI_Sendrecv_replace
            return None

        if self.kind is KINDS.function and self.direction == Direction.IN:
            # ...Jeff does not remember why we do not specify
            # INTENT for FUNCTION (i.e., PROCEDURE) types, but we
            # don't...
            return None

        if self.kind is KINDS.polyfunction and self.direction == Direction.IN:
            # ...Dan (for issue 396) duplicated the suppression of
            # INTENT for POLYFUNCTION (i.e., PROCEDURE) types
            return None

        if "f08_intent" not in self._parseset["suppress"]:
            # Otherwise, unless the binding specifically asked us
            # to suppress the F08 intent (e.g.,
            # MPI_BUFFER_ATTACH), emit it.
            return f"INTENT({self.direction.value})"

        return None

    @property
    def optional(self) -> Optional[str]:
        """ """

        return "OPTIONAL" if self._parseset["optional"] else None

    @property
    def asynchronous(self) -> Optional[str]:
        """ """

        return "ASYNCHRONOUS" if self._parseset["asynchronous"] else None

    @property
    def type_length(self) -> str:
        """ """

        # If this is a string and we have a length, also emit that
        if self._parseset["kind"] in ("STRING", "STRING_ARRAY"):
            length = self._parseset["length"]
            return f"(LEN={length})" if length else "(LEN=*)"

        if self._parseset["kind"] == "STRING_2DARRAY":
            return "(LEN=*)"

        return ""

    @property
    def name_length(self) -> str:
        """ """

        if self.kind is KINDS.f90_status:
            return "(MPI_STATUS_SIZE)"

        if self.kind is KINDS.string_array:
            return "(*)"

        if self.kind is KINDS.string_2darray:
            return f"({self._parseset['length']}, *)"

        if self._parseset is not None and self._parseset["array_type"] == "hidden":
            return "(*)"

        if (
            self.kind is not KINDS.string
            and self._parseset["length"] is not None
            and self.kind is not KINDS.c_buffer4
        ):
            if isinstance(self._parseset["length"], list):
                return f"({', '.join(reversed(self._parseset['length']))})"

            if self._parseset["length"] == "":
                return "(*)"

            if self._parseset["length"] is not None:
                return f"({self._parseset['length']})"

        return ""


class F08Parameter(IntentMixin, F08ParameterBase):
    """This class is a Fortran 2008 parameter."""


class EmbiggenedF08Parameter(EmbiggenedMixin, F08Parameter):
    """This class is an embiggened Fortran 2008 parameter."""


class F08ParameterCallback(F08ParameterBase):
    """
    This classs is a Fortran 2008 parameter which does not print an intent, but still has a
    semantic direction.
    """


class EmbiggenedF08ParameterCallback(EmbiggenedMixin, F08ParameterBase):
    """
    This class is an embiggened Fortran 2008 parameter which does not print an intent, but still
    has a semantic direction.
    """


class ProfilingMixin:
    """This mixing contains the name change to the PMPI prefix."""

    @property
    def name(self) -> str:
        return "P" + super().name


class CallbackMixin:
    """This mixin contains the to str functionality of a Fortran 2008 callback."""

    def __str__(self) -> str:
        """"""

        binding = "ABSTRACT INTERFACE"

        lines = super().__str__().split("\n\t")

        binding += "\n\t" + lines[0]

        for line in lines[1:]:
            binding += "\n\t\t" + line

        return binding


class F08Symbol:
    """This class is a base class for all Fortran 2008 symbols."""

    def __init__(self, parseset: Mapping) -> None:
        self._parseset = parseset

    def __str__(self) -> str:
        """Get source code."""

        binding = ""

        if self.return_type:
            binding += self.return_type + " "

        binding += self.name + "("
        binding += ", ".join(parameter.name for parameter in self.parameters)
        binding += ")"

        if self.parameters:
            binding += "\n\t" + self.intrinsic if self.intrinsic else ""

            binding += "\n\t"

            descriptors = []

            for descriptor, parameters in self.groupings.items():
                descriptors.append(descriptor + " :: " + ", ".join(map(str, parameters)))

            binding += "\n\t".join(descriptors)

        return binding

    @property
    def name(self) -> str:
        """Get Fortran 2008 name."""

        return self._parseset["name"]

    @property
    def return_kind(self) -> Optional["Kind"]:
        """ """

        kind_name = self._parseset["return_kind"]

        if kind_name in ("NOTHING", "ERROR_CODE"):
            return None

        return KINDS[self._parseset["return_kind"]]

    @property
    def return_type(self) -> Optional[str]:
        """ """

        if self.return_kind:
            return self.return_kind.express.f08

        return None

    @property
    def groupings(self) -> Mapping[str, List[F08Parameter]]:
        """ """

        groupings = defaultdict(list)

        for parameter in self.parameters:
            groupings[parameter.descriptor].append(parameter)

        return groupings

    @property
    def parameters(self) -> Tuple[F08Parameter, ...]:
        """ """

        def expressible(parameter) -> bool:
            return (
                "f08_parameter" not in parameter["suppress"]
                and parameter["kind"] != "VARARGS"
                and parameter["large_only"] is False
            )

        return tuple(
            F08Parameter(parameter)
            for parameter in self._parseset["parameters"]
            if expressible(parameter)
        )

    @property
    def intrinsic(self) -> Optional[str]:
        """ """

        has_intrinsic = any(parameter.intrinsic for parameter in self.parameters)

        if not has_intrinsic:
            return ""

        return r"USE, INTRINSIC :: ISO_C_BINDING, ONLY : C_PTR"


class EmbiggenedF08Symbol(F08Symbol):
    """This class is a base class for all embiggened fortran symbols."""

    def __init__(self, parseset: Mapping, embiggening: str) -> str:
        self._parseset = parseset

        self._embiggening = embiggening

    @property
    def return_type(self) -> Optional[str]:
        """ """

        if self.return_kind:
            if self.return_kind.express.embiggen:
                return self.return_kind.express.embiggen.f08

            return self.return_kind.express.f08

        return None

    @property
    def name(self) -> str:
        """Get Fortran 2008 name."""

        if not self._parseset["attributes"]["f08_abstract_interface"]:
            return f"{self._parseset['name']}{self._embiggening}"

        return self._parseset["name"]

    @property
    def parameters(self) -> Tuple[Union[F08Parameter, EmbiggenedF08Parameter], ...]:
        """Get all parameters."""

        def expressible(parameter) -> bool:
            return "f08_parameter" not in parameter["suppress"] and parameter["kind"] != "VARARGS"

        parameters: List[Union[F08Parameter, EmbiggenedF08Parameter]] = []
        for parameter in self._parseset["parameters"]:
            if expressible(parameter):
                if parameter["kind"].startswith("POLY"):
                    parameters.append(EmbiggenedF08Parameter(parameter, self._embiggening))

                else:
                    parameters.append(F08Parameter(parameter))

        return tuple(parameters)


class F08Procedure(F08Symbol):
    """This class represents a Fortran 2008 procedure."""


class ProfilingF08Procedure(ProfilingMixin, F08Symbol):
    """This class represents a PMPI Fortran 2008 procedure."""


class EmbiggenedF08Procedure(EmbiggenedF08Symbol):
    """This class represents a Fortran 2008 embiggened procedure."""


class EmbiggenedProfilingF08Procedure(ProfilingMixin, EmbiggenedF08Procedure):
    """This class represents a Embiggened PMPI Fortran 2008 procedure."""


class F08Callback(CallbackMixin, F08Symbol):
    """This class represents a Fortran 2008 callback."""

    @property
    def parameters(self) -> Tuple[F08ParameterCallback, ...]:
        """Get all parameters of the Callback."""

        def expressible(parameter) -> bool:
            return (
                "f08_parameter" not in parameter["suppress"]
                and parameter["kind"] != "VARARGS"
                and parameter["large_only"] is False
            )

        return tuple(
            F08ParameterCallback(parameter)
            for parameter in self._parseset["parameters"]
            if expressible(parameter)
        )

    @property
    def groupings(self) -> Mapping[str, List[F08ParameterCallback]]:
        """Get all groupings of parameters of the Callback."""

        groupings = defaultdict(list)

        for parameter in self.parameters:
            groupings[parameter.descriptor].append(parameter)

        return groupings


class EmbiggenedF08Callback(CallbackMixin, EmbiggenedF08Symbol):
    """"""

    def __init__(self, parseset: Mapping, postfix: str) -> None:
        self._parseset = parseset

        self._embiggening = postfix

    @property
    def name(self) -> str:
        """Get Fortran 2008 name."""

        return self._parseset["name"] + self._embiggening

    @property
    def parameters(self) -> Tuple[Union[F08ParameterCallback, EmbiggenedF08ParameterCallback], ...]:
        """ """

        def expressible(parameter) -> bool:
            return "f08_parameter" not in parameter["suppress"] and parameter["kind"] != "VARARGS"

        parameters: List[Union[F08ParameterCallback, EmbiggenedF08ParameterCallback]] = []
        for parameter in self._parseset["parameters"]:
            if expressible(parameter):
                if parameter["kind"].startswith("POLY"):
                    parameters.append(EmbiggenedF08ParameterCallback(parameter, self._embiggening))

                else:
                    parameters.append(F08ParameterCallback(parameter))

        return tuple(parameters)


class F08PredefinedFunction(F08Symbol):
    """This class represents a Fortran 2008 predefined function."""

    @property
    def parameters(self) -> Tuple[F08Parameter, ...]:
        """Get all parameters of predefined function."""

        def expressible(parameter) -> bool:
            return (
                "f08_parameter" not in parameter["suppress"]
                and parameter["kind"] != "VARARGS"
                and parameter["large_only"] is False
            )

        parameters = []

        for parameter in self._parseset["parameters"]:
            if expressible(parameter):
                if "SHOW_INTENT" in parameter["kind"]:
                    parameters.append(F08Parameter(parameter))

                else:
                    # TODO rename F08ParameterCallback
                    parameters.append(F08ParameterCallback(parameter))

        return tuple(parameters)

    @property
    def groupings(self) -> Mapping[str, List[F08Parameter]]:
        """Get all groupings of the predefined function."""

        groupings = defaultdict(list)

        for parameter in self.parameters:
            groupings[parameter.descriptor].append(parameter)

        return groupings


class EmbiggenedF08PredefinedFunction(EmbiggenedF08Symbol):
    """This class represents an embiggened fortran 2008 predefined function."""

    @property
    def name(self) -> str:
        # TODO investigate why this is required, something is not right!
        return super().name.upper()

    @property
    def parameters(self) -> Tuple[Union[F08Parameter, EmbiggenedF08Parameter], ...]:
        """Get all parameters of the predefined function."""

        def expressible(parameter) -> bool:
            return (
                "f08_parameter" not in parameter["suppress"]
                and parameter["kind"] != "VARARGS"
                and parameter["large_only"] is False
            )

        parameters = []

        for parameter in self._parseset["parameters"]:
            if expressible(parameter):
                if parameter["kind"].startswith("POLY"):
                    parameters.append(EmbiggenedF08ParameterCallback(parameter, self._embiggening))

                else:
                    parameters.append(F08ParameterCallback(parameter))

        return tuple(parameters)
