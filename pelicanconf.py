AUTHOR = 'Pioner palace'
SITENAME = 'Дворец пионеров'
SITEURL = ""

PATH = "content"
STATIC_PATHS = ['static']
THEME = 'themes/palace'


TIMEZONE = 'Europe/Moscow'

DEFAULT_LANG = 'ru'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 30

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# pelicanconf.py
ARTICLE_SAVE_AS = 'courses/{slug}.html'
ARTICLE_URL = 'courses/{slug}.html'
ARTICLE_LANG_SAVE_AS = 'courses/{slug}.html'

# Указываем шаблон для статей (курсов)
ARTICLE_TEMPLATE = 'course.html'

PAGE_PATHS = ['pages', 'magazines']
PAGE_SAVE_AS = '{slug}.html'
PAGE_URL = '{slug}.html'

# pelicanconf.py

# Включаем Markdown
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},          # ← важно! включает списки, таблицы, сноски
        'markdown.extensions.meta': {},           # ← важно! для чтения метаданных
    },
    'output_format': 'html5',
}