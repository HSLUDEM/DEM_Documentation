# Configuration file for the Sphinx documentation builder.

# -- Project information

import os
from importlib.metadata import version as pkg_version, PackageNotFoundError

project = 'District Energy Model'
copyright = '2025, HSLU CC TES'
author = 'HSLU CC TES'

#release = '0.1'
#version = '0.1.0-alpha0'

# Try to get version info from Read the Docs
# e.g. 'latest', 'v0.1.0-alpha0', '0.2.1', etc.
rtd_version = os.environ.get("READTHEDOCS_VERSION_NAME") or os.environ.get("READTHEDOCS_VERSION")

if rtd_version:
    # Here you can decide how to map the RTD version string to Sphinx's
    # 'version' (short) and 'release' (full) fields.
    release = rtd_version
    # Take a short version up to first dash, or similar logic.
    # For 'v0.1.0-alpha0' this would give 'v0.1.0'
    version = rtd_version.split('-')[0]
else:
    # Local default when not on RTD
    release = '0.1.0-alpha0'
    version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx_togglebutton',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
# html_theme = 'classic'

# -- Options for EPUB output
epub_show_urls = 'footnote'

# Add this if not already defined
html_static_path = ['_static']

# Set the favicon
html_favicon = '_static/favicon.png'


# Inject custom CSS to increase page width
def setup(app):
    app.add_css_file('custom.css')