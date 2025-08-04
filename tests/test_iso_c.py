"""
This module contains tests related to the ISO C expressions.
"""


# pylint: disable=redefined-outer-name, unused-argument


# import pytest
# 
# 
# from typing import Mapping
# 
# 
# from pympistandard.storage import PROCEDURES
# from pympistandard.isoc import ISOCSymbol
# 
# 
# @pytest.mark.parametrize(
#     "procedure_name, expected", [("MPI_Procedure_name", "ISO_C_RETURN MPI_Procedure_name(void)")]
# )
# def test_iso_c_symbol_string_representation(procedure_name: str, expected: str) -> None:
#     """Test the expression of a ISOCSymbol."""
# 
#     procedure = PROCEDURES[procedure_name]
#     iso_c_procedure = procedure.express.iso_c
# 
#     assert str(iso_c_procedure) == expected
# 
# 
# @pytest.mark.parametrize(
#         "kind_name, expected", [("ARGUMENT_LIST", 3)]
#         )
# def test_pointer_expression(kind_name: str, expected: str) -> None:
#     """Tests whether the pointer expression of a kind with ISO C is correct."""
# 
#     raise NotImplementedError

def test_iso_c_embiggen_profiling(bundled_dataset):
    mpi_send = bundled_dataset.PROCEDURES.mpi_send

    assert mpi_send.express.embiggen.profile.iso_c.name == "PMPI_Send_c"

