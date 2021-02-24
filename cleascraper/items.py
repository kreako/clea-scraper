# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from datetime import datetime


class RecipeItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    categories = scrapy.Field()
    text = scrapy.Field()
    dt = scrapy.Field()
