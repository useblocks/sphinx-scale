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

.. panels::
    :card: + intro-card text-center
    :column: col-lg-3 col-md-6 col-sm-6 col-xs-12 d-flex
    :img-top-cls: scale-card-image

    ---
    :img-top: _static/icon_problem.svg

    Have a problem?
    ^^^^^^^^^^^^^^

    Check if our documented problems are familiar to you and follow their links to one or more solutions.

    +++

    .. link-button:: problems
            :type: ref
            :text: Problems documentation
            :classes: btn-block btn-secondary stretched-link

    ---
    :img-top: _static/icon_solution.svg

    Get a solution
    ^^^^^^^^^^^^^^

    Take a look into our solutions for common problems.

    +++

    .. link-button:: solutions
            :type: ref
            :text: Solutions documentation
            :classes: btn-block btn-secondary stretched-link

    ---
    :img-top: _static/icon_role.svg

    Analyse your role
    ^^^^^^^^^^^^^^^^^

    Find out what typical problems a specific process role may have with ``Docs-As-Code`` and ``Sphinx``.

    +++

    .. link-button:: roles
            :type: ref
            :text: Roles documentation
            :classes: btn-block btn-secondary stretched-link

    ---
    :img-top: _static/icon_tool.svg

    Find new tools
    ^^^^^^^^^^^^^^

    Find new ideas in our tool, extensions and script chapter.

    +++

    .. link-button:: tools
            :type: ref
            :text: Tools documentation
            :classes: btn-block btn-secondary stretched-link

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
