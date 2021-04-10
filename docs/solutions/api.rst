API
===

.. solution:: autodoc directive for Python APIs
   :id: s_python_api
   :solves: p_python_api
   :uses: t_sphinx

   Use the sphinx feature `autodoc <https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html>`_ to
   automatically to document an API b using the docstrings of related python based objects
   (modules, classes, functions, ...).

    .. code-block:: python

       .. autoclass my_app.my_module.my_class
          :members:  # Add all public mebmers with a docstring
          :undoc-members:  # Add members without a docstring
          :private-members  # Add also private members like "_my_secret"
