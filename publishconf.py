#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *


# don't delete our .git submodule dir
DELETE_OUTPUT_DIRECTORY = False

# use the correct abs url
SITEURL = 'https://datareview.github.io'
RELATIVE_URLS = False


FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

# Following items are often useful when publishing
DISQUS_SITENAME = 'alexikey-github-io'
DISQUS_NO_ID = True
#GOOGLE_ANALYTICS = ""
