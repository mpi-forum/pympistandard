Python API to the MPI Standard
##############################

This tutorial is intended to teach how to use the Python API of the MPI Standard.

Structure of the MPI Standard
*****************************

The Python usage in the MPI Standard is varied. 

The Python Domain Specific Language (DSL): We use the DSL to specify and encode the information in the MPI Standard through *mpi-binding* latex blocks. This facilitates that the "truth" remains within the Latex of the Standard.

The Python API *pympistandard* (./pympistandard) is the package by which access to the DSL encoded information is given to tools.

The tools which operate on the DSL encoded information are also written in Python (although they could be written in any language). This includes the binding_prepass (binding-tool/binding_prepass), binding_tool (tools/binding_tool), binding_linter (binding-tool/binding_linter), etc.

Finally, the testing of both the binding_tool, DSL, and text of the MPI Standard are partially done in Python (test/).

How to start using the Python API
*********************************

The goal of the Python API is to provide access to all information in the MPI Standard as easily as possible. Therefore importing the pympistandard package is done the typical python way, either by exporting the PYTHONPATH or having the pympistandard package on a standard path. The current solution is to have PYTHONPATH correctly exported.

To have functioning setup do:

#. change directory to the mpi-standard directory containing the version which you want to access programatically
#. ``make`` (at least past the rendering such that the apis.json file exists)
#. ``export PYTHONPATH=$(pwd)``

At this point the following should be possible within a python interpreter:

.. sourcecode::

    import pympistandard

.. toctree::
    :maxdepth: 2

    procedure

The Python API
**************

After importing the pympistandard package no information is yet loaded. One must first do:

.. sourcecode::
    
    pympistandard.use_api_version(1)

This loads the information contained in the MPI Standard using the first API version.

In future, other versions of the API will be accessible and a deprecation warning will be given. Extensions will not merit a new version, only backwards compatibility breaking changes. Once the ``use_api_version`` has been called the information is read into the global variables, at which point all information in the Standard will be accessible.

.. sourcecode::
    
    import pympistandard as std
    std.use_api_version(1) 

The top-level package contains **PROCEDURES**, **KINDS**, **CALLBACKS**, **PREDEFINED_FUNCTIONS** (the names are subject to change).

* PROCEDURES are all MPI procedures such as MPI_Send, MPI_Wait, MPI_Allreduce, MPI_Init, ...
* KINDS are all the different KINDS which are currently specified within the MPI Standard (these are subject to major revisions)
* CALLBACKS are all callback functions which are given as Kinds, these provide access to the expressions instead of just a label like the corresponding KIND
* PREDEFINED_FUNCTIONS are the predefined callback functions provided by the MPI Standard and its implementations

Using the Python API
********************

The global containers can be accessed using the dot notation or the dictionary access:

.. sourcecode::
    
    mpi_send = std.PROCEDURES.mpi_send

    mpi_send = std.PROCEDURES["mpi_send"]

Capitalisation is ignored. `MPI_SEND` is the same as `mpi_send`.

Checking membership of in a container can be done with:

.. sourcecode::
    
    "mpi_send" in std.PROCEDURES
    mpi_send in std.PROCEDURES

Another method to fetch Procedure/Callback/PredefinedFunction objects is through the provided iterators. Iterators are currently available for all Procedures expressible in a given language:

.. sourcecode::
    
    count_initializing_iso_c_procedures = sum(procedure.express.iso_c.is_initializing() for procedure in std.all_iso_c_procedures())

*Currently, is_initializing does not exist.*

Language Agnostic Information
*****************************

The above `mpi_send` object is a Procedure object which encapsulates all information which is generic to the MPI Procedure MPI\_Send. In future this will include all sorts of information such as the initialising, starting, completing, and freeing behaviour of a specific procedure. Currently the properties are `has_embiggenment` and `has_proxy_render`.

Language Expressions
********************

In addition to language agnostic information about the MPI Procedure the object provides access to expressions of the Procedure. An expression is a form of the Procedure in a specific language officially standardised by the MPI Forum through the MPI Standard. To access the ISO C expression of the _MPI\_Send_ procedure you would do:

.. sourcecode::
    
    c_send = std.PROCEDURES.mpi_send.express.iso_c

The `c\_send` object is a ISOCProcedure. The language specific procedure objects allow access to properties which are specific to a language. For example, ISO C procedures may use uppercase indexing in the MPI Standard therefore the `has_uppercase_index` property is provided within the ISOCProcedure.

In addition to language specific properties the expression in the language is enabled through this object. Access to parameters, return type/kind, and name is given:

.. sourcecode::

    c_send.name   # 'MPI_Send'
    c_send.return_type   # 'int'

Parameters are accessed as objects themselves:

.. sourcecode::
    
    names = (parameter.name for parameter in c_send.parameters)   # ('buf', 'count', 'datatype', 'dest', 'tag', 'comm')

Parameters also provide all properties associated with them and can be access through the object.

Not all Procedures are expressed in all languages. Therefore when an attempt is made to access an expression which does not exist a Nonetype is returned:

.. sourcecode::

    std.PROCEDURES.mpi_sizeof.iso_c   # None

Other Expressions
*****************

The expressions are not only related to the language in which a binding is expressed, but also the type of binding. For example, the profiling  interface of MPI specifies many PMPI prefixed procedures which can be accessed through:

.. sourcecode::

    pmpi_send = std.PROCEDURES.mpi_send.profile.iso_c
    pmpi_send.name   # 'PMPI_Send'

Another large expression subset is the embiggened procedures:

.. sourcecode::

    mpi_send_c = std.PROCEDURES.mpi_send.embiggen.iso_c
    mpi_send_c.name   # 'MPI_Send_c'

These expression attributes can be combined arbitrarily: `mpi_send.profile.embiggen.iso_c`. If a valid configuration is chosen an object representing the properties and expression will be returned. If not a Nonetype will be returned.

Instead of accessing the expressions through the dot notation you can also choose to have an iterable over all expressions of a language:

.. sourcecode::

    print(std.PROCEDURES.mpi_send.express.all_iso_c)

    # (<pympistandard.isoc.ISOCProcedure object at 0x10ee9ef10>,
    #  <pympistandard.isoc.ProfilingISOCProcedure object at 0x10ee9eeb0>,
    #  <pympistandard.isoc.EmbiggenedISOCProcedure object at 0x10ee9ed30>,
    #  <pympistandard.isoc.EmbiggenedProfilingISOCProcedure object at 0x10ee9ed90>)
