.. Sphinx Needs external data documentation master file, created by
   sphinx-quickstart on Thu Apr 15 17:03:08 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Demo Sphinx Needs external data
===============================

This is a demo from the `Sphinx-Scale documentation project <https://sphinx-scale.readthedocs.io>`__.

It demonstrates the usage of:

* need_import

Please see `Sphinx-Scale documentation project <https://sphinx-scale.readthedocs.io>`__
for more details and source code.


Original Needs
--------------

.. req:: Dummy requirement
   :id: REQ_1

.. spec:: Dummy specification
   :id: SPEC_1
   :links: REQ_1
   :connects: REQ_1

.. test:: Dummy test case
   :id: TEST_1
   :links: SPEC_1, REQ_1
   :connects: SPEC_1, REQ_1


Created needs.json
------------------

Created via ``make needs``.

.. literalinclude:: needs.json


Imported needs
--------------

Using::

   .. needimport:: needs.json

.. needimport:: needs.json
   :id_prefix: IMPORTED_




Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
