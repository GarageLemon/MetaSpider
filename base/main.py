from base.config import DEFAULT_SPIDER_ATTRIBUTES, DEFAULT_ITEMS_ATTRIBUTES, process
from base.metaspider_creator import meta_spider_attributes_creator, meta_items_attributes_creator, chose_attrib_number
from metaspider.spiders.meta_spider import MetaSpider
from scrapy.crawler import CrawlerProcess


def make_new_spider_attribs():
    # meta_items_attributes_creator()
    meta_spider_attributes_creator()


def start_meta_crawler(process=process):
    process.crawl(MetaSpider)
    process.start()


def main_menu():
    menu_functions = {
        'Make New Spider': 'make_new_spider_attribs',
        'Start Crawler': 'start_meta_crawler'
    }
    print(f"Type a number of option you want to choose...\n"
          f"If you don't have any spiders, make one first before start parse...\n")
    while True:
        for ind, key in enumerate(menu_functions.keys()):
            print(f"{ind + 1}. {key}")
        choice = chose_attrib_number(menu_functions)
        if type(choice) == str:
            return
        choicen_name = list(menu_functions)[choice]
        func = globals()[menu_functions[choicen_name]]
        func()


if __name__ == '__main__':
    main_menu()