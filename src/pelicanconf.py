#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Aleksander Alekseev'
SITENAME = "Aleksander Alekseev's blog"
SITEURL = 'https://afiskon.github.io'

PATH = 'content'

TIMEZONE = 'UTC'

DEFAULT_LANG = 'en'

DISQUS_SITENAME = 'afiskon'

#DISPLAY_PAGES_ON_MENU = True
#PAGE_PATHS = ['pages']

#PAGES = (
#  ("About me", "pages/about.html"),
#)

# THEME = 'pelican-simplegrey'

# Feed generation is usually not desired when developing
FEED_ALL_RSS = 'rss/all.xml'
CATEGORY_FEED_RSS = 'rss/%s.xml'
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_CATEGORY = 'General'

LINKS = (
  ('About me', 'pages/about.html'),
#  ('You can modify those links in your config file', '#'),
)

# Social widget
SOCIAL = (
  ('Twitter', 'https://twitter.com/afiskon'),
  ('GitHub', 'https://github.com/afiskon'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
