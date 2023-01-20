from base.config import DEFAULT_SPIDER_ATTRIBUTES, DEFAULT_ITEMS_ATTRIBUTES,\
    CURRENT_SPIDER_ATTRIBUTES, CURRENT_ITEMS_ATTRIBUTES
from copy import deepcopy


def meta_items_attributes_creator() -> dict:
    pass


def meta_spider_attributes_creator(current_spider=CURRENT_SPIDER_ATTRIBUTES,
                                   default_spider=DEFAULT_SPIDER_ATTRIBUTES) -> None:
    while True:
        print(f"Choose attribute number to change for you new Spider...\n Or type 'Exit' to return...")
        print(f"0. Set settings to default")
        for ind, key in enumerate(default_spider.keys()):
            print(f"{ind + 1}. {key}")
        print(current_spider)
        chosen_attribute = chose_attrib_number(default_spider)
        if type(chosen_attribute) == str:
            return
        if chosen_attribute >= 0:
            attribute_change(chosen_attribute, current_spider, default_spider)
        else:
            current_spider = deepcopy(default_spider)
        

def chose_attrib_number(parse_dict: dict) -> int | str:
    while True:
        try:
            chosen_attribute = input()
            if return_input_check(chosen_attribute, None, None, high_menu=True):
                return 'exit'
            chosen_attribute = int(chosen_attribute)
            if chosen_attribute > len(parse_dict.keys()) or chosen_attribute < 0:
                print('Please, type valid attribute Number...\n')
                continue
            return chosen_attribute - 1
        except ValueError:
            print('Type valid attribute Number, not a text...\n')
            continue


def attribute_change(key_index: int, current_spider, default_spider) -> None:
    attribute_name = list(current_spider)[key_index]

    if type(default_spider[attribute_name]) == list:
        list_handler(attribute_name, current_spider)
        return
    elif type(default_spider[attribute_name]) == dict:
        dict_handler(attribute_name, current_spider)
        return
    else:
        name_handler(attribute_name, current_spider)
        return


def name_handler(attribute_name: str, current_spider: dict) -> None:
    print('Type a name for you new spider, it should contain only alphabet letters, without numbers or symbols...\n'
          'Type Clear for clear this name, or Exit for go to select stage\n')
    while True:
        name = str(input()).lower().strip().replace(' ', '_')
        if return_input_check(name, attribute_name, current_spider):
            return
        if name.isalpha() and name.lower().strip() != 'clear':
            current_spider[attribute_name] = name
            print(f"Name is set to {name}, you can return to select stage by typing 'Exit', or select a new name...")
        else:
            print('You name is not valid, please use only alphabet letters...')


def list_handler(attribute_name: str, current_spider: dict) -> None:
    print('This attribute is a list, type different values to append to it...\n'
          'Type Clear for clear the list, or Exit for go to select stage\n')
    while True:
        attribute = str(input(f"Type different {attribute_name} for you new Spider\n")).strip().lower()
        if return_input_check(attribute, attribute_name, current_spider):
            return
        elif attribute.lower().strip() != 'clear':
            current_spider[attribute_name].append(attribute)


def dict_handler(attribute_name: str, current_spider: dict) -> None:
    print('This attribute is a css selector, type different values to append to it...\n'
          'Type Clear for clear this dictionary, or Exit for go to select stage\n')
    while True:
        if current_spider[attribute_name]:
            for key, value in current_spider[attribute_name].items():
                print(f"{key} : {value}")
        attribute_pair = str(input(f"Type <name, value> to update current selector or add new...\n"))
        if return_input_check(attribute_pair, attribute_name, current_spider):
            return
        elif attribute_pair.lower().strip() != 'clear':
            attribute_pair = dict([tuple(x.strip().lower() for x in attribute_pair.split(','))])
            current_spider[attribute_name].update(attribute_pair)


def return_input_check(input_result: str, attribute_name: str | None, current_spider: dict | None, high_menu=False) -> bool:
    if not high_menu:
        if input_result.lower().strip() == 'clear':
            current_spider[attribute_name].clear()
            return False
    if input_result.lower().strip() == 'exit':
        return True
    return False