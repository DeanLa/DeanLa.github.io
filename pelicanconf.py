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

DEFAULT_LANG = 'English'

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
LINKS = (('Pelican', 'http://getpelican.com/'),)

# Social widget
SOCIAL = (('Facebook', 'https://www.facebook.com/DeanLangsam'),
          ('LinkedIn', 'https://www.linkedin.com/in/deanla/'),
          ('Github','https://github.com/DeanLa'))

DEFAULT_PAGINATION = 10

PLUGIN_PATHS = ['pelican-plugins']

THEME = 'pelican-themes/pelican-bootstrap3'
BOOTSTRAP_THEME = 'flatly'

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
DIRECT_TEMPLATES = ('index','tags', 'categories', 'authors', 'archives', 'search')

# Custom CSS and JS
CUSTOM_CSS = 'static/css/custom.css'
CUSTOM_JS = 'static/js/custom.js'

STATIC_PATHS = [ 'extra' ]

EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/css/custom.css'},
    'extra/custom.js': {'path': 'static/js/custom.js'}
}
# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
