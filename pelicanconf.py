AUTHOR = "Hristo Mihaylov"
SITENAME = "Thoughts"
SITEURL = "https://blog.hris.to"

RELATIVE_URLS = False
DELETE_OUTPUT_DIRECTORY = True

PATH = "content"

TIMEZONE = "Europe/Vienna"
DEFAULT_DATE_FORMAT = "%B %d, %Y"

DEFAULT_LANG = "en"
THEME = "theme"

PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"
ARTICLE_URL = "{slug}/"
ARTICLE_SAVE_AS = "{slug}/index.html"

STATIC_PATHS = ["images", "static", "fonts"]

EXTRA_PATH_METADATA = {
    "static/CNAME": {"path": "CNAME"},
    "static/robots.txt": {"path": "robots.txt"},
    "images/favicon.ico": {"path": "favicon.ico"},
}

SOCIAL = (("GitHub", "https://github.com/hmih"),)

SITEMETA = "All opinions are those of your employer"
