"""
This module contains the definition of the F90Procedure and F90Parameter.

Together these are responsible for emitting valid F90 source code for any Procedure.
"""


from typing import Mapping, Optional, Tuple, List, Union
from collections import defaultdict


from .storage import KINDS
from .parameter import Parameter


class F90Parameter(Parameter):
    """This class represents a Fortran 90 parameter."""

    def __str__(self) -> str:
        """ """

        return str(self.name) + str(self.dimensions)

    @property
    def name(self) -> str:
        """Get name of parameter."""

        return self._parseset["name"].upper()

    @property
    def func_type(self) -> str:
        """
        Get access to the func_type.
        """

        # TODO remove asap, similar to isoc

        name = self._parseset["func_type"]

        if name.startswith("MPI_"):
            name = name[4:]

        return name.upper()

    @property
    def type(self) -> str:
        """Get Fortran 90 type of parameter."""

        return self.kind.express.f90 or ""

    @property
    def dimensions(self) -> str:
        """Get dimension of parameter."""

        if (
            "f90_parenthesis" in self._parseset["suppress"]
            or "f90_buf_paren" in self._parseset["suppress"]
        ):
            return ""

        dimensions = list()

        if self._parseset["kind"] in ("BUFFER", "C_BUFFER2", "C_BUFFER3", "STRING_ARRAY"):
            # can these be set to length?
            # length is not None for many
            dimensions.append("*")

        elif self._parseset["kind"] == "F90_STATUS":
            dimensions.append("MPI_STATUS_SIZE")

        elif self._parseset["kind"] == "STATUS":
            dimensions.append("MPI_STATUS_SIZE")

            if self._parseset["length"] is not None:
                dimensions.append(self._parseset["length"])

        # There are cases where we need to emit a length
        elif self._parseset["kind"] == "C_BUFFER4":
            dimensions.append(self._parseset["length"].upper())

        elif self._parseset["kind"] == "STRING_2DARRAY":
            dimensions.append(self._parseset["length"].upper())
            dimensions.append("*")

        # what is this?
        # why do we need to exclude these?
        elif (
            self._parseset["kind"] != "STRING"
            and self._parseset["length"] is not None
            and self._parseset["kind"] != "C_BUFFER4"
        ):
            if isinstance(self._parseset["length"], list):
                # As of MPI-4.0, MPI has parameters with -- at most --
                # 2 dimensions.  No need for a loop.  Indeed, we only
                # want to emit one dimension here -- the other will be
                # '*', and will be handled below.

                dimensions.append(self._parseset["length"][1])

                # use in mpi_group_incl/excl

            # We always need a '*' at the end
            dimensions.append("*")

        if dimensions:
            return "(" + ", ".join(dimensions) + ")"

        return ""


class CPTRF90Parameter(F90Parameter):
    """ """

    @property
    def type(self) -> str:
        """Get Fortran 90 type of parameter."""

        if self.kind.f90_cptr is None:
            return ""

        return self.kind.f90_cptr


class F90Symbol:
    """This class is the base class for all F90 callables."""

    def __init__(self, parseset: Mapping) -> None:
        self._parseset = parseset

    @property
    def name(self) -> str:
        """Fetch the F90Procedure name."""

        # NOTE is there a pattern to when the name_f90 is used?
        return (
            self._parseset["name_f90"] if self._parseset["name_f90"] else self._parseset["name"]
        ).upper()

    @property
    def return_kind(self) -> Optional["Kind"]:
        """Fetch return Kind."""

        kind_name = self._parseset["return_kind"]

        if kind_name in ("NOTHING", "ERROR_CODE"):
            return None

        return KINDS[kind_name]

    @property
    def return_type(self) -> Optional[str]:
        """Fetch return type."""

        return self.return_kind.express.f90 if self.return_kind else None

    @property
    def parameters(self) -> Tuple[F90Parameter, ...]:
        """Fetch parameters for this procedure."""

        def expressible(parameter: Mapping) -> bool:
            return (
                "f90_parameter" not in parameter["suppress"]
                and parameter["kind"] != "VARARGS"
                and parameter["large_only"] is False
            )

        return tuple(
            F90Parameter(parameter)
            for parameter in self._parseset["parameters"]
            if expressible(parameter)
        )

    @property
    def groupings(self) -> Mapping[str, List[F90Parameter]]:
        """Get groups of parameters with the same KIND."""

        groupings = defaultdict(list)

        for parameter in self.parameters:
            groupings[parameter.kind.express.f90].append(parameter)

        return groupings


class IndexOverloadMixin:
    """"""
    # TODO this will disappear after rewrite
    #      we should generate the CPTR expression explicitly

    @property
    def index_overload(self) -> Optional[str]:
        """ """

        return self._parseset["attributes"]["f90_index_overload"]


class NotWithMPIFMixin:
    """"""
    # TODO understand what this is for

    @property
    def not_with_mpif(self) -> bool:
        """ """

        return self._parseset["attributes"]["not_with_mpif"]


class ProfilingMixin:
    """"""

    @property
    def name(self) -> str:
        """"""

        return "P" + super().name


class F90Procedure(IndexOverloadMixin, NotWithMPIFMixin, F90Symbol):
    """
    The F90Procedure represents the entire expression of a Procedure in Fortran 90.
    """

    def __str__(self) -> str:
        """ """

        # return_type + name + parameter_list
        # type parameters
        # ...

        binding = ""

        if self.return_type:
            binding += self.return_type + " "

        binding += self.name + "("
        binding += ", ".join(parameter.name for parameter in self.parameters)
        binding += ")"

        if self.groupings:
            binding += "\n"

            groups = []

            for type_name, parameters in self.groupings.items():
                groups.append(
                    "\t" + type_name + " " + ", ".join(str(parameter) for parameter in parameters)
                )

            binding += "\n".join(groups)

        return binding


class CPTRF90Procedure(F90Procedure):
    """ """

    def __str__(self) -> str:
        binding = ""

        if self.return_type:
            binding += self.return_type + " "

        binding += self.name + "("
        binding += ", ".join(parameter.name for parameter in self.parameters)
        binding += ")"

        if self.groupings:
            binding += "\n"

            binding += self.intrinsic + "\n"

            groups = []

            for type_name, parameters in self.groupings.items():
                groups.append(
                    "\t" + type_name + " " + ", ".join(str(parameter) for parameter in parameters)
                )

            binding += "\n".join(groups)

        return binding

    @property
    def intrinsic(self) -> str:
        """"""

        return "USE, INTRINSIC :: ISO_C_BINDING, ONLY : C_PTR\n\tIMPORT :: MPI_ADDRESS_KIND"

    @property
    def name(self) -> str:
        """"""

        return super().name + "_CPTR"

    @property
    def parameters(self) -> Tuple[Union[F90Parameter, CPTRF90Parameter], ...]:
        """Fetch parameters for this procedure."""

        def expressible(parameter: Mapping) -> bool:
            return (
                "f90_parameter" not in parameter["suppress"]
                and parameter["kind"] != "VARARGS"
                and parameter["large_only"] is False
            )

        # TODO construct CPTRF90Parameter

        return tuple(
            F90Parameter(parameter)
            for parameter in self._parseset["parameters"]
            if expressible(parameter)
        )

    @property
    def groupings(self) -> Mapping[str, List[Union[F90Parameter, CPTRF90Parameter]]]:
        """Get groups of parameters with the same KIND."""

        groupings = defaultdict(list)

        for parameter in self.parameters:
            # TODO use .f90_cptr if exists
            groupings[parameter.kind.express.f90].append(parameter)

        return groupings


class ProfilingF90Procedure(ProfilingMixin, F90Procedure):
    """"""


class ProfilingCPTRF90Procedure(ProfilingMixin, CPTRF90Procedure):
    """"""


class F90Callback(F90Symbol):
    """
    The F90Procedure represents the entire expression of a Procedure in Fortran 90.
    """

    def __str__(self) -> str:
        """ """

        # return_type + name + parameter_list
        # type parameters
        # ...

        binding = ""

        if self.return_type:
            binding += self.return_type + " "

        binding += self.name + "("
        binding += ", ".join(parameter.name for parameter in self.parameters)
        binding += ")"

        if self.groupings:
            binding += "\n"

            groups = []

            for type_name, parameters in self.groupings.items():
                groups.append(
                    "\t" + type_name + " " + ", ".join(str(parameter) for parameter in parameters)
                )

            binding += "\n".join(groups)

        return binding


class F90PredefinedFunction(IndexOverloadMixin, NotWithMPIFMixin, F90Symbol):
    """"""

    def __str__(self) -> str:
        """ """

        # return_type + name + parameter_list
        # type parameters
        # ...

        binding = ""

        if self.return_type:
            binding += self.return_type + " "

        binding += self.name + "("
        binding += ", ".join(parameter.name for parameter in self.parameters)
        binding += ")"

        if self.groupings:
            binding += "\n"

            groups = []

            for type_name, parameters in self.groupings.items():
                groups.append(
                    "\t" + type_name + " " + ", ".join(str(parameter) for parameter in parameters)
                )

            binding += "\n".join(groups)

        return binding
