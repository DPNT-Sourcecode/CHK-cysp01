

# noinspection PyUnusedLocal
# skus = unicode string
def parse_request(skus):
    item_list = []
    if not isinstance(skus, str):
        return None



def checkout(skus):
    item_list = parse_request(skus)
    raise NotImplementedError()


