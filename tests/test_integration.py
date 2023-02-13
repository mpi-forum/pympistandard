"""
This module contains tests which test the overall behaviour of pympistandard.
"""


def test_mpi_send_iso_c(bundled_dataset):
    assert str(bundled_dataset.PROCEDURES.mpi_send.express.iso_c) == (
        "int MPI_Send("
        "const void* buf, "
        "int count, "
        "MPI_Datatype datatype, "
        "int dest, "
        "int tag, "
        "MPI_Comm comm)"
    )


def test_mpi_comm_spawn_multiple(bundled_dataset):
    assert str(bundled_dataset.PROCEDURES.mpi_comm_spawn_multiple.express.iso_c) == (
        "int MPI_Comm_spawn_multiple("
        "int count, char* array_of_commands[], "
        "char** array_of_argv[], "
        "const int array_of_maxprocs[], "
        "const MPI_Info array_of_info[], "
        "int root, "
        "MPI_Comm comm, MPI_Comm* intercomm, "
        "int array_of_errcodes[])"
    )


def test_mpi_allgatherv_init(bundled_dataset):
    assert str(bundled_dataset.PROCEDURES.mpi_allgatherv_init.express.iso_c) == (
        "int MPI_Allgatherv_init("
        "const void* sendbuf, "
        "int sendcount, "
        "MPI_Datatype sendtype, "
        "void* recvbuf, "
        "const int recvcounts[], "
        "const int displs[], "
        "MPI_Datatype recvtype, "
        "MPI_Comm comm, "
        "MPI_Info info, "
        "MPI_Request* request)"
    )
