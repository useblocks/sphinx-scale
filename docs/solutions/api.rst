API
===

Solutions on this page
----------------------
To search all ``solutions`` take a look into the upper page :ref:`solutions`.

.. needtable::
   :filter: "API" in sections and type=="solution"
   :columns: title, id, solves

.. solution:: autodoc directive for Python APIs
   :id: sphinx_autodoc
   :solves: python_api_doc
   :uses: sphinx

   Use the sphinx feature `autodoc <https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html>`_ to
   automatically to document an API by using the docstrings of related python based objects
   (modules, classes, functions, ...).

    .. code-block:: python

       .. autoclass my_app.my_module.my_class
          :members:  # Add all public mebmers with a docstring
          :undoc-members:  # Add members without a docstring
          :private-members  # Add also private members like "_my_secret"
