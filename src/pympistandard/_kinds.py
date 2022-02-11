"""
This module contains all kinds as dataclasses.
"""


from .kind import Kind, PolyKind, CPTRKind

BUFFER = Kind(
    name="BUFFER",
    _lis="choice",
    _iso_c_small="void",
    _f90_small="<type>",
    _f08_small="TYPE(*), DIMENSION(..)",
)
"""The BUFFER Kind is used in various places and acts like this."""

C_BUFFER = CPTRKind(
    name="C_BUFFER",
    _lis="choice",
    _iso_c_small="void",
    _f90_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
    _f08_small="TYPE(C_PTR)",
    _f90_cptr="TYPE(C_PTR)",
)
C_BUFFER2 = Kind(
    name="C_BUFFER2", _lis="choice", _iso_c_small="void", _f90_small="<type>", _f08_small="TYPE(C_PTR)"
)
C_BUFFER3 = Kind(
    name="C_BUFFER3",
    _lis=None,
    _iso_c_small="void",
    _f90_small="<TYPE>",
    _f08_small="TYPE(C_PTR), VALUE",
)
C_BUFFER4 = Kind(
    name="C_BUFFER4",
    _lis=None,
    _iso_c_small="void",
    _f90_small="<type>",
    _f08_small="TYPE(C_PTR), VALUE",
)
EXTRA_STATE = Kind(
    name="EXTRA_STATE",
    _lis=None,
    _iso_c_small="void",
    _f90_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
    _f08_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
)
EXTRA_STATE2 = Kind(
    name="EXTRA_STATE2", _lis=None, _iso_c_small="void", _f90_small="INTEGER", _f08_small="INTEGER"
)
FUNCTION_SMALL = Kind(
    name="FUNCTION_SMALL",
    _lis="function",
    _iso_c_small=None,
    _f90_small="EXTERNAL",
    _f08_small="PROCEDURE",
)
FUNCTION = Kind(
    name="FUNCTION", _lis="function", _iso_c_small=None, _f90_small="EXTERNAL", _f08_small="PROCEDURE"
)
POLYFUNCTION = PolyKind(
    name="POLYFUNCTION",
    _lis="function",
    _iso_c_small=None,
    _f90_small="EXTERNAL",
    _f08_small="PROCEDURE",
    _iso_c_large=None,
    _f08_large="PROCEDURE",
)
EVENT_CB_FUNCTION = Kind(
    name="EVENT_CB_FUNCTION",
    _lis="function",
    _iso_c_small="MPI_T_event_cb_function",
    _f90_small=None,
    _f08_small=None,
)
EVENT_FREE_CB_FUNCTION = Kind(
    name="EVENT_FREE_CB_FUNCTION",
    _lis="function",
    _iso_c_small="MPI_T_event_free_cb_function",
    _f90_small=None,
    _f08_small=None,
)
EVENT_DROP_CB_FUNCTION = Kind(
    name="EVENT_DROP_CB_FUNCTION",
    _lis="function",
    _iso_c_small="MPI_T_event_dropped_cb_function",
    _f90_small=None,
    _f08_small=None,
)
STRING = Kind(
    name="STRING",
    _lis="string",
    _iso_c_small="char",
    _f90_small="CHARACTER*(*)",
    _f08_small="CHARACTER",
)
STRING_ARRAY = Kind(
    name="STRING_ARRAY",
    _lis="array of strings",
    _iso_c_small="char",
    _f90_small="CHARACTER*(*)",
    _f08_small="CHARACTER",
)
STRING_2DARRAY = Kind(
    name="STRING_2DARRAY",
    _lis="array of array of strings",
    _iso_c_small="char",
    _f90_small="CHARACTER*(*)",
    _f08_small="CHARACTER",
)
ARGUMENT_COUNT = Kind(
    name="ARGUMENT_COUNT", _lis=None, _iso_c_small="int", _f90_small=None, _f08_small=None
)
ARGUMENT_LIST = Kind(
    name="ARGUMENT_LIST", _lis=None, _iso_c_small="char", _f90_small=None, _f08_small=None
)
ARRAY_LENGTH = Kind(
    name="ARRAY_LENGTH", _lis="integer", _iso_c_small="int", _f90_small="INTEGER", _f08_small="INTEGER"
)
ARRAY_LENGTH_NNI = Kind(
    name="ARRAY_LENGTH_NNI",
    _lis="non-negative integer",
    _iso_c_small="int",
    _f90_small="INTEGER",
    _f08_small="INTEGER",
)
ARRAY_LENGTH_PI = Kind(
    name="ARRAY_LENGTH_PI",
    _lis="positive integer",
    _iso_c_small="int",
    _f90_small="INTEGER",
    _f08_small="INTEGER",
)
ATTRIBUTE_VAL_10 = Kind(
    name="ATTRIBUTE_VAL_10", _lis=None, _iso_c_small="void", _f90_small="INTEGER", _f08_small="INTEGER"
)
ATTRIBUTE_VAL = Kind(
    name="ATTRIBUTE_VAL",
    _lis=None,
    _iso_c_small="void",
    _f90_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
    _f08_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
)
BLOCKLENGTH = Kind(
    name="BLOCKLENGTH",
    _lis="non-negative integer",
    _iso_c_small="int",
    _f90_small="INTEGER",
    _f08_small="INTEGER",
)
COLOR = Kind(
    name="COLOR", _lis="integer", _iso_c_small="int", _f90_small="INTEGER", _f08_small="INTEGER"
)
COORDINATE = Kind(
    name="COORDINATE", _lis="integer", _iso_c_small="int", _f90_small="INTEGER", _f08_small="INTEGER"
)
COORDINATE_NNI = Kind(
    name="COORDINATE_NNI",
    _lis="non-negative integer",
    _iso_c_small="int",
    _f90_small="INTEGER",
    _f08_small="INTEGER",
)
DEGREE = Kind(
    name="DEGREE",
    _lis="non-negative integer",
    _iso_c_small="int",
    _f90_small="INTEGER",
    _f08_small="INTEGER",
)
DIMENSION = Kind(
    name="DIMENSION", _lis="integer", _iso_c_small="int", _f90_small="INTEGER", _f08_small="INTEGER"
)
ENUM = Kind(name="ENUM", _lis="integer", _iso_c_small="int", _f90_small="INTEGER", _f08_small="INTEGER")
FILE_DESCRIPTOR = Kind(
    name="FILE_DESCRIPTOR",
    _lis="integer",
    _iso_c_small="int",
    _f90_small="INTEGER",
    _f08_small="INTEGER",
)
KEY = Kind(name="KEY", _lis="integer", _iso_c_small="int", _f90_small="INTEGER", _f08_small="INTEGER")
KEYVAL = Kind(
    name="KEYVAL", _lis="integer", _iso_c_small="int", _f90_small="INTEGER", _f08_small="INTEGER"
)
INDEX = Kind(
    name="INDEX", _lis="integer", _iso_c_small="int", _f90_small="INTEGER", _f08_small="INTEGER"
)
LOGICAL = Kind(
    name="LOGICAL", _lis="logical", _iso_c_small="int", _f90_small="LOGICAL", _f08_small="LOGICAL"
)
LOGICAL_OPTIONAL = Kind(
    name="LOGICAL_OPTIONAL", _lis="integer", _iso_c_small="int", _f90_small=None, _f08_small=None
)
LOGICAL_BOOLEAN = Kind(
    name="LOGICAL_BOOLEAN",
    _lis="boolean",
    _iso_c_small="int",
    _f90_small="LOGICAL",
    _f08_small="LOGICAL",
)
MATH = Kind(name="MATH", _lis="integer", _iso_c_small="int", _f90_small="INTEGER", _f08_small="INTEGER")
NUM_DIMS = Kind(
    name="NUM_DIMS", _lis="integer", _iso_c_small="int", _f90_small="INTEGER", _f08_small="INTEGER"
)
RANK = Kind(name="RANK", _lis="integer", _iso_c_small="int", _f90_small="INTEGER", _f08_small="INTEGER")
RANK_NNI = Kind(
    name="RANK_NNI",
    _lis="non-negative integer",
    _iso_c_small="int",
    _f90_small="INTEGER",
    _f08_small="INTEGER",
)
COMM_SIZE = Kind(
    name="COMM_SIZE", _lis="integer", _iso_c_small="int", _f90_small="INTEGER", _f08_small="INTEGER"
)
COMM_SIZE_PI = Kind(
    name="COMM_SIZE_PI",
    _lis="positive integer",
    _iso_c_small="int",
    _f90_small="INTEGER",
    _f08_small="INTEGER",
)
STRING_LENGTH = Kind(
    name="STRING_LENGTH", _lis="integer", _iso_c_small="int", _f90_small="INTEGER", _f08_small="INTEGER"
)
STRIDE_BYTES = Kind(
    name="STRIDE_BYTES",
    _lis="integer",
    _iso_c_small="MPI_Aint",
    _f90_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
    _f08_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
)
STRIDE_ELEM = Kind(
    name="STRIDE_ELEM", _lis="integer", _iso_c_small="int", _f90_small="INTEGER", _f08_small="INTEGER"
)
TAG = Kind(name="TAG", _lis="integer", _iso_c_small="int", _f90_small="INTEGER", _f08_small="INTEGER")
VERSION = Kind(
    name="VERSION", _lis="integer", _iso_c_small="int", _f90_small="INTEGER", _f08_small="INTEGER"
)
WEIGHT = Kind(
    name="WEIGHT",
    _lis="non-negative integer",
    _iso_c_small="int",
    _f90_small="INTEGER",
    _f08_small="INTEGER",
)
OFFSET = Kind(
    name="OFFSET",
    _lis="integer",
    _iso_c_small="MPI_Offset",
    _f90_small="INTEGER(KIND=MPI_OFFSET_KIND)",
    _f08_small="INTEGER(KIND=MPI_OFFSET_KIND)",
)
PROFILE_LEVEL = Kind(
    name="PROFILE_LEVEL", _lis="integer", _iso_c_small="int", _f90_small="INTEGER", _f08_small="INTEGER"
)
ASSERT = Kind(
    name="ASSERT", _lis="integer", _iso_c_small="int", _f90_small="INTEGER", _f08_small="INTEGER"
)
WINDOW_SIZE = Kind(
    name="WINDOW_SIZE",
    _lis="non-negative integer",
    _iso_c_small="MPI_Aint",
    _f90_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
    _f08_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
)
INFO_VALUE_LENGTH = Kind(
    name="INFO_VALUE_LENGTH",
    _lis="integer",
    _iso_c_small="int",
    _f90_small="INTEGER",
    _f08_small="INTEGER",
)
ACCESS_MODE = Kind(
    name="ACCESS_MODE", _lis="integer", _iso_c_small="int", _f90_small="INTEGER", _f08_small="INTEGER"
)
KEY_INDEX = Kind(
    name="KEY_INDEX", _lis="integer", _iso_c_small="int", _f90_small="INTEGER", _f08_small="INTEGER"
)
TOOLENUM_INDEX = Kind(
    name="TOOLENUM_INDEX", _lis="integer", _iso_c_small="int", _f90_small=None, _f08_small=None
)
TOOLENUM_SIZE = Kind(
    name="TOOLENUM_SIZE", _lis="integer", _iso_c_small="int", _f90_small=None, _f08_small=None
)
TOOL_VAR_VERBOSITY = Kind(
    name="TOOL_VAR_VERBOSITY", _lis="integer", _iso_c_small="int", _f90_small=None, _f08_small=None
)
TOOL_VAR_VALUE = Kind(
    name="TOOL_VAR_VALUE", _lis="integer", _iso_c_small="int", _f90_small=None, _f08_small=None
)
CVAR_INDEX = Kind(
    name="CVAR_INDEX", _lis="integer", _iso_c_small="int", _f90_small=None, _f08_small=None
)
CVAR_INDEX_SPECIAL = Kind(
    name="CVAR_INDEX_SPECIAL", _lis="index", _iso_c_small="int", _f90_small=None, _f08_small=None
)
PVAR_INDEX = Kind(
    name="PVAR_INDEX", _lis="integer", _iso_c_small="int", _f90_small=None, _f08_small=None
)
PVAR_CLASS = Kind(
    name="PVAR_CLASS", _lis="integer", _iso_c_small="int", _f90_small=None, _f08_small=None
)
SOURCE_INDEX = Kind(
    name="SOURCE_INDEX", _lis="integer", _iso_c_small="int", _f90_small=None, _f08_small=None
)
EVENT_INDEX = Kind(
    name="EVENT_INDEX", _lis="integer", _iso_c_small="int", _f90_small=None, _f08_small=None
)
CAT_INDEX = Kind(name="CAT_INDEX", _lis="integer", _iso_c_small="int", _f90_small=None, _f08_small=None)
UPDATE_NUMBER = Kind(
    name="UPDATE_NUMBER", _lis="integer", _iso_c_small="int", _f90_small=None, _f08_small=None
)
DROPPED_COUNT = Kind(
    name="DROPPED_COUNT",
    _lis="positive integer",
    _iso_c_small="MPI_Count",
    _f90_small=None,
    _f08_small=None,
)
TYPECLASS_SIZE = Kind(
    name="TYPECLASS_SIZE",
    _lis="integer",
    _iso_c_small="int",
    _f90_small="INTEGER",
    _f08_small="INTEGER",
)
GENERIC_DTYPE_INT = Kind(
    name="GENERIC_DTYPE_INT",
    _lis="integer",
    _iso_c_small="int",
    _f90_small="INTEGER",
    _f08_small="INTEGER",
)
GENERIC_DTYPE_COUNT = Kind(
    name="GENERIC_DTYPE_COUNT",
    _lis="integer",
    _iso_c_small="MPI_Count",
    _f90_small="INTEGER(KIND=MPI_COUNT_KIND)",
    _f08_small="INTEGER(KIND=MPI_COUNT_KIND)",
)
PROCESS_GRID_SIZE = Kind(
    name="PROCESS_GRID_SIZE",
    _lis="positive integer",
    _iso_c_small="int",
    _f90_small="INTEGER",
    _f08_small="INTEGER",
)
DTYPE_DISTRIBUTION = Kind(
    name="DTYPE_DISTRIBUTION",
    _lis="positive integer",
    _iso_c_small="int",
    _f90_small="INTEGER",
    _f08_small="INTEGER",
)
ALLOC_MEM_NUM_BYTES = Kind(
    name="ALLOC_MEM_NUM_BYTES",
    _lis="non-negative integer",
    _iso_c_small="MPI_Aint",
    _f90_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
    _f08_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
)
PACK_EXTERNAL_SIZE = Kind(
    name="PACK_EXTERNAL_SIZE",
    _lis="integer",
    _iso_c_small="MPI_Aint",
    _f90_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
    _f08_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
)
WIN_ATTACH_SIZE = Kind(
    name="WIN_ATTACH_SIZE",
    _lis="non-negative integer",
    _iso_c_small="MPI_Aint",
    _f90_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
    _f08_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
)
DISPLACEMENT_SMALL = Kind(
    name="DISPLACEMENT_SMALL",
    _lis="integer",
    _iso_c_small="int",
    _f90_small="INTEGER",
    _f08_small="INTEGER",
)
DISPLACEMENT = Kind(
    name="DISPLACEMENT",
    _lis="integer",
    _iso_c_small="MPI_Aint",
    _f90_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
    _f08_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
)
DISPLACEMENT_NNI = Kind(
    name="DISPLACEMENT_NNI",
    _lis="non-negative integer",
    _iso_c_small="MPI_Aint",
    _f90_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
    _f08_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
)
POLYDISPLACEMENT = PolyKind(
    name="POLYDISPLACEMENT",
    _lis="integer",
    _iso_c_small="int",
    _f90_small="INTEGER",
    _f08_small="INTEGER",
    _iso_c_large="MPI_Aint",
    _f08_large="INTEGER(KIND=MPI_ADDRESS_KIND)",
)
NUM_BYTES_SMALL = Kind(
    name="NUM_BYTES_SMALL",
    _lis="integer",
    _iso_c_small="int",
    _f90_small="INTEGER",
    _f08_small="INTEGER",
)
NUM_BYTES = Kind(
    name="NUM_BYTES",
    _lis="integer",
    _iso_c_small="MPI_Count",
    _f90_small="INTEGER(KIND=MPI_COUNT_KIND)",
    _f08_small="INTEGER(KIND=MPI_COUNT_KIND)",
)
NUM_BYTES_NNI_SMALL = Kind(
    name="NUM_BYTES_NNI_SMALL",
    _lis="non-negative integer",
    _iso_c_small="int",
    _f90_small="INTEGER",
    _f08_small="INTEGER",
)
NUM_BYTES_NNI = Kind(
    name="NUM_BYTES_NNI",
    _lis="non-negative integer",
    _iso_c_small="MPI_Count",
    _f90_small="INTEGER(KIND=MPI_COUNT_KIND)",
    _f08_small="INTEGER(KIND=MPI_COUNT_KIND)",
)
ERROR_CODE = Kind(
    name="ERROR_CODE", _lis="integer", _iso_c_small="int", _f90_small="INTEGER", _f08_small="INTEGER"
)
ERROR_CODE_SHOW_INTENT = Kind(
    name="ERROR_CODE_SHOW_INTENT",
    _lis="integer",
    _iso_c_small="int",
    _f90_small="INTEGER",
    _f08_small="INTEGER",
)
ERROR_CLASS = Kind(
    name="ERROR_CLASS", _lis="integer", _iso_c_small="int", _f90_small="INTEGER", _f08_small="INTEGER"
)
ORDER = Kind(name="ORDER", _lis="state", _iso_c_small="int", _f90_small="INTEGER", _f08_small="INTEGER")
THREAD_LEVEL = Kind(
    name="THREAD_LEVEL", _lis="integer", _iso_c_small="int", _f90_small="INTEGER", _f08_small="INTEGER"
)
COMBINER = Kind(
    name="COMBINER", _lis="state", _iso_c_small="int", _f90_small="INTEGER", _f08_small="INTEGER"
)
LOCK_TYPE = Kind(
    name="LOCK_TYPE", _lis="state", _iso_c_small="int", _f90_small="INTEGER", _f08_small="INTEGER"
)
TOOLS_ENUM = Kind(
    name="TOOLS_ENUM", _lis="handle", _iso_c_small="MPI_T_enum", _f90_small=None, _f08_small=None
)
UPDATE_MODE = Kind(
    name="UPDATE_MODE", _lis="state", _iso_c_small="int", _f90_small="INTEGER", _f08_small="INTEGER"
)
BIND_TYPE = Kind(name="BIND_TYPE", _lis="integer", _iso_c_small="int", _f90_small=None, _f08_small=None)
SOURCE_ORDERING = Kind(
    name="SOURCE_ORDERING",
    _lis="integer",
    _iso_c_small="MPI_T_source_order",
    _f90_small=None,
    _f08_small=None,
)
CALLBACK_SAFETY = Kind(
    name="CALLBACK_SAFETY",
    _lis="integer",
    _iso_c_small="MPI_T_cb_safety",
    _f90_small=None,
    _f08_small=None,
)
VARIABLE_SCOPE = Kind(
    name="VARIABLE_SCOPE", _lis="integer", _iso_c_small="int", _f90_small=None, _f08_small=None
)
TYPECLASS = Kind(
    name="TYPECLASS", _lis="integer", _iso_c_small="int", _f90_small="INTEGER", _f08_small="INTEGER"
)
GROUP_COMPARISON = Kind(
    name="GROUP_COMPARISON",
    _lis="integer",
    _iso_c_small="int",
    _f90_small="INTEGER",
    _f08_small="INTEGER",
)
COMM_COMPARISON = Kind(
    name="COMM_COMPARISON",
    _lis="integer",
    _iso_c_small="int",
    _f90_small="INTEGER",
    _f08_small="INTEGER",
)
SPLIT_TYPE = Kind(
    name="SPLIT_TYPE", _lis="integer", _iso_c_small="int", _f90_small="INTEGER", _f08_small="INTEGER"
)
TOPOLOGY_TYPE = Kind(
    name="TOPOLOGY_TYPE", _lis="state", _iso_c_small="int", _f90_small="INTEGER", _f08_small="INTEGER"
)
DISTRIB_ENUM = Kind(
    name="DISTRIB_ENUM", _lis="state", _iso_c_small="int", _f90_small="INTEGER", _f08_small="INTEGER"
)
RMA_DISPLACEMENT_SMALL = Kind(
    name="RMA_DISPLACEMENT_SMALL",
    _lis="positive integer",
    _iso_c_small="int",
    _f90_small="INTEGER",
    _f08_small="INTEGER",
)
RMA_DISPLACEMENT = Kind(
    name="RMA_DISPLACEMENT",
    _lis="positive integer",
    _iso_c_small="MPI_Aint",
    _f90_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
    _f08_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
)
POLYRMA_DISPLACEMENT = PolyKind(
    name="POLYRMA_DISPLACEMENT",
    _lis="positive integer",
    _iso_c_small="int",
    _f90_small="INTEGER",
    _f08_small="INTEGER",
    _iso_c_large="MPI_Aint",
    _f08_large="INTEGER(KIND=MPI_ADDRESS_KIND)",
)
RMA_DISPLACEMENT_NNI_SMALL = Kind(
    name="RMA_DISPLACEMENT_NNI_SMALL",
    _lis="non-negative integer",
    _iso_c_small="int",
    _f90_small="INTEGER",
    _f08_small="INTEGER",
)
RMA_DISPLACEMENT_NNI = Kind(
    name="RMA_DISPLACEMENT_NNI",
    _lis="non-negative integer",
    _iso_c_small="MPI_Aint",
    _f90_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
    _f08_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
)
POLYRMA_DISPLACEMENT_NNI = PolyKind(
    name="POLYRMA_DISPLACEMENT_NNI",
    _lis="non-negative integer",
    _iso_c_small="int",
    _f90_small="INTEGER",
    _f08_small="INTEGER",
    _iso_c_large="MPI_Aint",
    _f08_large="INTEGER(KIND=MPI_ADDRESS_KIND)",
)
DISPOFFSET_SMALL = Kind(
    name="DISPOFFSET_SMALL",
    _lis="integer",
    _iso_c_small="MPI_Aint",
    _f90_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
    _f08_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
)
DISPOFFSET = Kind(
    name="DISPOFFSET",
    _lis="integer",
    _iso_c_small="MPI_Count",
    _f90_small="INTEGER(KIND=MPI_COUNT_KIND)",
    _f08_small="INTEGER(KIND=MPI_COUNT_KIND)",
)
POLYDISPOFFSET = PolyKind(
    name="POLYDISPOFFSET",
    _lis="integer",
    _iso_c_small="MPI_Aint",
    _f90_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
    _f08_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
    _iso_c_large="MPI_Count",
    _f08_large="INTEGER(KIND=MPI_COUNT_KIND)",
)
DTYPE_NUM_ELEM_NNI_SMALL = Kind(
    name="DTYPE_NUM_ELEM_NNI_SMALL",
    _lis="non-negative integer",
    _iso_c_small="int",
    _f90_small="INTEGER",
    _f08_small="INTEGER",
)
DTYPE_NUM_ELEM_NNI = Kind(
    name="DTYPE_NUM_ELEM_NNI",
    _lis="non-negative integer",
    _iso_c_small="MPI_Count",
    _f90_small="INTEGER(KIND=MPI_COUNT_KIND)",
    _f08_small="INTEGER(KIND=MPI_COUNT_KIND)",
)
POLYDTYPE_NUM_ELEM_NNI = PolyKind(
    name="POLYDTYPE_NUM_ELEM_NNI",
    _lis="non-negative integer",
    _iso_c_small="int",
    _f90_small="INTEGER",
    _f08_small="INTEGER",
    _iso_c_large="MPI_Count",
    _f08_large="INTEGER(KIND=MPI_COUNT_KIND)",
)
DTYPE_NUM_ELEM_SMALL = Kind(
    name="DTYPE_NUM_ELEM_SMALL",
    _lis="integer",
    _iso_c_small="int",
    _f90_small="INTEGER",
    _f08_small="INTEGER",
)
DTYPE_NUM_ELEM = Kind(
    name="DTYPE_NUM_ELEM",
    _lis="integer",
    _iso_c_small="MPI_Count",
    _f90_small="INTEGER(KIND=MPI_COUNT_KIND)",
    _f08_small="INTEGER(KIND=MPI_COUNT_KIND)",
)
POLYDTYPE_NUM_ELEM = PolyKind(
    name="POLYDTYPE_NUM_ELEM",
    _lis="integer",
    _iso_c_small="int",
    _f90_small="INTEGER",
    _f08_small="INTEGER",
    _iso_c_large="MPI_Count",
    _f08_large="INTEGER(KIND=MPI_COUNT_KIND)",
)
DTYPE_NUM_ELEM_PI_SMALL = Kind(
    name="DTYPE_NUM_ELEM_PI_SMALL",
    _lis="positive integer",
    _iso_c_small="int",
    _f90_small="INTEGER",
    _f08_small="INTEGER",
)
DTYPE_NUM_ELEM_PI = Kind(
    name="DTYPE_NUM_ELEM_PI",
    _lis="positive integer",
    _iso_c_small="MPI_Count",
    _f90_small="INTEGER(KIND=MPI_COUNT_KIND)",
    _f08_small="INTEGER(KIND=MPI_COUNT_KIND)",
)
POLYDTYPE_NUM_ELEM_PI = PolyKind(
    name="POLYDTYPE_NUM_ELEM_PI",
    _lis="positive integer",
    _iso_c_small="int",
    _f90_small="INTEGER",
    _f08_small="INTEGER",
    _iso_c_large="MPI_Count",
    _f08_large="INTEGER(KIND=MPI_COUNT_KIND)",
)
DTYPE_STRIDE_BYTES_SMALL = Kind(
    name="DTYPE_STRIDE_BYTES_SMALL",
    _lis="integer",
    _iso_c_small="MPI_Aint",
    _f90_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
    _f08_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
)
DTYPE_STRIDE_BYTES = Kind(
    name="DTYPE_STRIDE_BYTES",
    _lis="integer",
    _iso_c_small="MPI_Count",
    _f90_small="INTEGER(KIND=MPI_COUNT_KIND)",
    _f08_small="INTEGER(KIND=MPI_COUNT_KIND)",
)
POLYDTYPE_STRIDE_BYTES = PolyKind(
    name="POLYDTYPE_STRIDE_BYTES",
    _lis="integer",
    _iso_c_small="MPI_Aint",
    _f90_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
    _f08_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
    _iso_c_large="MPI_Count",
    _f08_large="INTEGER(KIND=MPI_COUNT_KIND)",
)
DISPLACEMENT_COUNT_SMALL = Kind(
    name="DISPLACEMENT_COUNT_SMALL",
    _lis="integer",
    _iso_c_small="int",
    _f90_small="INTEGER",
    _f08_small="INTEGER",
)
DISPLACEMENT_COUNT = Kind(
    name="DISPLACEMENT_COUNT",
    _lis="integer",
    _iso_c_small="MPI_Count",
    _f90_small="INTEGER(KIND=MPI_COUNT_KIND)",
    _f08_small="INTEGER(KIND=MPI_COUNT_KIND)",
)
POLYDISPLACEMENT_COUNT = PolyKind(
    name="POLYDISPLACEMENT_COUNT",
    _lis="integer",
    _iso_c_small="int",
    _f90_small="INTEGER",
    _f08_small="INTEGER",
    _iso_c_large="MPI_Count",
    _f08_large="INTEGER(KIND=MPI_COUNT_KIND)",
)
DISPLACEMENT_AINT_COUNT_SMALL = Kind(
    name="DISPLACEMENT_AINT_COUNT_SMALL",
    _lis="integer",
    _iso_c_small="MPI_Aint",
    _f90_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
    _f08_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
)
DISPLACEMENT_AINT_COUNT = Kind(
    name="DISPLACEMENT_AINT_COUNT",
    _lis="integer",
    _iso_c_small="MPI_Count",
    _f90_small="INTEGER(KIND=MPI_COUNT_KIND)",
    _f08_small="INTEGER(KIND=MPI_COUNT_KIND)",
)
POLYDISPLACEMENT_AINT_COUNT = PolyKind(
    name="POLYDISPLACEMENT_AINT_COUNT",
    _lis="integer",
    _iso_c_small="MPI_Aint",
    _f90_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
    _f08_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
    _iso_c_large="MPI_Count",
    _f08_large="INTEGER(KIND=MPI_COUNT_KIND)",
)
DTYPE_PACK_SIZE_SMALL = Kind(
    name="DTYPE_PACK_SIZE_SMALL",
    _lis="integer",
    _iso_c_small="MPI_Aint",
    _f90_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
    _f08_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
)
DTYPE_PACK_SIZE = Kind(
    name="DTYPE_PACK_SIZE",
    _lis="integer",
    _iso_c_small="MPI_Count",
    _f90_small="INTEGER(KIND=MPI_COUNT_KIND)",
    _f08_small="INTEGER(KIND=MPI_COUNT_KIND)",
)
POLYDTYPE_PACK_SIZE = PolyKind(
    name="POLYDTYPE_PACK_SIZE",
    _lis="integer",
    _iso_c_small="MPI_Aint",
    _f90_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
    _f08_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
    _iso_c_large="MPI_Count",
    _f08_large="INTEGER(KIND=MPI_COUNT_KIND)",
)
LOCATION_SMALL = Kind(
    name="LOCATION_SMALL",
    _lis="integer",
    _iso_c_small="MPI_Aint",
    _f90_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
    _f08_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
)
LOCATION = Kind(
    name="LOCATION",
    _lis="integer",
    _iso_c_small="MPI_Count",
    _f90_small="INTEGER(KIND=MPI_COUNT_KIND)",
    _f08_small="INTEGER(KIND=MPI_COUNT_KIND)",
)
POLYLOCATION = PolyKind(
    name="POLYLOCATION",
    _lis="integer",
    _iso_c_small="MPI_Aint",
    _f90_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
    _f08_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
    _iso_c_large="MPI_Count",
    _f08_large="INTEGER(KIND=MPI_COUNT_KIND)",
)
TOOLS_NUM_ELEM_SMALL = Kind(
    name="TOOLS_NUM_ELEM_SMALL",
    _lis="integer",
    _iso_c_small="int",
    _f90_small="INTEGER",
    _f08_small="INTEGER",
)
TOOLS_NUM_ELEM = Kind(
    name="TOOLS_NUM_ELEM",
    _lis="integer",
    _iso_c_small="MPI_Count",
    _f90_small="INTEGER(KIND=MPI_COUNT_KIND)",
    _f08_small="INTEGER(KIND=MPI_COUNT_KIND)",
)
POLYTOOLS_NUM_ELEM = PolyKind(
    name="POLYTOOLS_NUM_ELEM",
    _lis="integer",
    _iso_c_small="int",
    _f90_small="INTEGER",
    _f08_small="INTEGER",
    _iso_c_large="MPI_Count",
    _f08_large="INTEGER(KIND=MPI_COUNT_KIND)",
)
TOOLS_TICK_COUNT = Kind(
    name="TOOLS_TICK_COUNT", _lis="integer", _iso_c_small="MPI_Count", _f90_small=None, _f08_small=None
)
POLYNUM_BYTES = PolyKind(
    name="POLYNUM_BYTES",
    _lis="integer",
    _iso_c_small="int",
    _f90_small="INTEGER",
    _f08_small="INTEGER",
    _iso_c_large="MPI_Count",
    _f08_large="INTEGER(KIND=MPI_COUNT_KIND)",
)
POLYNUM_BYTES_NNI = PolyKind(
    name="POLYNUM_BYTES_NNI",
    _lis="non-negative integer",
    _iso_c_small="int",
    _f90_small="INTEGER",
    _f08_small="INTEGER",
    _iso_c_large="MPI_Count",
    _f08_large="INTEGER(KIND=MPI_COUNT_KIND)",
)
XFER_NUM_ELEM_NNI_SMALL = Kind(
    name="XFER_NUM_ELEM_NNI_SMALL",
    _lis="non-negative integer",
    _iso_c_small="int",
    _f90_small="INTEGER",
    _f08_small="INTEGER",
)
XFER_NUM_ELEM_NNI = Kind(
    name="XFER_NUM_ELEM_NNI",
    _lis="non-negative integer",
    _iso_c_small="MPI_Count",
    _f90_small="INTEGER(KIND=MPI_COUNT_KIND)",
    _f08_small="INTEGER(KIND=MPI_COUNT_KIND)",
)
POLYXFER_NUM_ELEM_NNI = PolyKind(
    name="POLYXFER_NUM_ELEM_NNI",
    _lis="non-negative integer",
    _iso_c_small="int",
    _f90_small="INTEGER",
    _f08_small="INTEGER",
    _iso_c_large="MPI_Count",
    _f08_large="INTEGER(KIND=MPI_COUNT_KIND)",
)
XFER_NUM_ELEM_SMALL = Kind(
    name="XFER_NUM_ELEM_SMALL",
    _lis="integer",
    _iso_c_small="int",
    _f90_small="INTEGER",
    _f08_small="INTEGER",
)
XFER_NUM_ELEM = Kind(
    name="XFER_NUM_ELEM",
    _lis="integer",
    _iso_c_small="MPI_Count",
    _f90_small="INTEGER(KIND=MPI_COUNT_KIND)",
    _f08_small="INTEGER(KIND=MPI_COUNT_KIND)",
)
POLYXFER_NUM_ELEM = PolyKind(
    name="POLYXFER_NUM_ELEM",
    _lis="integer",
    _iso_c_small="int",
    _f90_small="INTEGER",
    _f08_small="INTEGER",
    _iso_c_large="MPI_Count",
    _f08_large="INTEGER(KIND=MPI_COUNT_KIND)",
)
NUM_PARAM_VALUES_SMALL = Kind(
    name="NUM_PARAM_VALUES_SMALL",
    _lis="non-negative integer",
    _iso_c_small="int",
    _f90_small="INTEGER",
    _f08_small="INTEGER",
)
POLYNUM_PARAM_VALUES = PolyKind(
    name="POLYNUM_PARAM_VALUES",
    _lis="non-negative integer",
    _iso_c_small="int",
    _f90_small="INTEGER",
    _f08_small="INTEGER",
    _iso_c_large="MPI_Count",
    _f08_large="INTEGER(KIND=MPI_COUNT_KIND)",
)
NUM_PARAM_VALUES = Kind(
    name="NUM_PARAM_VALUES",
    _lis="non-negative integer",
    _iso_c_small="MPI_Count",
    _f90_small="INTEGER(KIND=MPI_COUNT_KIND)",
    _f08_small="INTEGER(KIND=MPI_COUNT_KIND)",
)
PARTITION = Kind(
    name="PARTITION",
    _lis="non-negative integer",
    _iso_c_small="int",
    _f90_small="INTEGER",
    _f08_small="INTEGER",
)
COMMUNICATOR = Kind(
    name="COMMUNICATOR",
    _lis="handle",
    _iso_c_small="MPI_Comm",
    _f90_small="INTEGER",
    _f08_small="TYPE(MPI_Comm)",
)
DATATYPE = Kind(
    name="DATATYPE",
    _lis="handle",
    _iso_c_small="MPI_Datatype",
    _f90_small="INTEGER",
    _f08_small="TYPE(MPI_Datatype)",
)
ERRHANDLER = Kind(
    name="ERRHANDLER",
    _lis="handle",
    _iso_c_small="MPI_Errhandler",
    _f90_small="INTEGER",
    _f08_small="TYPE(MPI_Errhandler)",
)
FILE = Kind(
    name="FILE",
    _lis="handle",
    _iso_c_small="MPI_File",
    _f90_small="INTEGER",
    _f08_small="TYPE(MPI_File)",
)
GROUP = Kind(
    name="GROUP",
    _lis="handle",
    _iso_c_small="MPI_Group",
    _f90_small="INTEGER",
    _f08_small="TYPE(MPI_Group)",
)
INFO = Kind(
    name="INFO",
    _lis="handle",
    _iso_c_small="MPI_Info",
    _f90_small="INTEGER",
    _f08_small="TYPE(MPI_Info)",
)
MESSAGE = Kind(
    name="MESSAGE",
    _lis="handle",
    _iso_c_small="MPI_Message",
    _f90_small="INTEGER",
    _f08_small="TYPE(MPI_Message)",
)
REQUEST = Kind(
    name="REQUEST",
    _lis="handle",
    _iso_c_small="MPI_Request",
    _f90_small="INTEGER",
    _f08_small="TYPE(MPI_Request)",
)
SESSION = Kind(
    name="SESSION",
    _lis="handle",
    _iso_c_small="MPI_Session",
    _f90_small="INTEGER",
    _f08_small="TYPE(MPI_Session)",
)
STATUS = Kind(
    name="STATUS",
    _lis="status",
    _iso_c_small="MPI_Status",
    _f90_small="INTEGER",
    _f08_small="TYPE(MPI_Status)",
)
WINDOW = Kind(
    name="WINDOW",
    _lis="handle",
    _iso_c_small="MPI_Win",
    _f90_small="INTEGER",
    _f08_small="TYPE(MPI_Win)",
)
OPERATION = Kind(
    name="OPERATION",
    _lis="handle",
    _iso_c_small="MPI_Op",
    _f90_small="INTEGER",
    _f08_small="TYPE(MPI_Op)",
)
CVAR = Kind(
    name="CVAR", _lis="handle", _iso_c_small="MPI_T_cvar_handle", _f90_small=None, _f08_small=None
)
PVAR = Kind(
    name="PVAR", _lis="handle", _iso_c_small="MPI_T_pvar_handle", _f90_small=None, _f08_small=None
)
PVAR_SESSION = Kind(
    name="PVAR_SESSION",
    _lis="handle",
    _iso_c_small="MPI_T_pvar_session",
    _f90_small=None,
    _f08_small=None,
)
EVENT_REGISTRATION = Kind(
    name="EVENT_REGISTRATION",
    _lis="handle",
    _iso_c_small="MPI_T_event_registration",
    _f90_small=None,
    _f08_small=None,
)
EVENT_INSTANCE = Kind(
    name="EVENT_INSTANCE",
    _lis="handle",
    _iso_c_small="MPI_T_event_instance",
    _f90_small=None,
    _f08_small=None,
)
TOOL_MPI_OBJ = Kind(
    name="TOOL_MPI_OBJ", _lis="pointer", _iso_c_small="void", _f90_small=None, _f08_small=None
)
F90_STATUS = Kind(
    name="F90_STATUS",
    _lis="status",
    _iso_c_small="MPI_Fint",
    _f90_small="INTEGER",
    _f08_small="INTEGER",
)
F08_STATUS = Kind(
    name="F08_STATUS",
    _lis="status",
    _iso_c_small="MPI_F08_status",
    _f90_small="TYPE(MPI_Status)",
    _f08_small="TYPE(MPI_Status)",
)
F90_COMM = Kind(name="F90_COMM", _lis=None, _iso_c_small="MPI_Fint", _f90_small=None, _f08_small=None)
F90_DATATYPE = Kind(
    name="F90_DATATYPE", _lis=None, _iso_c_small="MPI_Fint", _f90_small=None, _f08_small=None
)
F90_GROUP = Kind(name="F90_GROUP", _lis=None, _iso_c_small="MPI_Fint", _f90_small=None, _f08_small=None)
F90_REQUEST = Kind(
    name="F90_REQUEST", _lis=None, _iso_c_small="MPI_Fint", _f90_small=None, _f08_small=None
)
F90_FILE = Kind(name="F90_FILE", _lis=None, _iso_c_small="MPI_Fint", _f90_small=None, _f08_small=None)
F90_WIN = Kind(name="F90_WIN", _lis=None, _iso_c_small="MPI_Fint", _f90_small=None, _f08_small=None)
F90_OP = Kind(name="F90_OP", _lis=None, _iso_c_small="MPI_Fint", _f90_small=None, _f08_small=None)
F90_INFO = Kind(name="F90_INFO", _lis=None, _iso_c_small="MPI_Fint", _f90_small=None, _f08_small=None)
F90_ERRHANDLER = Kind(
    name="F90_ERRHANDLER", _lis=None, _iso_c_small="MPI_Fint", _f90_small=None, _f08_small=None
)
F90_MESSAGE = Kind(
    name="F90_MESSAGE", _lis=None, _iso_c_small="MPI_Fint", _f90_small=None, _f08_small=None
)
F90_SESSION = Kind(
    name="F90_SESSION", _lis=None, _iso_c_small="MPI_Fint", _f90_small=None, _f08_small=None
)
VARARGS = Kind(name="VARARGS", _lis="\\ldots", _iso_c_small="\\ldots", _f90_small=None, _f08_small=None)
WALL_TIME = Kind(
    name="WALL_TIME",
    _lis=None,
    _iso_c_small="double",
    _f90_small="DOUBLE PRECISION",
    _f08_small="DOUBLE PRECISION",
)
TICK_RESOLUTION = Kind(
    name="TICK_RESOLUTION",
    _lis=None,
    _iso_c_small="double",
    _f90_small="DOUBLE PRECISION",
    _f08_small="DOUBLE PRECISION",
)
NOTHING = Kind(name="NOTHING", _lis=None, _iso_c_small="void", _f90_small=None, _f08_small=None)
