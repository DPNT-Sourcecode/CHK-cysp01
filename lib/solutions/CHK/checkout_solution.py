ITEM_IDENTIFIERS = {"A", "B", "C", "D"}


# noinspection PyUnusedLocal
# skus = unicode string
def parse_request(skus):
    item_list = dict.fromkeys(ITEM_IDENTIFIERS, 0)
    if not isinstance(skus, str):
        return None
    for s in skus:
        if s.upper() not in item_list.keys():
            return None
        else:
            item_list[s.upper()] = item_list[s.upper()] + 1
    return item_list


def calculate_value(item_list):
    total_value = 0
    for item in item_list.keys():
        if item == "A":
            non_discounted_items_count = item_list[item] % 3
            total_value = total_value \
                          + (item_list[item] - non_discounted_items_count)/3 \
                          * 130 \
                          + non_discounted_items_count*50
        elif item == 'B':
            non_discounted_items_count = item_list[item] % 2
            total_value = total_value \
                          + (item_list[item] - non_discounted_items_count)/2 \
                          * 45 \
                          + non_discounted_items_count*30
        elif item == 'C':
            total_value = total_value + item_list[item] * 20
        elif item == 'D':
            total_value = total_value + item_list[item] * 15
    return total_value


def checkout(skus):
    item_list = parse_request(skus)
    if item_list:
        return calculate_value(item_list)
    return -1






