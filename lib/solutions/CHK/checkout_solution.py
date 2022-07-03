from typing import Dict

ITEM_IDENTIFIERS = {"A", "B", "C", "D"}


class PriceSpecs:
    @staticmethod
    def price_per_item(item):
        if item == "A":
            return 50
        elif item == "B":
            return 30
        elif item == "C":
            return 20
        elif item == "D":
            return 15
        elif item == "E":
            return 40


# class PriceDiscounter:
#     def __init__(self, items: Dict[str, int]):
#         self.items = items
#
#     def reduce_price(self, value):
#         value -= round((self.items["A"] - self.items["A"] % 5)*10
#                        - (self.items["A"] - self.items["A"] % 3)*6.7)
#         value -= round((self.items["B"] - self.items["B"] % 2)*7.5)
#         return value


class PriceCalculator:
    def __init__(self, items: Dict[str, int]):
        self.items = items

    def calculate_value(self):
        total_value = 0

        for item in self.items.keys():
            if item == "A":
                non_discounted_items_count = self.items[item] % 3
                total_value = total_value \
                              + (self.items[
                                     item] - non_discounted_items_count) / 3 \
                              * 130 \
                              + non_discounted_items_count * \
                              PriceSpecs.price_per_item(item)
            elif item == 'B':
                non_discounted_items_count = self.items[item] % 2
                total_value = total_value \
                              + (self.items[
                                     item] - non_discounted_items_count) / 2 \
                              * 45 \
                              + non_discounted_items_count \
                              * PriceSpecs.price_per_item(item)
            elif item == 'C':
                total_value = total_value + self.items[item] \
                              * PriceSpecs.price_per_item(item)
            elif item == 'D':
                total_value = total_value + self.items[item] \
                              * PriceSpecs.price_per_item(item)
        return total_value

    def reduce_item_count_based_on_other_items(self):
        number_of_b_items_to_reduce = (self.items["E"] - self.items["E"] % 2) \
                                      / 2
        final_number_of_items = self.items["B"] - number_of_b_items_to_reduce
        self.items["B"] = final_number_of_items if final_number_of_items > 0 \
            else 0

# noinspection PyUnusedLocal
# skus = unicode string
def parse_request(skus):
    item_list = dict.fromkeys(ITEM_IDENTIFIERS, 0)
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


