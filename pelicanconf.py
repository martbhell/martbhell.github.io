import os

AUTHOR = 'Johan Guldmyr'
SITENAME = 'There is IT in Helsinki'
SITEURL = os.getenv('SITE_URL', '')

PATH = 'content'

TIMEZONE = 'Europe/Helsinki'

DEFAULT_LANG = 'en'

DEFAULT_DATE_FORMAT = '%Y-%m-%d'

SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.5,
        "indexes": 0.5,
        "pages": 0.5
    },
    "changefreqs": {
        "articles": "monthly",
        "indexes": "daily",
        "pages": "monthly"
    }
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = "atom.xml"
FEED_MAX_ITEMS = 20
CATEGORY_FEED_ATOM = "{slug}.atom.xml"
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll - opens in new window
LINKS = (
         ('Was There an NHL Game Yesterday?', 'https://wtangy.se'),
         )

FOOTER_LINKS = (
         ('Tags', 'tags/'),
         ('Categories', 'categories/'),
         ('Recipes in Finnish', 'tag/resepti'),
         )

# Social widget
SOCIAL = (('martbhell', 'https://twitter.com/martbhell'),
          )

ICONS = (
        ('twitter', 'https://twitter.com/martbhell'),
        ('rss', 'atom.xml'),
        ('github', 'https://github.com/martbhell'),
          )


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

GOOGLE_ANALYTICS = os.getenv('GOOGLE_ANALYTICS')

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        # This is for enabling the TOC generation
        "markdown.extensions.toc": {"title": "Table of Contents"},
    },
    'output_format': 'html5',
}

import alchemy
THEME = alchemy.path()
HIDE_AUTHORS = True
SITEIMAGE = '/images/blog_site_image_small.webp'
STATIC_PATHS = ['extras']

EXTRA_PATH_METADATA = {
    'extras/android-chrome-192x192.png': {'path': 'android-chrome-192x192.png'},
    'extras/android-chrome-512x512.png': {'path': 'android-chrome-512x512.png'},
    'extras/apple-touch-icon.png': {'path': 'apple-touch-icon.png'},
    'extras/favicon-16x16.png': {'path': 'favicon-16x16.png'},
    'extras/favicon-32x32.png': {'path': 'favicon-32x32.png'},
    'extras/favicon.ico': {'path': 'favicon.ico'},
    'extras/manifest.json': {'path': 'manifest.json'},
}

#TEMPLATE_PAGES = {'src/tag-cloud.html': 'posts/tag-cloud.html'}
