#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Oleksandr Kursik'
SITENAME = u'DataStories'  
#SITENAME = ''  
SITEURL =''

FAVICON = 'images/favicon.ico'
PATH = 'content'

TIMEZONE = 'Europe/Kiev'

#DEFAULT_LANG = u'uk'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#         )

# Social widget
SOCIAL = (('linkedin',  'https://www.linkedin.com/in/oleksandr-kursik'),
          ('facebook',   'https://www.facebook.com/olexandr.kursik'),
          ('github',  'https://github.com/alexikey'),
          )

DEFAULT_PAGINATION = 5


DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_TAGS_ON_SIDEBAR = True
TAG_CLOUD_MAX_ITEMS = 10
DISPLAY_PAGES_ON_MENU = False

#BOOTSTRAP_NAVBAR_INVERSE = True
#DISPLAY_TAGS_INLINE = True

MENUITEMS = (
     (u'Блог', '/'),
     (u'Про мене', '/pages/about.html'),
     (u'Контакти', '/pages/contact.html')
     
#     ('Email', 'http://www.google.com/recaptcha/mailhide/d?...'),
#     ('Vita', '/pdfs/HouserCV.pdf')
     )


# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False

# THEME
THEME = u"pelican-bootstrap3"
#BOOTSTRAP_THEME = 'simplex'
#BOOTSTRAP_THEME = 'spacelab'
#BOOTSTRAP_THEME = 'readable'
BOOTSTRAP_THEME = 'cerulean'
CUSTOM_CSS = 'static/custom.css'
BOOTSTRAP_FLUID = False


# To tell Pelican to copy the relevant file to the desired destination, 
# add the path to STATIC_PATHS and the destination to EXTRA_PATH_METADATA
STATIC_PATHS = ['figure', 'images','extra/custom.css']
# Tell Pelican to change the path to 'static/custom.css' in the output dir
EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/custom.css'}
}

# Plugin Setup
NOTEBOOK_DIR = 'notebooks'
PLUGIN_PATHS = ['/home/alex/virtualenvs/pelican/pelican-plugins']
PLUGINS = ['i18n_subsites','rmd_reader','tag_cloud','sitemap','summary','assets'
            # 'liquid_tags.img', 'liquid_tags.video',
            # 'liquid_tags.youtube', 'liquid_tags.vimeo',
            # 'liquid_tags.include_code', 'liquid_tags.notebook'
           ]
# Enable Jinja2 i18n extension used to parse translations.
JINJA_EXTENSIONS = ['jinja2.ext.i18n']


MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'headerid', 'toc']


RMD_READER_RENAME_PLOT = 'directory'
RMD_READER_KNITR_OPTS_CHUNK = {'fig.path': 'figure/'}


LOAD_CONTENT_CACHE = False
#Localize settings
# I18N_SUBSITES = {
#      'uk': {
#          'SITENAME': 'DataStories',
#          'LOCALE': u'uk_UA.utf8'
#          },
#      # 'en': {
#      #     'SITENAME': 'DataStories',
#      #     'LOCALE': 'en'
#      # }
# }

# DATE_FORMATS = {
#  	'en': ('en_US','%a, %d %b %Y'),
#   	'uk': (u'uk_UA.utf8','%a, %d %b %Y'),
# }

PYGMENTS_STYLE = 'zenburn'  
TYPOGRIFY = True
#IGNORE_FILES = ['	notes.md']

DISQUS_SITENAME = ''
DISQUS_NO_ID = True


# DISQUS_SECRET_KEY = u'YOUR_SECRET_KEY'
# DISQUS_PUBLIC_KEY = u'YOUR_PUBLIC_KEY'

#CEO
DISPLAY_BREADCRUMBS = True
DISPLAY_CATEGORY_IN_BREADCRUMBS = True


#Banner
BANNER = 'images/blue-computer-business-background-header.jpg'
#BANNER = 'f8386357ec7ebd1ffb50626a71ed1ed0-1  .png'
#BANNER_SUBTITLE = 'This is my subtitle'
BANNER_ALL_PAGES = True


#HEADER_IMAGE = "images/profile.jpg"
HIDE_SITENAME = True
#HIDE_SIDEBAR  = True
#SITELOGO = 'images/profile.jpg'

# Sitemap
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}