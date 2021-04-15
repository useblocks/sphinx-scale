Sphinx-Needs
============

.. solution:: template option for needs
   :id: sphinx_needs_templates
   :solves: needs_pre_post_content
   :uses: sphinx; sphinx_needs

   Use
   `template <https://sphinxcontrib-needs.readthedocs.io/en/latest/directives/need.html#need-template>`_,
   `pre_template <https://sphinxcontrib-needs.readthedocs.io/en/latest/directives/need.html#pre-template>`_ or
   `post_template <https://sphinxcontrib-needs.readthedocs.io/en/latest/directives/need.html#pre-template>`_
   to define the location of a template-file, which contains extra data/content.

   This templates are based on `jinja <https://jinja.palletsprojects.com/en/2.11.x/>`_ and have access to
   the current need data (title, id, status, content, ...).

   Example of a template stored as file ``extra_title.need`` in ``needs_templates/``:

   .. code-block:: jinja

      **{{title}}** ({{id}})

   The above code will add a simple line with title and id of the need.

   To set it in front of a need use ``pre_template``:

   .. code-block:: rst

      .. spec:: my need
         :pre_template: extra_title


   To set a template automatically, use
   `global_options <https://sphinxcontrib-needs.readthedocs.io/en/latest/configuration.html#needs-global-options>`_ ::

       needs_global_options = {
          'pre_template': [
                ('extra_title', 'type=="spec"')
          ],






