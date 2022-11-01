# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'OpenL'
release = '5.26'
author = 'OpenL team'
version = 'doc version 1'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'myst_parser',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# The _static folder must be in the docs folder. Files here are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# A list of CSS files. The entry must be a filename string or a tuple containing
# the filename string and the attributes dictionary. The filename must be
# relative to the html_static_path, or a full URI
html_css_files = ["custom.css"]

# -- Options for EPUB output
epub_show_urls = 'footnote'
