from typing import Dict


class PriceSpecs:
    def __init__(self, price, quantity_discounts={}, item_reducer=''):
        self.price = price
        self.quantity_discounts = quantity_discounts
        self.item_reducer = item_reducer


ITEMS = {"A": PriceSpecs(50, {5: 200, 3: 130}),
         "B": PriceSpecs(30, {2: 45}),
         "C": PriceSpecs(20),
         "D": PriceSpecs(15),
         "E": PriceSpecs(40),
         "F": PriceSpecs(10), "G": 20,
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
                        number_of_items = number_of_items - non_discounted_number
                total_value += non_discounted_number*ITEMS[item].price
                # non_discounted_items_max_disc = self.items[item] % 5
                # non_discounted_items_count = (non_discounted_items_max_disc) % 3
                #
                # total_value = total_value \
                #               + (self.items[item]
                #                  - non_discounted_items_max_disc) \
                #               / 5 \
                #               * 200 \
                #               + (non_discounted_items_max_disc
                #                  - non_discounted_items_count) / 3 \
                #               * 130 \
                #               + non_discounted_items_count * \
                #               ITEMS[item].price
            # elif item == 'B':
            #     non_discounted_items_count = self.items[item] % 2
            #     total_value = total_value \
            #                   + (self.items[
            #                          item] - non_discounted_items_count) / 2 \
            #                   * 45 \
            #                   + non_discounted_items_count \
            #                   * ITEMS[item].price
            else:
                total_value = total_value + self.items[item] \
                              * ITEMS[item].price
        return total_value

    def reduce_item_count_based_on_other_items(self):
        number_of_b_items_to_reduce = (self.items["E"] - self.items["E"] % 2) \
                                      / 2
        final_number_of_items = self.items["B"] - number_of_b_items_to_reduce
        self.items["B"] = final_number_of_items if final_number_of_items > 0 \
            else 0
        if "F" in self.items.keys() and self.items["F"] > 2:
            number_of_f_items_to_reduce = int(self.items["F"] / 3)
            self.items["F"] = self.items["F"] - number_of_f_items_to_reduce


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








