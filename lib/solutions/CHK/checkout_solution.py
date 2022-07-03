from typing import Dict


class ItemReducer:
    def __init__(self, item, quantity):
        self.item = item
        self.quantity = quantity


class GroupDiscount:
    def __init__(self, items_list, quantity, group_discount_price):
        self.items_list = items_list
        self.quantity = quantity
        self.group_discount_price = group_discount_price


class PriceSpecs:
    def __init__(
            self, price, quantity_discounts=None, item_reducer=None, free_item=0):
        self.price = price
        self.quantity_discounts = quantity_discounts
        self.item_reducer = item_reducer
        self.free_item = free_item


GROUP_DISCOUNTS = [GroupDiscount(["S", "T", "X", "Y", "Z"], 3, 45)]


ITEMS = {"A": PriceSpecs(50, quantity_discounts={5: 200, 3: 130}),
         "B": PriceSpecs(30, quantity_discounts={2: 45}),
         "C": PriceSpecs(20),
         "D": PriceSpecs(15),
         "E": PriceSpecs(40, item_reducer=ItemReducer("B", 2)),
         "F": PriceSpecs(10, free_item=3),
         "G": PriceSpecs(20),
         "H": PriceSpecs(10, quantity_discounts={10: 80, 5:45}),
         "I": PriceSpecs(35),
         "J": PriceSpecs(60),
         "K": PriceSpecs(70, quantity_discounts={2: 150}),
         "L": PriceSpecs(90),
         "M": PriceSpecs(15),
         "N": PriceSpecs(40, item_reducer=ItemReducer("M", 3)),
         "O": PriceSpecs(10),
         "P": PriceSpecs(50, quantity_discounts={5: 200}),
         "Q": PriceSpecs(30, quantity_discounts={3: 80}),
         "R": PriceSpecs(50, item_reducer=ItemReducer("Q", 3)),
         "S": PriceSpecs(20),
         "T": PriceSpecs(20),
         "U": PriceSpecs(40, free_item=4),
         "V": PriceSpecs(50, quantity_discounts={3: 130, 2: 90}),
         "W": PriceSpecs(20),
         "X": PriceSpecs(17),
         "Y": PriceSpecs(20),
         "Z": PriceSpecs(21)}


class PriceCalculator:
    def __init__(self, items: Dict[str, int]):
        self.items = items

    def calculate_value(self):
        total_value = 0
        self.reduce_item_count_based_on_other_items()
        for item in self.items.keys():
            if ITEMS[item].quantity_discounts:
                non_discounted_number = self.items[item]
                number_of_items = self.items[item]
                for disc_quan in ITEMS[item].quantity_discounts.keys():
                    non_discounted_number = number_of_items % disc_quan
                    total_value += (number_of_items - non_discounted_number) \
                                   / disc_quan \
                                   * ITEMS[item].quantity_discounts[disc_quan]
                    if number_of_items - non_discounted_number > 0:
                        number_of_items = non_discounted_number
                total_value += non_discounted_number*ITEMS[item].price
            else:
                total_value = total_value + self.items[item] \
                              * ITEMS[item].price
        return self.reduce_price_for_group_discount(total_value)

    def reduce_item_count_based_on_other_items(self):
        for item in self.items.keys():
            if ITEMS[item].item_reducer:
                item_to_reduce = ITEMS[item].item_reducer.item
                number_of_items_to_reduce = (self.items[item] - self.items[item]
                                             % ITEMS[item].item_reducer.quantity)\
                                            /ITEMS[item].item_reducer.quantity
                final_number_of_items = self.items[item_to_reduce] \
                                        - number_of_items_to_reduce
                self.items[item_to_reduce] = final_number_of_items \
                    if final_number_of_items > 0 else 0
            if ITEMS[item].free_item > 0:
                number_of_free_items_to_reduce = int(self.items[item]
                                                  / ITEMS[item].free_item)

                self.items[item] = self.items[item] \
                                   - number_of_free_items_to_reduce

    def reduce_price_for_group_discount(self, total_value):
        for group_disc in GROUP_DISCOUNTS:
            reduced_item_list = dict((k, self.items[k])
                                     for k, v in self.items.keys()
                                     if k in group_disc.items_list)
            for key
            reduced_item_list_sorted = {key: value for key, value in sorted(reduced_item_list.items(), key=lambda item: item[1])})
            total_items_for_group_disc = 0
            for item in group_disc.items_list:
                total_items_for_group_disc += reduced_item_list[item]
            if total_items_for_group_disc % group_disc.quantity > 0:


# noinspection PyUnusedLocal
# skus = unicode string
def parse_request(skus):
    item_list = dict.fromkeys(ITEMS, 0)
    if not isinstance(skus, str):
        return None
    for s in skus:
        if s not in item_list.keys():
            return None
        else:
            item_list[s] = item_list[s] + 1
    return item_list


def checkout(skus):
    item_list = parse_request(skus)
    if item_list:
        return PriceCalculator(item_list).calculate_value()
    return -1


