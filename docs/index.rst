.. image:: _static/sphinx_scale_wide_logo.png
   :width: 80%
   :align: center
   :class: sphinx-scale-logo

Sphinx-scale Documentation
==========================

``Sphinx-scale`` documents solutions for large setups of ``Docs-As-Code`` environments using ``Sphinx`` as their
main documentation tool.

This documentations provides currently :need_count:`type=="solution"` solutions for :need_count:`type=="problem"`
problems, which :need_count:`type=="role"` process roles may worry about in :need_count:`type=="tool"` tools.

All data
--------
.. needtable::
   :columns: type, title, id

Explanation
~~~~~~~~~~~
The above tables shows all objects (problems, solutions, ...) we have in our documentation.
Use the search box on the upper right side of the table to search for specific content (e.g. ``api`` if you want to find
solutions for how to document your API).

The table supports pagination and the search filter gets executed on all columns,
so you can also search for ``solution`` to get objects of type solution only.


Content
-------

.. toctree::
   :maxdepth: 2

   roles/index
   problems/index
   solutions/index
   tools/index
   usage
   contribute

Motivation
----------
The content of ``Sphinx-scale`` is based on experiences made in large projects, which mostly have:

* > 50 developers / editors
* > 500 readers
* > 10 shared Sphinx based documentations
* > 3 external data sources for additional content (Jira, github, Doors, Enterprise Architect, ...)
* multiple stakeholders (sw architects, sw developers, sw testers, sw safety officers, project managers, ...)



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
