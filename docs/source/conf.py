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
    "sphinx.ext.autodoc",
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_theme_options = {
    "navbar_align": "content",
    "navbar_end": ["theme-switcher", "navbar-icon-links"],
    "navigation_with_keys": True,
    "show_toc_level": 2,
    "show_nav_level": 2,
    # Enable secondary sidebar for navigation within User Guide
    "secondary_sidebar_items": ["page-toc", "sourcelink"],
    "show_prev_next": True,
    # Clean navigation - only show User Guide in top nav
    "navbar_start": ["navbar-logo"],
    "navbar_center": ["navbar-nav"],
}

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

# MyST Parser configuration to help with toc generation
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "substitution",
    "tasklist",
]

# Ensure proper toctree depth
html_theme_options.update({
    "collapse_navigation": False,
    "sticky_navigation": True,
    "includehidden": True,
    "titles_only": False
})