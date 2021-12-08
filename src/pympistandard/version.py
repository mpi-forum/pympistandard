"""
This module defines the Version class which is used to represent a version of the MPI Standard.
"""


class Version:
    """
    The Version class is used to hold the version number of the MPI Standard.
    """

    def __init__(self, major: int, minor: int) -> None:
        self._major = major
        self._minor = minor

    def __str__(self) -> str:
        """Get version string."""

        return f"{self.major}.{self.minor}"

    @property
    def major(self) -> int:
        """Get major version integer."""

        return self._major

    @property
    def minor(self) -> int:
        """Get minor version integer."""

        return self._minor
