from typing import Dict


class PriceCalculator:
    ITEM_IDENTIFIERS = {"A", "B", "C", "D"}

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
                              + non_discounted_items_count * 50
            elif item == 'B':
                non_discounted_items_count = self.items[item] % 2
                total_value = total_value \
                              + (self.items[
                                     item] - non_discounted_items_count) / 2 \
                              * 45 \
                              + non_discounted_items_count * 30
            elif item == 'C':
                total_value = total_value + self.items[item] * 20
            elif item == 'D':
                total_value = total_value + self.items[item] * 15
        return total_value


# noinspection PyUnusedLocal
# skus = unicode string
def parse_request(skus):
    item_list = dict.fromkeys(PriceCalculator.ITEM_IDENTIFIERS, 0)
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
        return PriceCalculator.calculate_value(item_list)
    return -1




