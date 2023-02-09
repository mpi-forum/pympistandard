"""
This module provides all access to the MPI Standard Python API. Everything
below this level should be considered private.
"""


__all__ = ["PROCEDURES", "KINDS", "CALLBACKS", "PREDEFINED_FUNCTIONS", "CONSTANTS"]
__author__ = "Martin Ruefenacht"
__version__ = "0.1"


from pathlib import Path
import importlib.resources
import json
from enum import Enum
from typing import Union, Tuple, Optional
import logging
import os
import sys


MPI_DATABASE_FILE: str = "apis.json"


from .storage import KINDS, PROCEDURES, CALLBACKS, PREDEFINED_FUNCTIONS, clear_storage
from .parameter import Direction
from .procedure import Procedure
from .callback import Callback
from .predefined_function import PredefinedFunction
from .kind import Kind, PolyKind
from . import _kinds
from .export import export
from .lis import LISProcedure
from .isoc import (
    ISOCProcedure,
    EmbiggenedISOCProcedure,
    ISOCPredefinedFunction,
    EmbiggenedISOCPredefinedFunction,
    ISOCCallback,
    EmbiggenedISOCCallback,
)
from .f90 import F90Procedure, F90Callback, F90PredefinedFunction
from .f08 import (
    F08Procedure,
    EmbiggenedF08Procedure,
    F08Callback,
    EmbiggenedF08Callback,
    F08PredefinedFunction,
    EmbiggenedF08PredefinedFunction,
)


@export
def unload() -> None:
    """Unloads currently loaded Python API Interface and MPI Standard."""

    clear_storage()


# TODO rename to load(api_version, mpi_version, path)
@export
def use_api_version(
    version: Union[int, str] = "LATEST",
    given_path: Optional[Union[str, Path]] = None,
    force_bundled: bool = False,
) -> None:
    """Sets the Python API interface which the user expects to use."""

    unload()

    # load version of API
    if version in (1, "LATEST"):
        _register_kinds_v1()

        path = _resolve_path(given_path, force_bundled)
        _load_database_v1(path)

    else:
        raise RuntimeError("Valid versions of Python API are [1, LATEST].")


@export
def all_lis_procedures() -> Tuple[Procedure]:
    """Fetch all LIS expressible procedures available in the Standard."""

    return tuple(
        procedure
        for procedure in PROCEDURES.values()
        if procedure.express.lis is not None
    )


@export
def all_iso_c_procedures() -> Tuple[Procedure]:
    """Fetch all ISO C expressible procedures available in the Standard."""

    return tuple(
        procedure
        for procedure in PROCEDURES.values()
        if procedure.express.iso_c is not None
    )


@export
def all_f08_procedures() -> Tuple[Procedure]:
    """Fetch all F08 expressible procedures available in the Standard."""

    return tuple(
        procedure
        for procedure in PROCEDURES.values()
        if procedure.express.f08 is not None
    )


@export
def all_f90_procedures() -> Tuple[Procedure]:
    """Fetch all F90 expressible procedures available in the Standard."""

    return tuple(
        procedure
        for procedure in PROCEDURES.values()
        if procedure.express.f90 is not None
    )


def _register_kinds_v1() -> None:
    """
    Register all Kind instances found in the _kinds.py file in the KINDS variable.
    """

    for key, item in _kinds.__dict__.items():
        if isinstance(item, Kind):
            KINDS[key.lower()] = item


def _load_bundled_db():
    if sys.version_info.major == 3 and sys.version_info.minor < 9:
        with importlib.resources.path(
            "pympistandard.data", MPI_DATABASE_FILE
        ) as datapath:
            return datapath

    else:
        return importlib.resources.files("pympistandard.data").joinpath(
            MPI_DATABASE_FILE
        )


def _resolve_path(
    given_path: Optional[Union[str, Path]] = None, force_bundled: bool = False
) -> Path:
    """Find correct path to load apis.json from."""

    if force_bundled:
        path = _load_bundled_db()

    # convert str path to Path
    elif isinstance(given_path, str):
        given_path = Path(given_path)

    # use given path
    elif isinstance(given_path, Path):
        path = given_path / MPI_DATABASE_FILE

    # use environment variable paths
    elif "MPISTANDARD" in os.environ:
        path = Path(os.environ["MPISTANDARD"] + "/" + MPI_DATABASE_FILE)

    else:
        # fallback to packaged data
        path = _load_bundled_db()

    # require resolved path to exist
    path.resolve(True)

    return path


def _load_database_v1(path: Path) -> None:
    """
    Find and register all procedures found in the 'apis.json' file with Procedure instances.
    """

    with path.open("r") as datafile:
        if path.suffix == ".json":
            dataset = json.load(datafile)

        elif path.suffix == ".yaml":
            try:
                import yaml

                dataset = yaml.load(datafile)

            except Exception as error:
                print("yaml may not be installed")
                raise error

        else:
            raise RuntimeError(f"Unrecognized suffix of data file {path}")

        # read in datafile
        for name, desc in dataset.items():
            if desc["attributes"]["predefined_function"]:
                predef = PredefinedFunction(name, desc)
                PREDEFINED_FUNCTIONS[predef.name] = predef

            elif desc["attributes"]["callback"]:
                callback = Callback(name, desc)
                CALLBACKS[callback.name] = callback

            else:
                procedure = Procedure(name, desc)
                PROCEDURES[procedure.name] = procedure
