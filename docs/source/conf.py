# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'elsai-docs'
copyright = '2025, Optisol'
author = 'Optisol'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
    "pydata_sphinx_theme",
    "sphinx_multiversion",
     'sphinx_copybutton',
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_show_sourcelink = False
html_static_path = ['_static']

def setup(app):
    app.add_css_file("custom.css")
html_title = 'Elsai Docs'
html_context = {
    'display_github': True,
    'display_gitlab': False,
}

# Optional: pattern to include branches/tags
smv_tag_whitelist = r'^v\d+\.\d+.*$'  # Tags like v1.0
smv_branch_whitelist = r'^(main|master|dev)$'  # Branches to build
