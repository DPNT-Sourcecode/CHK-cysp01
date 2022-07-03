from solutions.CHK import checkout_solution


def test_parse_request_given_uppercase_and_existing_items():
    request = "AABC"

    obtained_items = checkout_solution.parse_request(request)

    expected_items = {"A": 2, "B": 1, "C": 1, "D": 0}
    assert obtained_items == expected_items


def test_parse_request_given_non_existing_item_identifier():
    request = "AABCE"

    obtained_items = checkout_solution.parse_request(request)

    assert obtained_items is None
