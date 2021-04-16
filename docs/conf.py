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
import shutil
import subprocess
from docutils.parsers.rst import directives

from sphinx.util import logging
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

needs_role_need_template = "{title}"

needs_types = [dict(directive="role", title="Role", prefix="R_", color="#BFD8D2", style="node"),
               dict(directive="problem", title="Problem", prefix="P_", color="#cb5d7e", style="node"),
               dict(directive="solution", title="Solution", prefix="S_", color="#7dca5d", style="node"),
               dict(directive="tool", title="Tool", prefix="T_", color="#5d7ecb", style="node"),
               dict(directive="demo", title="Demo", prefix="D_", color="#cccccc", style="node"),
               ]

needs_flow_link_types = ['links', 'solves', 'uses']
needs_flow_show_links = True
needs_extra_links = [
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
    {   # Demo -> Solution
        "option": "demonstrates",
        "incoming": "demonstrated by",
        "outgoing": "demonstrates",
        "style": "bold,#cccccc",
    },

]

needs_layouts = {
    'scale_short': {
        'grid': 'content_footer',
        'layout': {
            # 'head': ['**<<meta("title")>>** (<<meta("id")>>)'],
            # 'meta': [],
            'footer': ['**ID**: <<meta_id()>>']
        }
    }
}

needs_id_regex = "^[A-Za-z0-9_]"
needs_id_required = True

needs_extra_options = {
    "path": directives.unchanged,  # Used by demo need
    "build_status": directives.unchanged,  # Used by demo need
    "build_path": directives.unchanged,  # Used by demo need
    "demo_path": directives.unchanged,  # Used by demo need
    "demo_conf": directives.unchanged,  # Used by demo need
}

needs_global_options = {
      # Without default value
      'template': [
            ('solution', 'type=="solution"'),
            ('demo', 'type=="demo"')
      ],
      'post_template': [
            ('post_solution', 'type=="solution"'),
            ('post_problem', 'type=="problem"'),
            ('post_demo', 'type=="demo"')
      ],
      'pre_template': [
            ('pre_scale', 'type in ["solution", "problem", "demo", "role"]')
      ],
      'layout': [
            ('scale_short', 'type in ["solution", "problem", "demo", "role"]')
      ],
      'style': [
            ('green_border', 'type=="solution"'),
            ('red_border', 'type=="problem"'),
            ('blue_border', 'type=="tool"')
      ],
      'build_status': [  # Starts the build of the demo
          ('[[build()]]', 'type=="demo"')
      ]
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


def build(env, need, needs):
    """
    Builds a sphinx-project in demos/ and copies the build-result to the current sphinx project
    build folder under "demos/demo-id".
    """
    log = logging.getLogger(__name__)

    demo_path = os.path.abspath(os.path.join(env.srcdir, need['path']))
    demo_conf = os.path.join(demo_path, 'conf.py')
    assert os.path.isfile(demo_conf)
    demo_build_html = os.path.join(demo_path, '_build', 'html')

    log.info(f'Building demo {need["id"]} at {demo_path}')

    # Start sphinx to build this demo
    exit_code = subprocess.call(f'sphinx-build -b html {demo_path} {demo_build_html}', shell=True)
    need['build_path'] = demo_build_html
    need['demo_path'] = f"/demos/{need['id']}/index.html"
    need['demo_conf'] = f"/demos/{need['id']}/conf.py"

    # Copy the demo html content to sphinx-scale outdir.
    scale_outdir = env.app.builder.outdir
    scale_demos = os.path.join(scale_outdir, 'demos/')
    scale_this_demo = os.path.join(scale_demos, need['id']+ '/')
    try:
        os.mkdir(scale_demos)
    except FileExistsError:
        pass

    try:
        os.mkdir(scale_this_demo)
    except FileExistsError:
        pass

    shutil.copytree(demo_build_html, scale_this_demo, dirs_exist_ok=True)

    return 'passed' if exit_code == 0 else 'failed'


needs_functions = [build]
