"""
This module contains the Expressions class.
"""


# pylint: disable=wildcard-import, undefined-variable


from collections import defaultdict
from typing import Mapping, Union, Optional


from .lis import *
from .isoc import *
from .f08 import *
from .f90 import *


SUFFIX = "_c"


_VALID_LIS_COMPOSITIONS = {"procedure.lis": LISProcedure}


_VALID_ISO_C_COMPOSITIONS = {
    "procedure.iso_c": ISOCProcedure,
    "procedure.profile.iso_c": ProfilingISOCProcedure,
    "procedure.embiggen.iso_c": EmbiggenedISOCProcedure,
    "procedure.embiggen.profile.iso_c": EmbiggenedProfilingISOCProcedure,
    "callback.iso_c": ISOCCallback,
    "callback.embiggen.iso_c": EmbiggenedISOCCallback,
    "predefinedfunction.iso_c": ISOCPredefinedFunction,
    "predefinedfunction.embiggen.iso_c": EmbiggenedISOCPredefinedFunction,
}


_VALID_F08_COMPOSITIONS = {
    "procedure.f08": F08Procedure,
    "procedure.profile.f08": ProfilingF08Procedure,
    "procedure.embiggen.f08": EmbiggenedF08Procedure,
    "procedure.embiggen.profile.f08": EmbiggenedProfilingF08Procedure,
    "callback.f08": F08Callback,
    "callback.embiggen.f08": EmbiggenedF08Callback,
    "predefinedfunction.f08": F08PredefinedFunction,
    "predefinedfunction.embiggen.f08": EmbiggenedF08PredefinedFunction,
}


_VALID_F90_COMPOSITIONS = {
    "procedure.f90": F90Procedure,
    "procedure.cptr.f90": CPTRF90Procedure,
    "procedure.profile.f90": ProfilingF90Procedure,
    "procedure.cptr.profile.f90": ProfilingF90Procedure,
    "callback.f90": F90Callback,
    "predefinedfunction.f90": F90PredefinedFunction,
}


class Expression:
    """
    The Expression object contains the partial or full url of the expression the user is wanting
    to have created.
    """

    def __init__(self, parseset: Mapping, symbol: str) -> None:
        self._parseset = parseset

        self._properties = defaultdict(lambda: False)
        self._symbol = symbol

    def __str__(self) -> str:
        """
        Access the final URL of this expression before the language.

        The rule is that the ordering is sorted alphabetically. When we find a situation
        that requires specific ordering this will have to be revisited.

        Examples:
         - .embiggen.profile
         - .cptr.profile
        """

        return ".".join(sorted(name for name, existance in self._properties.items() if existance))

    #    def __getitem__(self, url: str) -> Optional[Union[LISSymbol, ISOCSymbol, F08Symbol, F90Symbol]]:
    #        """Allow bracket access to the expressions."""
    #
    #        return

    def _access_all_expressions(self, urls) -> Tuple:
        """Access all expressions of urls."""

        return tuple(
            expr
            for expr in (self._express_url(url, urls) for url in urls if self._symbol in url)
            if expr is not None
        )

    @property
    def all_iso_c(self) -> Tuple[ISOCSymbol]:
        """Access all ISO C expressions."""

        return self._access_all_expressions(_VALID_ISO_C_COMPOSITIONS)

    @property
    def all_f08(self) -> Tuple[F08Symbol]:
        """Access all F08 expressions."""

        return self._access_all_expressions(_VALID_F08_COMPOSITIONS)

    @property
    def all_f90(self) -> Tuple[F90Symbol]:
        """Access all F90 expressions."""

        return self._access_all_expressions(_VALID_F90_COMPOSITIONS)

    def _has_embiggenment(self) -> bool:
        """"""

        # is there a better way to query this?

        return any(
            parameter["kind"].startswith("POLY") for parameter in self._parseset["parameters"]
        )

    def _has_cptr(self) -> bool:
        """"""

        return self._parseset["attributes"]["f90_index_overload"] is not None

    def _express_composition(
        self, language: str, compositions: Mapping
    ) -> Optional[Union[LISSymbol, ISOCSymbol, F08Symbol, F90Symbol]]:
        """
        Fetch and instantiate the correct underlying class and check for errors in the composition.
        """

        lang_map = {"lis": "lis", "iso_c": "c", "f08": "f08", "f90": "f90"}

        # check expressibility in language
        if not self._parseset["attributes"][lang_map[language] + "_expressible"]:
            return None

        url = ".".join(filter(lambda com: bool(com), (self._symbol, str(self), language)))

        return self._express_url(url, compositions)

    def _express_url(
        self, url: str, compositions: Mapping
    ) -> Optional[Union[LISSymbol, ISOCSymbol, F08Symbol, F90Symbol]]:
        """"""

        if url not in compositions:
            # do we want to raise an Exception here? The url just doesn't exist.
            return None

        # NOTE could this be made factory functions in the modules?

        if "cptr" in url:
            if not self._has_cptr():
                return None

        if "embiggen" in url:
            if not self._has_embiggenment():
                return None

            return compositions[url](self._parseset, SUFFIX)

        return compositions[url](self._parseset)

    @property
    def lis(self) -> LISSymbol:
        """Access the LIS language procedure object."""

        return self._express_composition("lis", _VALID_LIS_COMPOSITIONS)

    @property
    def iso_c(self) -> ISOCSymbol:
        """Access the C language procedure object."""

        return self._express_composition("iso_c", _VALID_ISO_C_COMPOSITIONS)

    @property
    def f08(self) -> F08Symbol:
        """Access the F08 language procedure object."""

        return self._express_composition("f08", _VALID_F08_COMPOSITIONS)

    @property
    def f90(self) -> F90Symbol:
        """Access the F90 language procedure object."""

        return self._express_composition("f90", _VALID_F90_COMPOSITIONS)

    @property
    def embiggen(self) -> "Expression":
        """Add _embiggen_ to the expression."""

        self._properties["embiggen"] = True

        return self

    @property
    def profile(self) -> "Expression":
        """Add _profile_ to the expression."""

        self._properties["profile"] = True

        return self

    @property
    def cptr(self) -> "Expression":
        """Add _cptr_ to the expression."""

        self._properties["cptr"] = True

        return self


class Expressions(Expression):
    """"""

    @property
    def embiggen(self) -> Expression:
        """Add _embiggen_ to the expression."""

        return Expression(self._parseset, self._symbol).embiggen

    @property
    def profile(self) -> Expression:
        """Add _profile_ to the expression."""

        return Expression(self._parseset, self._symbol).profile

    @property
    def cptr(self) -> Expression:
        """Add _cptr_ to the expression."""

        return Expression(self._parseset, self._symbol).cptr
