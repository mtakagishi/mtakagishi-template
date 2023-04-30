# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'mtakagishi-template'
copyright = '2023, mtakagishi'
author = 'mtakagishi'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
    'sphinx.ext.todo',
    'sphinxcontrib.blockdiag',
    'sphinx_sitemap',
    'sphinxnotes.strike',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'jp'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_static_path = ['_static']

html_title = project
html_theme = "pydata_sphinx_theme"
html_logo = "_static/logo.png"

html_theme_options = {
    "logo": {
        "text": project,
    },
    "github_url": "https://github.com/mtakagishi/mtakagishi-template",
    "twitter_url": "https://twitter.com/mtakagishi",
}

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

[extensions]
todo_include_todos = True

# blockdiag
blockdiag_html_image_format = 'SVG'
blockdiag_fontpath = 'docs/_static/ipaexg.ttf'

# sphinx-sitemap
html_baseurl = 'https://mtakagishi-template.netlify.app/'
sitemap_url_scheme = "{link}"
sitemap_locales = [None]

html_extra_path = ['robots.txt', 'ads.txt']
