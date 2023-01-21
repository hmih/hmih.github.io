AUTHOR = "Hristo Mihaylov"
SITENAME = "hris.to"
SITETITLE = "Thoughts"
SITEURL = ""

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
    "static/robots.txt": {"path": "robots.txt"},
    "images/favicon.ico": {"path": "favicon.ico"},
}

SOCIAL = (("GitHub", "https://github.com/hmih"),)

SITEMETA = "All opinions are those of your employer"
