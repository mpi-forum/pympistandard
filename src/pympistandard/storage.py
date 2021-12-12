"""
This module serves as the central storage of input objects.
"""


__all__ = ["KINDS", "PROCEDURES", "CALLBACKS", "PREDEFINED_FUNCTIONS", "CONSTANTS"]


from typing import MutableMapping


from .namespace import NamespaceDict


KINDS = NamespaceDict()
PROCEDURES: MutableMapping[str, "Procedure"] = NamespaceDict()
CALLBACKS = NamespaceDict()
PREDEFINED_FUNCTIONS = NamespaceDict()

CONSTANTS = NamespaceDict()
# to support this the Python DSL in the MPI Standard needs to be extended
# and all the constants need to be encoded (name, type, value if given)

def clear_storage():
    KINDS.clear()
    PROCEDURES.clear()
    CALLBACKS.clear()
    PREDEFINED_FUNCTIONS.clear()
    CONSTANTS.clear()
