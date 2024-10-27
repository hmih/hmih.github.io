AUTHOR = "Hristo Mihaylov"
SITENAME = "Thoughts"
SITEURL = "https://hmih.github.io"

RELATIVE_URLS = True
DELETE_OUTPUT_DIRECTORY = True

PATH = "content"

TIMEZONE = "Europe/Vienna"
DEFAULT_DATE_FORMAT = "%B %d, %Y"

DEFAULT_LANG = "en"
THEME = "theme"

ARTICLE_URL = ARTICLE_SAVE_AS = PAGE_URL = PAGE_SAVE_AS = "{slug}.html"


### disabled https://docs.getpelican.com/en/stable/settings.html#url-settings
DRAFT_URL = ""
DRAFT_SAVE_AS = ""
DRAFT_PAGE_URL = ""
DRAFT_PAGE_SAVE_AS = ""
AUTHOR_URL = ""
AUTHOR_SAVE_AS = ""
CATEGORY_URL = ""
CATEGORY_SAVE_AS = ""
TAG_URL = ""
TAG_SAVE_AS = ""
PAGE_URL = ""
PAGE_SAVE_AS = ""

ARCHIVES_SAVE_AS = ""
AUTHORS_SAVE_AS = ""
CATEGORIES_SAVE_AS = ""
TAGS_SAVE_AS = ""

FEED_ATOM = ""
FEED_ATOM_URL = ""
FEED_RSS = ""
FEED_RSS_URL = ""
FEED_ALL_ATOM = ""
FEED_ALL_ATOM_URL = ""
FEED_ALL_RSS = ""
FEED_ALL_RSS_URL = ""
CATEGORY_FEED_RSS = ""
CATEGORY_FEED_RSS_URL = ""
CATEGORY_FEED_ATOM = ""
CATEGORY_FEED_ATOM_URL = ""
AUTHOR_FEED_ATOM = ""
AUTHOR_FEED_ATOM_URL = ""
AUTHOR_FEED_RSS = ""
AUTHOR_FEED_RSS_URL = ""
TAG_FEED_ATOM = ""
TAG_FEED_ATOM_URL = ""
TAG_FEED_RSS = ""
TAG_FEED_RSS_URL = ""
TRANSLATION_FEED_ATOM = ""
TRANSLATION_FEED_ATOM_URL = ""
###

STATIC_PATHS = ["images", "static", "fonts"]

EXTRA_PATH_METADATA = {
    "static/robots.txt": {"path": "robots.txt"},
    "images/favicon.ico": {"path": "favicon.ico"},
}

SOCIAL = (("GitHub", "https://github.com/hmih"),)

SITEMETA = "All opinions are those of your employer"
