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


def checkout(skus):
    item_list = parse_request(skus)
    raise NotImplementedError()

