"""
This module defines the Kind and PolyKind types.

The Kind represents a cross language internal to MPI type.
"""


from dataclasses import dataclass
from collections import defaultdict
from typing import Optional, MutableMapping, TYPE_CHECKING


from .storage import CALLBACKS


if TYPE_CHECKING:
    from .callback import Callback


# NOTE Kind will in future need to support value space, SEND_RANK = (natural numbers, MPI_PROC_NULL)
#      excluding ("MPI_ANY_SOURCE")
#
#      whereas RECV_RANK = (natural numbers, MPI_PROC_NULL, MPI_ANY_SOURCE)
#      or TAG = (natural numbers up to MPI_TAG_UB)


class KindExpression:
    """This class is for representing a Kind in a specific language."""

    def __init__(self, kind: "Kind") -> None:
        self._properties: MutableMapping[str, bool] = defaultdict(lambda: False)
        self._kind = kind

    @property
    def embiggen(self) -> "KindExpression":
        """Embiggen the expression of the Kind."""

        self._properties["embiggen"] = True
        return self

    @property
    def lis(self) -> Optional[str]:
        """Express the kind in the LIS form."""

        return self._kind._lis

    @property
    def iso_c(self) -> Optional[str]:
        """Express the kind in the ISO C form."""

        if self._properties["embiggen"]:
            if self._kind.has_embiggenment():
                return self._kind._iso_c_large

            return None

        return self._kind._iso_c_small

    @property
    def f08(self) -> Optional[str]:
        """Express the Kind in the Fortran 2008 form."""

        if self._properties["embiggen"]:
            return self._kind._f08_large

        return self._kind._f08_small

    @property
    def f90(self) -> Optional[str]:
        """Express the Kind in the Fortran 90 form."""

        if self._properties["embiggen"]:
            return None

        return self._kind._f90_small


class KindExpressions(KindExpression):
    """This class is the entry point for the dot notation of expressing a Kind."""

    @property
    def embiggen(self) -> KindExpression:
        return KindExpression(self._kind).embiggen


@dataclass(frozen=True)
class Kind:
    """
    The Kind class replaces the previous AoS apporach to kinds. Each kind will
    individually hold its expressions in each language and size form.
    """

    name: str

    _lis: Optional[str] = None

    _iso_c_small: Optional[str] = None
    _f90_small: Optional[str] = None
    _f08_small: Optional[str] = None

    def has_embiggenment(self) -> bool:
        """Gets whether the Kind has an embiggenment form."""

        # NOTE this should be removed, this is a RTTI which python already is.

        return False

    @property
    def callback(self) -> Optional['Callback']:
        """Access the relevant Callback object for this Kind."""

        # NOTE this should eventually be non-optional, all FUNCTION KINDs will have a Callback
        #      object association

        if self.name in ("FUNCTION", "FUNCTION_SMALL", "POLYFUNCTION"):
            # NOTE this doesn't exist for most KINDs except *FUNCTION*
            #      currently not possible since FUNCTION kinds don't have any knowledge

            return None

        if "CB_FUNCTION" in self.name:
            # These are the MPI_T_Event callbacks
            # EVENT_CB_FUNCTION, EVENT_FREE_CB_FUNCTION, EVENT_DROP_CB_FUNCTION

            return CALLBACKS["MPI_T_" + self.name]

        return None

    @property
    def express(self) -> KindExpressions:
        """Get the KindExpression object to express the Kind in a language."""

        return KindExpressions(self)


@dataclass(frozen=True)
class PolyKind(Kind):
    """
    The Kind class replaces the previous AoS apporach to kinds. Each kind will
    individually hold its expressions in each language and size form.
    """

    _iso_c_large: Optional[str] = None
    _f08_large: Optional[str] = None

    def has_embiggenment(self) -> bool:
        return True


@dataclass(frozen=True)
class CPTRKind(Kind):
    """
    This Kind class is used with the four special index overloading _CPTR F90 procedures,
    MPI_ALLOC_MEM, MPI_WIN_ALLOCATE, MPI_WIN_ALLOCATE_SHARED, MPI_WIN_SHARED_QUERY.

    In which cases there is another expression aside from the original MPI_ADDRESS_KIND.
    """

    _f90_cptr: Optional[str] = None
