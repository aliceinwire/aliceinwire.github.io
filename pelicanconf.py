#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'arisut'
SITENAME = "Arisut's website"
SITETITLE = "Arisut's website"
SITESUBTITLE = 'Gentoo Kernel Project Leader'
SITEURL = 'https://aliceinwire.github.io/blog/'
SITELOGO = SITEURL + '/images/profile.png'
FAVICON = SITEURL + '/images/favicon.ico'

PATH = 'content'

TIMEZONE = 'Asia/Tokyo'

THEME = "theme"

DEFAULT_LANG = 'en'

MAIN_MENU = True

STATIC_PATHS = ['images', 'extra']

EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    }

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Gentoo', 'https://wiki.gentoo.org/wiki/User:Alicef'),
         ('rss', '//aliceinwire.github.io/blog/feeds/all.atom.xml'))

# Social widget
SOCIAL = (('mastodon', 'https://fosstodon.org/@alicef'),
        ('rss', 'https://aliceinwire.github.io/blog/feeds/all.atom.xml'))

DEFAULT_PAGINATION = 10

DEFAULT_METADATA = {
    'status': 'draft',
}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Pigment config
PYGMENTS_STYLE = 'monokai'

PLUGIN_PATHS = ['plugins/']
PLUGINS = ['pelican_comment_system']

PELICAN_COMMENT_SYSTEM = True
PELICAN_COMMENT_SYSTEM_IDENTICON_DATA = ('author',)
PELICAN_COMMENT_SYSTEM_DIR = '../comments'
