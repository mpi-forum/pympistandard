"""
This module contains all kinds as dataclasses.
"""


from .kind import Kind, PolyKind, CPTRKind

BUFFER = Kind(
    name="BUFFER",
    lis="choice",
    iso_c_small="void",
    f90_small="<type>",
    f08_small="TYPE(*), DIMENSION(..)",
)
"""The BUFFER Kind is used in various places and acts like this."""

C_BUFFER = CPTRKind(
    name="C_BUFFER",
    lis="choice",
    iso_c_small="void",
    f90_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
    f08_small="TYPE(C_PTR)",
    f90_cptr="TYPE(C_PTR)",
)
C_BUFFER2 = Kind(
    name="C_BUFFER2", lis="choice", iso_c_small="void", f90_small="<type>", f08_small="TYPE(C_PTR)"
)
C_BUFFER3 = Kind(
    name="C_BUFFER3",
    lis=None,
    iso_c_small="void",
    f90_small="<TYPE>",
    f08_small="TYPE(C_PTR), VALUE",
)
C_BUFFER4 = Kind(
    name="C_BUFFER4",
    lis=None,
    iso_c_small="void",
    f90_small="<type>",
    f08_small="TYPE(C_PTR), VALUE",
)
EXTRA_STATE = Kind(
    name="EXTRA_STATE",
    lis=None,
    iso_c_small="void",
    f90_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
    f08_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
)
EXTRA_STATE2 = Kind(
    name="EXTRA_STATE2", lis=None, iso_c_small="void", f90_small="INTEGER", f08_small="INTEGER"
)
FUNCTION_SMALL = Kind(
    name="FUNCTION_SMALL",
    lis="function",
    iso_c_small=None,
    f90_small="EXTERNAL",
    f08_small="PROCEDURE",
)
FUNCTION = Kind(
    name="FUNCTION", lis="function", iso_c_small=None, f90_small="EXTERNAL", f08_small="PROCEDURE"
)
POLYFUNCTION = PolyKind(
    name="POLYFUNCTION",
    lis="function",
    iso_c_small=None,
    f90_small="EXTERNAL",
    f08_small="PROCEDURE",
    iso_c_large=None,
    f08_large="PROCEDURE",
)
EVENT_CB_FUNCTION = Kind(
    name="EVENT_CB_FUNCTION",
    lis="function",
    iso_c_small="MPI_T_event_cb_function",
    f90_small=None,
    f08_small=None,
)
EVENT_FREE_CB_FUNCTION = Kind(
    name="EVENT_FREE_CB_FUNCTION",
    lis="function",
    iso_c_small="MPI_T_event_free_cb_function",
    f90_small=None,
    f08_small=None,
)
EVENT_DROP_CB_FUNCTION = Kind(
    name="EVENT_DROP_CB_FUNCTION",
    lis="function",
    iso_c_small="MPI_T_event_dropped_cb_function",
    f90_small=None,
    f08_small=None,
)
STRING = Kind(
    name="STRING",
    lis="string",
    iso_c_small="char",
    f90_small="CHARACTER*(*)",
    f08_small="CHARACTER",
)
STRING_ARRAY = Kind(
    name="STRING_ARRAY",
    lis="array of strings",
    iso_c_small="char",
    f90_small="CHARACTER*(*)",
    f08_small="CHARACTER",
)
STRING_2DARRAY = Kind(
    name="STRING_2DARRAY",
    lis="array of array of strings",
    iso_c_small="char",
    f90_small="CHARACTER*(*)",
    f08_small="CHARACTER",
)
ARGUMENT_COUNT = Kind(
    name="ARGUMENT_COUNT", lis=None, iso_c_small="int", f90_small=None, f08_small=None
)
ARGUMENT_LIST = Kind(
    name="ARGUMENT_LIST", lis=None, iso_c_small="char", f90_small=None, f08_small=None
)
ARRAY_LENGTH = Kind(
    name="ARRAY_LENGTH", lis="integer", iso_c_small="int", f90_small="INTEGER", f08_small="INTEGER"
)
ARRAY_LENGTH_NNI = Kind(
    name="ARRAY_LENGTH_NNI",
    lis="non-negative integer",
    iso_c_small="int",
    f90_small="INTEGER",
    f08_small="INTEGER",
)
ARRAY_LENGTH_PI = Kind(
    name="ARRAY_LENGTH_PI",
    lis="positive integer",
    iso_c_small="int",
    f90_small="INTEGER",
    f08_small="INTEGER",
)
ATTRIBUTE_VAL_10 = Kind(
    name="ATTRIBUTE_VAL_10", lis=None, iso_c_small="void", f90_small="INTEGER", f08_small="INTEGER"
)
ATTRIBUTE_VAL = Kind(
    name="ATTRIBUTE_VAL",
    lis=None,
    iso_c_small="void",
    f90_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
    f08_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
)
BLOCKLENGTH = Kind(
    name="BLOCKLENGTH",
    lis="non-negative integer",
    iso_c_small="int",
    f90_small="INTEGER",
    f08_small="INTEGER",
)
COLOR = Kind(
    name="COLOR", lis="integer", iso_c_small="int", f90_small="INTEGER", f08_small="INTEGER"
)
COORDINATE = Kind(
    name="COORDINATE", lis="integer", iso_c_small="int", f90_small="INTEGER", f08_small="INTEGER"
)
COORDINATE_NNI = Kind(
    name="COORDINATE_NNI",
    lis="non-negative integer",
    iso_c_small="int",
    f90_small="INTEGER",
    f08_small="INTEGER",
)
DEGREE = Kind(
    name="DEGREE",
    lis="non-negative integer",
    iso_c_small="int",
    f90_small="INTEGER",
    f08_small="INTEGER",
)
DIMENSION = Kind(
    name="DIMENSION", lis="integer", iso_c_small="int", f90_small="INTEGER", f08_small="INTEGER"
)
ENUM = Kind(name="ENUM", lis="integer", iso_c_small="int", f90_small="INTEGER", f08_small="INTEGER")
FILE_DESCRIPTOR = Kind(
    name="FILE_DESCRIPTOR",
    lis="integer",
    iso_c_small="int",
    f90_small="INTEGER",
    f08_small="INTEGER",
)
KEY = Kind(name="KEY", lis="integer", iso_c_small="int", f90_small="INTEGER", f08_small="INTEGER")
KEYVAL = Kind(
    name="KEYVAL", lis="integer", iso_c_small="int", f90_small="INTEGER", f08_small="INTEGER"
)
INDEX = Kind(
    name="INDEX", lis="integer", iso_c_small="int", f90_small="INTEGER", f08_small="INTEGER"
)
LOGICAL = Kind(
    name="LOGICAL", lis="logical", iso_c_small="int", f90_small="LOGICAL", f08_small="LOGICAL"
)
LOGICAL_OPTIONAL = Kind(
    name="LOGICAL_OPTIONAL", lis="integer", iso_c_small="int", f90_small=None, f08_small=None
)
LOGICAL_BOOLEAN = Kind(
    name="LOGICAL_BOOLEAN",
    lis="boolean",
    iso_c_small="int",
    f90_small="LOGICAL",
    f08_small="LOGICAL",
)
MATH = Kind(name="MATH", lis="integer", iso_c_small="int", f90_small="INTEGER", f08_small="INTEGER")
NUM_DIMS = Kind(
    name="NUM_DIMS", lis="integer", iso_c_small="int", f90_small="INTEGER", f08_small="INTEGER"
)
RANK = Kind(name="RANK", lis="integer", iso_c_small="int", f90_small="INTEGER", f08_small="INTEGER")
RANK_NNI = Kind(
    name="RANK_NNI",
    lis="non-negative integer",
    iso_c_small="int",
    f90_small="INTEGER",
    f08_small="INTEGER",
)
COMM_SIZE = Kind(
    name="COMM_SIZE", lis="integer", iso_c_small="int", f90_small="INTEGER", f08_small="INTEGER"
)
COMM_SIZE_PI = Kind(
    name="COMM_SIZE_PI",
    lis="positive integer",
    iso_c_small="int",
    f90_small="INTEGER",
    f08_small="INTEGER",
)
STRING_LENGTH = Kind(
    name="STRING_LENGTH", lis="integer", iso_c_small="int", f90_small="INTEGER", f08_small="INTEGER"
)
STRIDE_BYTES = Kind(
    name="STRIDE_BYTES",
    lis="integer",
    iso_c_small="MPI_Aint",
    f90_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
    f08_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
)
STRIDE_ELEM = Kind(
    name="STRIDE_ELEM", lis="integer", iso_c_small="int", f90_small="INTEGER", f08_small="INTEGER"
)
TAG = Kind(name="TAG", lis="integer", iso_c_small="int", f90_small="INTEGER", f08_small="INTEGER")
VERSION = Kind(
    name="VERSION", lis="integer", iso_c_small="int", f90_small="INTEGER", f08_small="INTEGER"
)
WEIGHT = Kind(
    name="WEIGHT",
    lis="non-negative integer",
    iso_c_small="int",
    f90_small="INTEGER",
    f08_small="INTEGER",
)
OFFSET = Kind(
    name="OFFSET",
    lis="integer",
    iso_c_small="MPI_Offset",
    f90_small="INTEGER(KIND=MPI_OFFSET_KIND)",
    f08_small="INTEGER(KIND=MPI_OFFSET_KIND)",
)
PROFILE_LEVEL = Kind(
    name="PROFILE_LEVEL", lis="integer", iso_c_small="int", f90_small="INTEGER", f08_small="INTEGER"
)
ASSERT = Kind(
    name="ASSERT", lis="integer", iso_c_small="int", f90_small="INTEGER", f08_small="INTEGER"
)
WINDOW_SIZE = Kind(
    name="WINDOW_SIZE",
    lis="non-negative integer",
    iso_c_small="MPI_Aint",
    f90_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
    f08_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
)
INFO_VALUE_LENGTH = Kind(
    name="INFO_VALUE_LENGTH",
    lis="integer",
    iso_c_small="int",
    f90_small="INTEGER",
    f08_small="INTEGER",
)
ACCESS_MODE = Kind(
    name="ACCESS_MODE", lis="integer", iso_c_small="int", f90_small="INTEGER", f08_small="INTEGER"
)
KEY_INDEX = Kind(
    name="KEY_INDEX", lis="integer", iso_c_small="int", f90_small="INTEGER", f08_small="INTEGER"
)
TOOLENUM_INDEX = Kind(
    name="TOOLENUM_INDEX", lis="integer", iso_c_small="int", f90_small=None, f08_small=None
)
TOOLENUM_SIZE = Kind(
    name="TOOLENUM_SIZE", lis="integer", iso_c_small="int", f90_small=None, f08_small=None
)
TOOL_VAR_VERBOSITY = Kind(
    name="TOOL_VAR_VERBOSITY", lis="integer", iso_c_small="int", f90_small=None, f08_small=None
)
TOOL_VAR_VALUE = Kind(
    name="TOOL_VAR_VALUE", lis="integer", iso_c_small="int", f90_small=None, f08_small=None
)
CVAR_INDEX = Kind(
    name="CVAR_INDEX", lis="integer", iso_c_small="int", f90_small=None, f08_small=None
)
CVAR_INDEX_SPECIAL = Kind(
    name="CVAR_INDEX_SPECIAL", lis="index", iso_c_small="int", f90_small=None, f08_small=None
)
PVAR_INDEX = Kind(
    name="PVAR_INDEX", lis="integer", iso_c_small="int", f90_small=None, f08_small=None
)
PVAR_CLASS = Kind(
    name="PVAR_CLASS", lis="integer", iso_c_small="int", f90_small=None, f08_small=None
)
SOURCE_INDEX = Kind(
    name="SOURCE_INDEX", lis="integer", iso_c_small="int", f90_small=None, f08_small=None
)
EVENT_INDEX = Kind(
    name="EVENT_INDEX", lis="integer", iso_c_small="int", f90_small=None, f08_small=None
)
CAT_INDEX = Kind(name="CAT_INDEX", lis="integer", iso_c_small="int", f90_small=None, f08_small=None)
UPDATE_NUMBER = Kind(
    name="UPDATE_NUMBER", lis="integer", iso_c_small="int", f90_small=None, f08_small=None
)
DROPPED_COUNT = Kind(
    name="DROPPED_COUNT",
    lis="positive integer",
    iso_c_small="MPI_Count",
    f90_small=None,
    f08_small=None,
)
TYPECLASS_SIZE = Kind(
    name="TYPECLASS_SIZE",
    lis="integer",
    iso_c_small="int",
    f90_small="INTEGER",
    f08_small="INTEGER",
)
GENERIC_DTYPE_INT = Kind(
    name="GENERIC_DTYPE_INT",
    lis="integer",
    iso_c_small="int",
    f90_small="INTEGER",
    f08_small="INTEGER",
)
GENERIC_DTYPE_COUNT = Kind(
    name="GENERIC_DTYPE_COUNT",
    lis="integer",
    iso_c_small="MPI_Count",
    f90_small="INTEGER(KIND=MPI_COUNT_KIND)",
    f08_small="INTEGER(KIND=MPI_COUNT_KIND)",
)
PROCESS_GRID_SIZE = Kind(
    name="PROCESS_GRID_SIZE",
    lis="positive integer",
    iso_c_small="int",
    f90_small="INTEGER",
    f08_small="INTEGER",
)
DTYPE_DISTRIBUTION = Kind(
    name="DTYPE_DISTRIBUTION",
    lis="positive integer",
    iso_c_small="int",
    f90_small="INTEGER",
    f08_small="INTEGER",
)
ALLOC_MEM_NUM_BYTES = Kind(
    name="ALLOC_MEM_NUM_BYTES",
    lis="non-negative integer",
    iso_c_small="MPI_Aint",
    f90_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
    f08_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
)
PACK_EXTERNAL_SIZE = Kind(
    name="PACK_EXTERNAL_SIZE",
    lis="integer",
    iso_c_small="MPI_Aint",
    f90_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
    f08_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
)
WIN_ATTACH_SIZE = Kind(
    name="WIN_ATTACH_SIZE",
    lis="non-negative integer",
    iso_c_small="MPI_Aint",
    f90_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
    f08_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
)
DISPLACEMENT_SMALL = Kind(
    name="DISPLACEMENT_SMALL",
    lis="integer",
    iso_c_small="int",
    f90_small="INTEGER",
    f08_small="INTEGER",
)
DISPLACEMENT = Kind(
    name="DISPLACEMENT",
    lis="integer",
    iso_c_small="MPI_Aint",
    f90_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
    f08_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
)
DISPLACEMENT_NNI = Kind(
    name="DISPLACEMENT_NNI",
    lis="non-negative integer",
    iso_c_small="MPI_Aint",
    f90_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
    f08_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
)
POLYDISPLACEMENT = PolyKind(
    name="POLYDISPLACEMENT",
    lis="integer",
    iso_c_small="int",
    f90_small="INTEGER",
    f08_small="INTEGER",
    iso_c_large="MPI_Aint",
    f08_large="INTEGER(KIND=MPI_ADDRESS_KIND)",
)
NUM_BYTES_SMALL = Kind(
    name="NUM_BYTES_SMALL",
    lis="integer",
    iso_c_small="int",
    f90_small="INTEGER",
    f08_small="INTEGER",
)
NUM_BYTES = Kind(
    name="NUM_BYTES",
    lis="integer",
    iso_c_small="MPI_Count",
    f90_small="INTEGER(KIND=MPI_COUNT_KIND)",
    f08_small="INTEGER(KIND=MPI_COUNT_KIND)",
)
NUM_BYTES_NNI_SMALL = Kind(
    name="NUM_BYTES_NNI_SMALL",
    lis="non-negative integer",
    iso_c_small="int",
    f90_small="INTEGER",
    f08_small="INTEGER",
)
NUM_BYTES_NNI = Kind(
    name="NUM_BYTES_NNI",
    lis="non-negative integer",
    iso_c_small="MPI_Count",
    f90_small="INTEGER(KIND=MPI_COUNT_KIND)",
    f08_small="INTEGER(KIND=MPI_COUNT_KIND)",
)
ERROR_CODE = Kind(
    name="ERROR_CODE", lis="integer", iso_c_small="int", f90_small="INTEGER", f08_small="INTEGER"
)
ERROR_CODE_SHOW_INTENT = Kind(
    name="ERROR_CODE_SHOW_INTENT",
    lis="integer",
    iso_c_small="int",
    f90_small="INTEGER",
    f08_small="INTEGER",
)
ERROR_CLASS = Kind(
    name="ERROR_CLASS", lis="integer", iso_c_small="int", f90_small="INTEGER", f08_small="INTEGER"
)
ORDER = Kind(name="ORDER", lis="state", iso_c_small="int", f90_small="INTEGER", f08_small="INTEGER")
THREAD_LEVEL = Kind(
    name="THREAD_LEVEL", lis="integer", iso_c_small="int", f90_small="INTEGER", f08_small="INTEGER"
)
COMBINER = Kind(
    name="COMBINER", lis="state", iso_c_small="int", f90_small="INTEGER", f08_small="INTEGER"
)
LOCK_TYPE = Kind(
    name="LOCK_TYPE", lis="state", iso_c_small="int", f90_small="INTEGER", f08_small="INTEGER"
)
TOOLS_ENUM = Kind(
    name="TOOLS_ENUM", lis="handle", iso_c_small="MPI_T_enum", f90_small=None, f08_small=None
)
UPDATE_MODE = Kind(
    name="UPDATE_MODE", lis="state", iso_c_small="int", f90_small="INTEGER", f08_small="INTEGER"
)
BIND_TYPE = Kind(name="BIND_TYPE", lis="integer", iso_c_small="int", f90_small=None, f08_small=None)
SOURCE_ORDERING = Kind(
    name="SOURCE_ORDERING",
    lis="integer",
    iso_c_small="MPI_T_source_order",
    f90_small=None,
    f08_small=None,
)
CALLBACK_SAFETY = Kind(
    name="CALLBACK_SAFETY",
    lis="integer",
    iso_c_small="MPI_T_cb_safety",
    f90_small=None,
    f08_small=None,
)
VARIABLE_SCOPE = Kind(
    name="VARIABLE_SCOPE", lis="integer", iso_c_small="int", f90_small=None, f08_small=None
)
TYPECLASS = Kind(
    name="TYPECLASS", lis="integer", iso_c_small="int", f90_small="INTEGER", f08_small="INTEGER"
)
GROUP_COMPARISON = Kind(
    name="GROUP_COMPARISON",
    lis="integer",
    iso_c_small="int",
    f90_small="INTEGER",
    f08_small="INTEGER",
)
COMM_COMPARISON = Kind(
    name="COMM_COMPARISON",
    lis="integer",
    iso_c_small="int",
    f90_small="INTEGER",
    f08_small="INTEGER",
)
SPLIT_TYPE = Kind(
    name="SPLIT_TYPE", lis="integer", iso_c_small="int", f90_small="INTEGER", f08_small="INTEGER"
)
TOPOLOGY_TYPE = Kind(
    name="TOPOLOGY_TYPE", lis="state", iso_c_small="int", f90_small="INTEGER", f08_small="INTEGER"
)
DISTRIB_ENUM = Kind(
    name="DISTRIB_ENUM", lis="state", iso_c_small="int", f90_small="INTEGER", f08_small="INTEGER"
)
RMA_DISPLACEMENT_SMALL = Kind(
    name="RMA_DISPLACEMENT_SMALL",
    lis="positive integer",
    iso_c_small="int",
    f90_small="INTEGER",
    f08_small="INTEGER",
)
RMA_DISPLACEMENT = Kind(
    name="RMA_DISPLACEMENT",
    lis="positive integer",
    iso_c_small="MPI_Aint",
    f90_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
    f08_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
)
POLYRMA_DISPLACEMENT = PolyKind(
    name="POLYRMA_DISPLACEMENT",
    lis="positive integer",
    iso_c_small="int",
    f90_small="INTEGER",
    f08_small="INTEGER",
    iso_c_large="MPI_Aint",
    f08_large="INTEGER(KIND=MPI_ADDRESS_KIND)",
)
RMA_DISPLACEMENT_NNI_SMALL = Kind(
    name="RMA_DISPLACEMENT_NNI_SMALL",
    lis="non-negative integer",
    iso_c_small="int",
    f90_small="INTEGER",
    f08_small="INTEGER",
)
RMA_DISPLACEMENT_NNI = Kind(
    name="RMA_DISPLACEMENT_NNI",
    lis="non-negative integer",
    iso_c_small="MPI_Aint",
    f90_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
    f08_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
)
POLYRMA_DISPLACEMENT_NNI = PolyKind(
    name="POLYRMA_DISPLACEMENT_NNI",
    lis="non-negative integer",
    iso_c_small="int",
    f90_small="INTEGER",
    f08_small="INTEGER",
    iso_c_large="MPI_Aint",
    f08_large="INTEGER(KIND=MPI_ADDRESS_KIND)",
)
DISPOFFSET_SMALL = Kind(
    name="DISPOFFSET_SMALL",
    lis="integer",
    iso_c_small="MPI_Aint",
    f90_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
    f08_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
)
DISPOFFSET = Kind(
    name="DISPOFFSET",
    lis="integer",
    iso_c_small="MPI_Count",
    f90_small="INTEGER(KIND=MPI_COUNT_KIND)",
    f08_small="INTEGER(KIND=MPI_COUNT_KIND)",
)
POLYDISPOFFSET = PolyKind(
    name="POLYDISPOFFSET",
    lis="integer",
    iso_c_small="MPI_Aint",
    f90_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
    f08_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
    iso_c_large="MPI_Count",
    f08_large="INTEGER(KIND=MPI_COUNT_KIND)",
)
DTYPE_NUM_ELEM_NNI_SMALL = Kind(
    name="DTYPE_NUM_ELEM_NNI_SMALL",
    lis="non-negative integer",
    iso_c_small="int",
    f90_small="INTEGER",
    f08_small="INTEGER",
)
DTYPE_NUM_ELEM_NNI = Kind(
    name="DTYPE_NUM_ELEM_NNI",
    lis="non-negative integer",
    iso_c_small="MPI_Count",
    f90_small="INTEGER(KIND=MPI_COUNT_KIND)",
    f08_small="INTEGER(KIND=MPI_COUNT_KIND)",
)
POLYDTYPE_NUM_ELEM_NNI = PolyKind(
    name="POLYDTYPE_NUM_ELEM_NNI",
    lis="non-negative integer",
    iso_c_small="int",
    f90_small="INTEGER",
    f08_small="INTEGER",
    iso_c_large="MPI_Count",
    f08_large="INTEGER(KIND=MPI_COUNT_KIND)",
)
DTYPE_NUM_ELEM_SMALL = Kind(
    name="DTYPE_NUM_ELEM_SMALL",
    lis="integer",
    iso_c_small="int",
    f90_small="INTEGER",
    f08_small="INTEGER",
)
DTYPE_NUM_ELEM = Kind(
    name="DTYPE_NUM_ELEM",
    lis="integer",
    iso_c_small="MPI_Count",
    f90_small="INTEGER(KIND=MPI_COUNT_KIND)",
    f08_small="INTEGER(KIND=MPI_COUNT_KIND)",
)
POLYDTYPE_NUM_ELEM = PolyKind(
    name="POLYDTYPE_NUM_ELEM",
    lis="integer",
    iso_c_small="int",
    f90_small="INTEGER",
    f08_small="INTEGER",
    iso_c_large="MPI_Count",
    f08_large="INTEGER(KIND=MPI_COUNT_KIND)",
)
DTYPE_NUM_ELEM_PI_SMALL = Kind(
    name="DTYPE_NUM_ELEM_PI_SMALL",
    lis="positive integer",
    iso_c_small="int",
    f90_small="INTEGER",
    f08_small="INTEGER",
)
DTYPE_NUM_ELEM_PI = Kind(
    name="DTYPE_NUM_ELEM_PI",
    lis="positive integer",
    iso_c_small="MPI_Count",
    f90_small="INTEGER(KIND=MPI_COUNT_KIND)",
    f08_small="INTEGER(KIND=MPI_COUNT_KIND)",
)
POLYDTYPE_NUM_ELEM_PI = PolyKind(
    name="POLYDTYPE_NUM_ELEM_PI",
    lis="positive integer",
    iso_c_small="int",
    f90_small="INTEGER",
    f08_small="INTEGER",
    iso_c_large="MPI_Count",
    f08_large="INTEGER(KIND=MPI_COUNT_KIND)",
)
DTYPE_STRIDE_BYTES_SMALL = Kind(
    name="DTYPE_STRIDE_BYTES_SMALL",
    lis="integer",
    iso_c_small="MPI_Aint",
    f90_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
    f08_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
)
DTYPE_STRIDE_BYTES = Kind(
    name="DTYPE_STRIDE_BYTES",
    lis="integer",
    iso_c_small="MPI_Count",
    f90_small="INTEGER(KIND=MPI_COUNT_KIND)",
    f08_small="INTEGER(KIND=MPI_COUNT_KIND)",
)
POLYDTYPE_STRIDE_BYTES = PolyKind(
    name="POLYDTYPE_STRIDE_BYTES",
    lis="integer",
    iso_c_small="MPI_Aint",
    f90_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
    f08_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
    iso_c_large="MPI_Count",
    f08_large="INTEGER(KIND=MPI_COUNT_KIND)",
)
DISPLACEMENT_COUNT_SMALL = Kind(
    name="DISPLACEMENT_COUNT_SMALL",
    lis="integer",
    iso_c_small="int",
    f90_small="INTEGER",
    f08_small="INTEGER",
)
DISPLACEMENT_COUNT = Kind(
    name="DISPLACEMENT_COUNT",
    lis="integer",
    iso_c_small="MPI_Count",
    f90_small="INTEGER(KIND=MPI_COUNT_KIND)",
    f08_small="INTEGER(KIND=MPI_COUNT_KIND)",
)
POLYDISPLACEMENT_COUNT = PolyKind(
    name="POLYDISPLACEMENT_COUNT",
    lis="integer",
    iso_c_small="int",
    f90_small="INTEGER",
    f08_small="INTEGER",
    iso_c_large="MPI_Count",
    f08_large="INTEGER(KIND=MPI_COUNT_KIND)",
)
DISPLACEMENT_AINT_COUNT_SMALL = Kind(
    name="DISPLACEMENT_AINT_COUNT_SMALL",
    lis="integer",
    iso_c_small="MPI_Aint",
    f90_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
    f08_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
)
DISPLACEMENT_AINT_COUNT = Kind(
    name="DISPLACEMENT_AINT_COUNT",
    lis="integer",
    iso_c_small="MPI_Count",
    f90_small="INTEGER(KIND=MPI_COUNT_KIND)",
    f08_small="INTEGER(KIND=MPI_COUNT_KIND)",
)
POLYDISPLACEMENT_AINT_COUNT = PolyKind(
    name="POLYDISPLACEMENT_AINT_COUNT",
    lis="integer",
    iso_c_small="MPI_Aint",
    f90_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
    f08_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
    iso_c_large="MPI_Count",
    f08_large="INTEGER(KIND=MPI_COUNT_KIND)",
)
DTYPE_PACK_SIZE_SMALL = Kind(
    name="DTYPE_PACK_SIZE_SMALL",
    lis="integer",
    iso_c_small="MPI_Aint",
    f90_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
    f08_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
)
DTYPE_PACK_SIZE = Kind(
    name="DTYPE_PACK_SIZE",
    lis="integer",
    iso_c_small="MPI_Count",
    f90_small="INTEGER(KIND=MPI_COUNT_KIND)",
    f08_small="INTEGER(KIND=MPI_COUNT_KIND)",
)
POLYDTYPE_PACK_SIZE = PolyKind(
    name="POLYDTYPE_PACK_SIZE",
    lis="integer",
    iso_c_small="MPI_Aint",
    f90_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
    f08_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
    iso_c_large="MPI_Count",
    f08_large="INTEGER(KIND=MPI_COUNT_KIND)",
)
LOCATION_SMALL = Kind(
    name="LOCATION_SMALL",
    lis="integer",
    iso_c_small="MPI_Aint",
    f90_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
    f08_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
)
LOCATION = Kind(
    name="LOCATION",
    lis="integer",
    iso_c_small="MPI_Count",
    f90_small="INTEGER(KIND=MPI_COUNT_KIND)",
    f08_small="INTEGER(KIND=MPI_COUNT_KIND)",
)
POLYLOCATION = PolyKind(
    name="POLYLOCATION",
    lis="integer",
    iso_c_small="MPI_Aint",
    f90_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
    f08_small="INTEGER(KIND=MPI_ADDRESS_KIND)",
    iso_c_large="MPI_Count",
    f08_large="INTEGER(KIND=MPI_COUNT_KIND)",
)
TOOLS_NUM_ELEM_SMALL = Kind(
    name="TOOLS_NUM_ELEM_SMALL",
    lis="integer",
    iso_c_small="int",
    f90_small="INTEGER",
    f08_small="INTEGER",
)
TOOLS_NUM_ELEM = Kind(
    name="TOOLS_NUM_ELEM",
    lis="integer",
    iso_c_small="MPI_Count",
    f90_small="INTEGER(KIND=MPI_COUNT_KIND)",
    f08_small="INTEGER(KIND=MPI_COUNT_KIND)",
)
POLYTOOLS_NUM_ELEM = PolyKind(
    name="POLYTOOLS_NUM_ELEM",
    lis="integer",
    iso_c_small="int",
    f90_small="INTEGER",
    f08_small="INTEGER",
    iso_c_large="MPI_Count",
    f08_large="INTEGER(KIND=MPI_COUNT_KIND)",
)
TOOLS_TICK_COUNT = Kind(
    name="TOOLS_TICK_COUNT", lis="integer", iso_c_small="MPI_Count", f90_small=None, f08_small=None
)
POLYNUM_BYTES = PolyKind(
    name="POLYNUM_BYTES",
    lis="integer",
    iso_c_small="int",
    f90_small="INTEGER",
    f08_small="INTEGER",
    iso_c_large="MPI_Count",
    f08_large="INTEGER(KIND=MPI_COUNT_KIND)",
)
POLYNUM_BYTES_NNI = PolyKind(
    name="POLYNUM_BYTES_NNI",
    lis="non-negative integer",
    iso_c_small="int",
    f90_small="INTEGER",
    f08_small="INTEGER",
    iso_c_large="MPI_Count",
    f08_large="INTEGER(KIND=MPI_COUNT_KIND)",
)
XFER_NUM_ELEM_NNI_SMALL = Kind(
    name="XFER_NUM_ELEM_NNI_SMALL",
    lis="non-negative integer",
    iso_c_small="int",
    f90_small="INTEGER",
    f08_small="INTEGER",
)
XFER_NUM_ELEM_NNI = Kind(
    name="XFER_NUM_ELEM_NNI",
    lis="non-negative integer",
    iso_c_small="MPI_Count",
    f90_small="INTEGER(KIND=MPI_COUNT_KIND)",
    f08_small="INTEGER(KIND=MPI_COUNT_KIND)",
)
POLYXFER_NUM_ELEM_NNI = PolyKind(
    name="POLYXFER_NUM_ELEM_NNI",
    lis="non-negative integer",
    iso_c_small="int",
    f90_small="INTEGER",
    f08_small="INTEGER",
    iso_c_large="MPI_Count",
    f08_large="INTEGER(KIND=MPI_COUNT_KIND)",
)
XFER_NUM_ELEM_SMALL = Kind(
    name="XFER_NUM_ELEM_SMALL",
    lis="integer",
    iso_c_small="int",
    f90_small="INTEGER",
    f08_small="INTEGER",
)
XFER_NUM_ELEM = Kind(
    name="XFER_NUM_ELEM",
    lis="integer",
    iso_c_small="MPI_Count",
    f90_small="INTEGER(KIND=MPI_COUNT_KIND)",
    f08_small="INTEGER(KIND=MPI_COUNT_KIND)",
)
POLYXFER_NUM_ELEM = PolyKind(
    name="POLYXFER_NUM_ELEM",
    lis="integer",
    iso_c_small="int",
    f90_small="INTEGER",
    f08_small="INTEGER",
    iso_c_large="MPI_Count",
    f08_large="INTEGER(KIND=MPI_COUNT_KIND)",
)
NUM_PARAM_VALUES_SMALL = Kind(
    name="NUM_PARAM_VALUES_SMALL",
    lis="non-negative integer",
    iso_c_small="int",
    f90_small="INTEGER",
    f08_small="INTEGER",
)
POLYNUM_PARAM_VALUES = PolyKind(
    name="POLYNUM_PARAM_VALUES",
    lis="non-negative integer",
    iso_c_small="int",
    f90_small="INTEGER",
    f08_small="INTEGER",
    iso_c_large="MPI_Count",
    f08_large="INTEGER(KIND=MPI_COUNT_KIND)",
)
NUM_PARAM_VALUES = Kind(
    name="NUM_PARAM_VALUES",
    lis="non-negative integer",
    iso_c_small="MPI_Count",
    f90_small="INTEGER(KIND=MPI_COUNT_KIND)",
    f08_small="INTEGER(KIND=MPI_COUNT_KIND)",
)
PARTITION = Kind(
    name="PARTITION",
    lis="non-negative integer",
    iso_c_small="int",
    f90_small="INTEGER",
    f08_small="INTEGER",
)
COMMUNICATOR = Kind(
    name="COMMUNICATOR",
    lis="handle",
    iso_c_small="MPI_Comm",
    f90_small="INTEGER",
    f08_small="TYPE(MPI_Comm)",
)
DATATYPE = Kind(
    name="DATATYPE",
    lis="handle",
    iso_c_small="MPI_Datatype",
    f90_small="INTEGER",
    f08_small="TYPE(MPI_Datatype)",
)
ERRHANDLER = Kind(
    name="ERRHANDLER",
    lis="handle",
    iso_c_small="MPI_Errhandler",
    f90_small="INTEGER",
    f08_small="TYPE(MPI_Errhandler)",
)
FILE = Kind(
    name="FILE",
    lis="handle",
    iso_c_small="MPI_File",
    f90_small="INTEGER",
    f08_small="TYPE(MPI_File)",
)
GROUP = Kind(
    name="GROUP",
    lis="handle",
    iso_c_small="MPI_Group",
    f90_small="INTEGER",
    f08_small="TYPE(MPI_Group)",
)
INFO = Kind(
    name="INFO",
    lis="handle",
    iso_c_small="MPI_Info",
    f90_small="INTEGER",
    f08_small="TYPE(MPI_Info)",
)
MESSAGE = Kind(
    name="MESSAGE",
    lis="handle",
    iso_c_small="MPI_Message",
    f90_small="INTEGER",
    f08_small="TYPE(MPI_Message)",
)
REQUEST = Kind(
    name="REQUEST",
    lis="handle",
    iso_c_small="MPI_Request",
    f90_small="INTEGER",
    f08_small="TYPE(MPI_Request)",
)
SESSION = Kind(
    name="SESSION",
    lis="handle",
    iso_c_small="MPI_Session",
    f90_small="INTEGER",
    f08_small="TYPE(MPI_Session)",
)
STATUS = Kind(
    name="STATUS",
    lis="status",
    iso_c_small="MPI_Status",
    f90_small="INTEGER",
    f08_small="TYPE(MPI_Status)",
)
WINDOW = Kind(
    name="WINDOW",
    lis="handle",
    iso_c_small="MPI_Win",
    f90_small="INTEGER",
    f08_small="TYPE(MPI_Win)",
)
OPERATION = Kind(
    name="OPERATION",
    lis="handle",
    iso_c_small="MPI_Op",
    f90_small="INTEGER",
    f08_small="TYPE(MPI_Op)",
)
CVAR = Kind(
    name="CVAR", lis="handle", iso_c_small="MPI_T_cvar_handle", f90_small=None, f08_small=None
)
PVAR = Kind(
    name="PVAR", lis="handle", iso_c_small="MPI_T_pvar_handle", f90_small=None, f08_small=None
)
PVAR_SESSION = Kind(
    name="PVAR_SESSION",
    lis="handle",
    iso_c_small="MPI_T_pvar_session",
    f90_small=None,
    f08_small=None,
)
EVENT_REGISTRATION = Kind(
    name="EVENT_REGISTRATION",
    lis="handle",
    iso_c_small="MPI_T_event_registration",
    f90_small=None,
    f08_small=None,
)
EVENT_INSTANCE = Kind(
    name="EVENT_INSTANCE",
    lis="handle",
    iso_c_small="MPI_T_event_instance",
    f90_small=None,
    f08_small=None,
)
TOOL_MPI_OBJ = Kind(
    name="TOOL_MPI_OBJ", lis="pointer", iso_c_small="void", f90_small=None, f08_small=None
)
F90_STATUS = Kind(
    name="F90_STATUS",
    lis="status",
    iso_c_small="MPI_Fint",
    f90_small="INTEGER",
    f08_small="INTEGER",
)
F08_STATUS = Kind(
    name="F08_STATUS",
    lis="status",
    iso_c_small="MPI_F08_status",
    f90_small="TYPE(MPI_Status)",
    f08_small="TYPE(MPI_Status)",
)
F90_COMM = Kind(name="F90_COMM", lis=None, iso_c_small="MPI_Fint", f90_small=None, f08_small=None)
F90_DATATYPE = Kind(
    name="F90_DATATYPE", lis=None, iso_c_small="MPI_Fint", f90_small=None, f08_small=None
)
F90_GROUP = Kind(name="F90_GROUP", lis=None, iso_c_small="MPI_Fint", f90_small=None, f08_small=None)
F90_REQUEST = Kind(
    name="F90_REQUEST", lis=None, iso_c_small="MPI_Fint", f90_small=None, f08_small=None
)
F90_FILE = Kind(name="F90_FILE", lis=None, iso_c_small="MPI_Fint", f90_small=None, f08_small=None)
F90_WIN = Kind(name="F90_WIN", lis=None, iso_c_small="MPI_Fint", f90_small=None, f08_small=None)
F90_OP = Kind(name="F90_OP", lis=None, iso_c_small="MPI_Fint", f90_small=None, f08_small=None)
F90_INFO = Kind(name="F90_INFO", lis=None, iso_c_small="MPI_Fint", f90_small=None, f08_small=None)
F90_ERRHANDLER = Kind(
    name="F90_ERRHANDLER", lis=None, iso_c_small="MPI_Fint", f90_small=None, f08_small=None
)
F90_MESSAGE = Kind(
    name="F90_MESSAGE", lis=None, iso_c_small="MPI_Fint", f90_small=None, f08_small=None
)
F90_SESSION = Kind(
    name="F90_SESSION", lis=None, iso_c_small="MPI_Fint", f90_small=None, f08_small=None
)
VARARGS = Kind(name="VARARGS", lis="\\ldots", iso_c_small="\\ldots", f90_small=None, f08_small=None)
WALL_TIME = Kind(
    name="WALL_TIME",
    lis=None,
    iso_c_small="double",
    f90_small="DOUBLE PRECISION",
    f08_small="DOUBLE PRECISION",
)
TICK_RESOLUTION = Kind(
    name="TICK_RESOLUTION",
    lis=None,
    iso_c_small="double",
    f90_small="DOUBLE PRECISION",
    f08_small="DOUBLE PRECISION",
)
NOTHING = Kind(name="NOTHING", lis=None, iso_c_small="void", f90_small=None, f08_small=None)
