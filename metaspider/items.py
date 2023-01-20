# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags


def remove_spaces(value: str):
    return value.strip()


class MetaspiderItem(scrapy.Item):
    name = scrapy.Field(input_processor=MapCompose(remove_tags, remove_spaces), output_processor=TakeFirst())
    price = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    link = scrapy.Field(output_processor=TakeFirst())
