from copy import deepcopy
from scrapy.crawler import CrawlerProcess

DEFAULT_SPIDER_ATTRIBUTES = {
    'name': 'defaultspider',
    'allowed_domains': list(),
    'start_urls': list(),
    'css_selectors': dict()
}

DEFAULT_ITEMS_ATTRIBUTES = {
        'name': 'a.b-product__img::attr(title)',
        'price': 'span.discount-price::text' or 'span.discount-price.no-discount-price::text',
        'link': 'a.b-product__img::attr(href)'
}

CURRENT_SPIDER_ATTRIBUTES = deepcopy(DEFAULT_SPIDER_ATTRIBUTES)
CURRENT_ITEMS_ATTRIBUTES = dict()


process = CrawlerProcess(settings={
    "FEEDS": {
        "items.json": {"format": "json"},
    },
    'FEED_EXPORT_ENCODING': 'utf-8'
})


# attribs = {
#     'name': 'seeds_spider',
#     'allowed_domains': ['semena.ru'],
#     'start_urls': ['https://semena.ru/catalog/semena/ovoshchi/', 'https://semena.ru/catalog/kartofel-semennoy/'],
#     'css': {
#         'name': 'a.b-product__img::attr(title)',
#         'price': 'span.discount-price::text' or 'span.discount-price.no-discount-price::text',
#         'link': 'a.b-product__img::attr(href)'
#             }
# }