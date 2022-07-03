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


def test_parse_request_given_request_without_letter():
    request = "AAB,"

    obtained_items = checkout_solution.parse_request(request)

    assert obtained_items is None


def test_parse_request_given_request_with_mixed_case():
    request = "AaBC"

    obtained_items = checkout_solution.parse_request(request)

    expected_items = {"A": 2, "B": 1, "C": 1, "D": 0}
    assert obtained_items == expected_items


def test_calculate_value_given_one_item_and_no_discount():
    given_items = {"A": 2, "B": 0, "C": 0, "D": 0}

    calc_value = checkout_solution.calculate_value(given_items)

    assert calc_value == 100


def test_calculate_value_given_one_item_and_only_discount():
    given_items = {"A": 3, "B": 0, "C": 0, "D": 0}

    calc_value = checkout_solution.calculate_value(given_items)

    assert calc_value == 130


def test_calculate_value_given_one_item_and_both_discount_and_not():
    given_items = {"A": 4, "B": 0, "C": 0, "D": 0}

    calc_value = checkout_solution.calculate_value(given_items)

    assert calc_value == 180


