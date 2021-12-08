"""
"""


from .symbol import Symbol


class Procedure(Symbol):
    """The Procedure class holds all information for a single MPI procedure.

    The Procedure class is responsible for containing all language agnostic
    information written by the MPI Forum and providing the information to
    tools which emit either source code or documentation.
    """

    def has_proxy_render(self) -> bool:
        """Get the proxy rendering property. With a proxy rendering for Fortran 2008 a text blurb
        is used."""

        return self._parseset["attributes"]["proxy_render"]

    def has_embiggenment(self) -> bool:
        """Get whether this Procedure has an embiggenment."""

        # NOTE can we remove this?
        #      it is a RTTI which python already has

        return any(
            parameter["kind"].startswith("POLY") for parameter in self._parseset["parameters"]
        ) or self._parseset["return_kind"].startswith("POLY")


#     @property
#     def introduced(self) -> Version:
#         """Get Version object of when the procedure was introduced into the Standard."""

#         raise NotImplementedError

#    @property
#    def initializing(self) -> bool:
#        pass

#    @property
#    def starting(self) -> bool:
#        pass

#    @property
#    def completing(self) -> bool:
#        pass

#    @property
#    def freeing(self) -> bool:
#        pass
