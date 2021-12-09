"""
This module contains test fixtures for the entire test suite.
"""


# pylint: disable=redefined-outer-name


import pytest


from pympistandard.storage import KINDS, PROCEDURES
from pympistandard.procedure import Procedure
from pympistandard.kind import Kind


@pytest.fixture(scope="session", autouse=True)
def dataset() -> None:
    """Creates the test parsesets required for all tests."""

    KINDS["return"] = Kind("RETURN", "LIS_RETURN", "ISO_C_RETURN", "F90_RETURN", "F08_RETURN")

    PROCEDURES["mpi_procedure_name"] = Procedure(
        "MPI_Procedure_name",
        {
            "name": "MPI_Procedure_name",
            "return_kind": "RETURN",
            "parameters": [],
            "attributes": {"c_expressible": True},
        },
    )
