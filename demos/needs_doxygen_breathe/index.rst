.. Demo C++ API with Doxygen documentation master file, created by
   sphinx-quickstart on Thu Apr 15 17:59:36 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Demo C++ API with Doxygen
=========================

RST content
-----------
.. need:: Need inside rst
   :id: NEED_1
   :status: open

.. need:: Need inside rst
   :id: NEED_3
   :status: open
   :links: NEED_1

C++ files
---------
:file: code/doxygen_example.hpp

.. literalinclude:: code/doxygen_example.hpp

Doxygen include
---------------
.. code-block:: rst

   .. doxygenfile:: doxygen_example.hpp
      :project: doxygen_example

``doxygenfile`` **result starts here:**

.. doxygenfile:: doxygen_example.hpp
   :project: doxygen_example

Analysis
--------
.. needtable::
   :style: table
   :columns: id, title, status, outgoing, incoming

.. needflow::


