import os

os.environ["API_TOKEN"] = "187699580:AAE4bdqIwCZfnzfubp67ndCxEGdtLQbeQOc"
os.environ["API_WEATHERMAP"] = "aa43bb5d86018c18a7b62fa61654dbe5"

API_TIMEOUT = 60
RETRY_TIMEOUT = .3
RETRY_CODES = [429, 500, 502, 503, 504]
