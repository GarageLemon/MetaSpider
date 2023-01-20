import scrapy
from metaspider.items import MetaspiderItem
from scrapy.loader import ItemLoader
from base.config import CURRENT_ITEMS_ATTRIBUTES, CURRENT_SPIDER_ATTRIBUTES


class Meta(type):
    def __new__(cls, name, base, attrs):
        attrs.update(CURRENT_SPIDER_ATTRIBUTES)
        return type.__new__(cls, name, base, attrs)


class MetaSpider(scrapy.Spider, metaclass=Meta):
    # name = 'seeds_spider'
    # allowed_domains = ['semena.ru']
    # start_urls = ['https://semena.ru/catalog/semena/ovoshchi/', 'https://semena.ru/catalog/kartofel-semennoy/']

    def parse(self, response):
        for products in response.css('div.b-product'):
            product = ItemLoader(item=MetaspiderItem(), selector=products)
            for item, pattern in self.css_selectors.items():
                product.add_css(item, pattern)
            # product.add_css('name', 'a.b-product__img::attr(title)')
            # product.add_css('price', 'span.discount-price::text' or 'span.discount-price.no-discount-price::text')
            # product.add_css('link', 'a.b-product__img::attr(href)')

            yield product.load_item()
