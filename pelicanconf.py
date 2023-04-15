AUTHOR = 'Johan Guldmyr'
SITENAME = 'There is IT in Helsinki'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Helsinki'

DEFAULT_LANG = 'en'

DEFAULT_DATE_FORMAT = '"%Y-%m-%d"'

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
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
         ('Was There an NHL Game Yesterday?', 'https://wtangy.se'),
         )

# Social widget
SOCIAL = (('martbhell', 'https://twitter.com/martbhell'),
          )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

GOOGLE_ANALYTICS = "G-H4LG7R6ZGG"
