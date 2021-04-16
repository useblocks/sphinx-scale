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
import sys
import subprocess
import shutil

sys.path.append(os.path.abspath("."))


# -- Project information -----------------------------------------------------

project = 'Demo C++ API with Doxygen'
copyright = '2021, sphinx-scale community'
author = 'sphinx-scale community'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinxcontrib.plantuml', 'sphinxcontrib.needs', 'breathe']


breathe_projects = {"doxygen_example": "_build/doxygen/xml"}
breathe_default_project = "doxygen_example"
if shutil.which("doxygen") and \
        not os.environ.get("SKIP_DOXYGEN", None) == "True":
    for prjname, prjdir in breathe_projects.items():
        print("Generating doxygen files for {}...".format(prjname))
        os.makedirs(prjdir, exist_ok=True)
        cmd = "cd code && doxygen {}.dox".format(prjname)
        subprocess.call(cmd, shell=True)
else:
    for prjname, prjdir in breathe_projects.items():
        assert os.path.exists(prjdir) is True, \
            "Regenerate doxygen XML for {}".format(prjname)

# PLANTUML config

on_rtd = os.environ.get('READTHEDOCS') == 'True'
cwd = os.getcwd()
local_plantuml_path = os.path.join(cwd, "../../docs/utils/plantuml.jar")

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
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
