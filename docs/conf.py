# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'sphinx-scale'
copyright = '2021, team useblocks'
author = 'team useblocks'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinxcontrib.plantuml',
    'sphinxcontrib.needs',
    'sphinx_copybutton',
    'sphinx_panels',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'alabaster'
html_theme = 'pydata_sphinx_theme'
html_logo = "_static/sphinx_scale_wide_logo.png"
html_favicon = "_static/sphinx_scale_favicon.png"
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_css_files = ['custom.css']

html_context = {
    "github_user": "useblocks",
    "github_repo": "sphinx-scale",
    "github_version": "main",
    "doc_path": "docs",
}

html_theme_options = {
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/useblocks/sphinx-scale",
            "icon": "fab fa-github-square",
        },
        {
            "name": "useblocks",
            "url": "https://useblocks.com",
            "icon": "fas fa-phone-square",
        },
    ],
    "use_edit_page_button": True,
}

##############################
# SPHINX-NEEDS CONFIGURATION #
##############################

needs_types = [dict(directive="role", title="Role", prefix="R_", color="#BFD8D2", style="node"),
               dict(directive="problem", title="Problem", prefix="P_", color="#cb5d7e", style="node"),
               dict(directive="solution", title="Solution", prefix="S_", color="#7dca5d", style="node"),
               dict(directive="tool", title="Tool", prefix="T_", color="#5d7ecb", style="node"),
               ]

needs_flow_link_types = ['links', 'worries', 'solves', 'uses']
needs_flow_show_links = True
needs_extra_links = [
    {   # Problem -> Role
        "option": "worries",
        "incoming": "worries about",
        "outgoing": "worries",
    },

    {   # Solution -> Problem
        "option": "solves",
        "incoming": "is solved by",
        "outgoing": "solves",
        "style": "bold,#7dca5d",
        "style_part": "#7dca5d",
        "style_start": "-",
        "style_end": "->"
    },

    {   # Solution -> Tool, Tool -> Tool
        "option": "uses",
        "incoming": "used by",
        "outgoing": "uses",
        "style": "bold,#5d7ecb",
    },
]

needs_layouts = {
    'solution': {
        'grid': 'content_footer',
        'layout': {
            # 'head': ['**<<meta("title")>>** (<<meta("id")>>)'],
            # 'meta': [],
            'footer': ['**ID**: <<meta("id")>>']
        }
    }
}

needs_id_regex = "^[A-Za-z0-9_]"
needs_id_required = True

needs_global_options = {
      # Without default value
      'template': [
            ('solution', 'type=="solution"')
      ],
      'post_template': [
            ('post_solution', 'type=="solution"')
      ],
      'pre_template': [
            ('pre_solution', 'type=="solution"')
      ],
      'layout': [
            ('solution', 'type=="solution"')
      ],
      'style': [
            ('green_border', 'type=="solution"'),
            ('red_border', 'type=="problem"'),
            ('blue_border', 'type=="tool"')
      ],
   }

# PLANTUML config

on_rtd = os.environ.get('READTHEDOCS') == 'True'
cwd = os.getcwd()
local_plantuml_path = os.path.join(cwd, "utils/plantuml.jar")

if on_rtd:
    # Deactivated using rtd plantuml version as it looks quite old.
    # plantuml = 'java -Djava.awt.headless=true -jar /usr/share/plantuml/plantuml.jar'
    plantuml = 'java -Djava.awt.headless=true -jar {}'.format(local_plantuml_path)
else:
    cwd = os.getcwd()
    plantuml = 'java -jar {}'.format(local_plantuml_path)

# If we are running on windows, we need to manipulate the path,
# otherwise plantuml will have problems.
if os.name == "nt":
    plantuml = plantuml.replace("/", "\\")
    plantuml = plantuml.replace("\\", "\\\\")

# plantuml_output_format = 'png'
plantuml_output_format = 'svg_img'
