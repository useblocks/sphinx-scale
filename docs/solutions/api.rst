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
   automatically document an API by using the docstrings of related python based objects
   (modules, classes, functions, ...).

    .. code-block:: python

       .. autoclass my_app.my_module.my_class
          :members:  # Add all public mebmers with a docstring
          :undoc-members:  # Add members without a docstring
          :private-members  # Add also private members like "_my_secret"



.. solution:: Doxygen + breathe for C++ APIs in Sphinx
   :id: doxygen_sphinx
   :solves: cpp_api_doc
   :uses: doxygen, breathe, sphinx

   :need:`doxygen` must be installed on the system!
   And :need:`breathe` must be installed as Python package on the used virtual environment.

   .. code-block:: python

      # conf.py

      # Executes doxygen.
      # This makes sure that the extension "breathe" has access to the latest API information.

      extensions = ['breathe']

      if shutil.which("doxygen"):
          breathe_projects = {
              "doxygen_example": "_build/doxygen/xml"
              }
          breathe_default_project = "doxygen_example"

          if not os.environ.get("SKIP_DOXYGEN", None) == "True":
              for prjname, prjdir in breathe_projects.items():
                  print("Generating doxygen files for {}...".format(prjname))
                  os.makedirs(prjdir, exist_ok=True)
                  cmd = "cd code && doxygen {}.dox".format(prjname)
                  subprocess.call(cmd, shell=True)
          else:
              for prjname, prjdir in breathe_projects.items():
                  assert os.path.exists(prjdir) == True, \
                      "Regenerate doxygen XML for {}".format(prjname)

   .. code-block:: rst

      .. index.rst

      .. doxygenfile:: doxygen_example.hpp
         :project: doxygen_example
