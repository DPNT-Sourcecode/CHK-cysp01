from typing import Dict

class ItemReducer:
    def __init__(self, item, quantity):
        self.item = item
        self.quantity = quantity

class PriceSpecs:
    def __init__(self, price, quantity_discounts=None, item_reducer=None, free_item=0):
        self.price = price
        self.quantity_discounts = quantity_discounts
        self.item_reducer = item_reducer
        self.free_item = free_item


ITEMS = {"A": PriceSpecs(50, {5: 200, 3: 130}),
         "B": PriceSpecs(30, {2: 45}),
         "C": PriceSpecs(20),
         "D": PriceSpecs(15),
         "E": PriceSpecs(40, item_reducer=ItemReducer("B", 2)),
         "F": PriceSpecs(10, item_reducer=3), "G": 20,
                    "H": 10, "I": 35, "J": 60, "K": 80, "L": 90, "M": 50, "N": 40,
                    "O":10, "P":50, "Q": 30, "R": 50, "S":30, "T": 20, "U": 40,
                    "V": 50, "W": 20, "X": 90, "Y": 10, "Z": 50}


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
        return total_value

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
                number_of_items_to_reduce = int(self.items[item]
                                                  / ITEMS[item].free_item)

                self.items[item] = self.items[item] - number_of_items_to_reduce
        # if "F" in self.items.keys() and self.items["F"] > 2:
        #     number_of_f_items_to_reduce = int(self.items["F"] / 3)
        #     self.items["F"] = self.items["F"] - number_of_f_items_to_reduce


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





