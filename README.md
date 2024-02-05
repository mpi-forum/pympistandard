# pympistandard

This library provides programmatic access to the extracted data from the MPI
Standard build process. The library comes packaged with the dataset for the
latest MPI Standard version. It is possible to override the database loaded
with either an environment variable or passing of a path:

```bash
export "MPISTANDARD"="/my/path/to/my/apis.json"
```

```python
import pympistandard as std
std.use_api_version(1, given_path="this_is_definitely_a_path")
```

```python
import pympistandard as std
std.use_api_version(1, force_bundled=True)
```

---

Usage example:
```python
import pympistandard as std
std.use_api_version(1)

if "mpi_send" in std.PROCEDURES:
    mpi_send = std.PROCEDURES.mpi_send 
    mpi_send = std.PROCEDURES["mpi_send"]

print(mpi_send.express.iso_c)
# int MPI_Send(const void* buf, int count, MPI_Datatype datatype, int dest, int tag, MPI_Comm comm)

embiggened = [proc.name for proc in std.PROCEDURES.values() if proc.has_embiggenment()]
print(f"Embiggened procedures in 4.1: {len(embiggened)}")
# 154
```
