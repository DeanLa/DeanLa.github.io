#!/usr/bin/env python
# -*- coding: utf-8 -*- #
# from __future__ import unicode_literals

AUTHOR = 'Dean Langsam'
SITENAME = 'DeanLa'
SITEURL = ''

PATH = 'content'
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['posts']

TIMEZONE = 'Asia/Jerusalem'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Display
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = True

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),)
LINKS = ()

# Social
SOCIAL = (
    ('', 'https://www.facebook.com/DeanLangsam','Facebook'),
    ('LinkedIn', 'https://www.linkedin.com/in/deanla/'),
    ('Github', 'https://github.com/DeanLa')
)

USE_OPEN_GRAPH = True
OPEN_GRAPH_FB_APP_ID = 259760160731955
TWITTER_CARDS = True

#
DEFAULT_PAGINATION = 10

PLUGIN_PATHS = ['pelican-plugins']

THEME = 'pelican-bootstrap3'
BOOTSTRAP_THEME = 'united'

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
PLUGINS = [
    'i18n_subsites',
    'series',
    'tag_cloud',
    'liquid_tags.youtube',
    'liquid_tags.notebook',
    'liquid_tags.include_code',
    'render_math',
    'pelican-ipynb.markup',
    'tipue_search']

I18N_TEMPLATES_LANG = 'en'
DIRECT_TEMPLATES = ('index', 'tags', 'categories', 'authors', 'archives', 'search')

# Custom CSS and JS
CUSTOM_CSS = 'static/css/custom.css'
CUSTOM_JS = 'static/js/custom.js'
PYGMENTS_STYLE = 'monokai'

STATIC_PATHS = ['extra', 'apps','img']

EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/css/custom.css'},
    'extra/custom.js': {'path': 'static/js/custom.js'},
    'extra/CNAME': {'path': 'CNAME'},
    'apps': {'path': 'apps'},

}
# Uncomment following line if you want document-relative URLs when developing
# SITEURL = 'http://deanla.com'
# RELATIVE_URLS = True

SHOW_ARTICLE_AUTHOR = True
LOAD_CONTENT_CACHE = False
DISPLAY_BREADCRUMBS = False

BANNER = 'img/intro-bg-narrow.jpg'
BANNER_SUBTITLE = ''
BANNER_ALL_PAGES = True

DISPLAY_ARTICLE_INFO_ON_INDEX = True