"""
This module implements the Namespace class.
"""


from typing import Any, Union
from collections import UserDict


def _clean_name(name: str) -> str:
    """Standardize name from 'MPI_Name' to 'mpi_name'."""

    return name.lower()


class NamespaceDict(UserDict):  # pylint: disable=too-many-ancestors
    """
    The NamespaceDict class gives the interface of a dictionary with the addition
    of an attribute access like a SimpleNamespace.
    """

    def __getattr__(self, name: str) -> Any:
        """Get by attribute/dot notation."""

        name = _clean_name(name)

        if name not in self.data:
            raise AttributeError(f"'{name}' not present in NamespaceDict.")

        return self.data[name]

    def __getitem__(self, name: str) -> Any:
        """Get by dict access."""

        name = _clean_name(name)

        return self.data[name]

    def __contains__(self, name: Union[str, Any]) -> bool:
        """Check if a named Procedure is available."""

        name = _clean_name(name)

        return name in self.data or name in self.data.values()
