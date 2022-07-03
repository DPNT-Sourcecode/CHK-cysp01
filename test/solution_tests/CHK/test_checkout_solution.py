from solutions.CHK import checkout_solution


def test_parse_request_given_uppercase_and_existing_items():
    request = "AABC"

    obtained_items = checkout_solution.parse_request(request)

    expected_items = dict.fromkeys(checkout_solution.ITEMS, 0)
    expected_items["A"] = 2
    expected_items["B"] = 1
    expected_items["C"] = 1
    assert obtained_items == expected_items


def test_parse_request_given_request_without_letter():
    request = "AAB,"

    obtained_items = checkout_solution.parse_request(request)

    assert obtained_items is None


def test_parse_request_given_request_with_mixed_case():
    request = "AaBC"

    obtained_items = checkout_solution.parse_request(request)

    assert obtained_items is None


def test_calculate_value_given_item_a_and_no_discount():
    given_items = {"A": 2, "B": 0, "C": 0, "D": 0, "E": 0}

    calc_value = checkout_solution.PriceCalculator(given_items).calculate_value()

    assert calc_value == 100


def test_calculate_value_given_item_a_and_only_small_discount():
    given_items = {"A": 3, "B": 0, "C": 0, "D": 0, "E": 0}

    calc_value = checkout_solution.PriceCalculator(given_items).calculate_value()

    assert calc_value == 130


def test_calculate_value_given_item_a_and_only_big_discount():
    given_items = {"A": 5, "B": 0, "C": 0, "D": 0, "E": 0}

    calc_value = checkout_solution.PriceCalculator(given_items).calculate_value()

    assert calc_value == 200


def test_calculate_value_given_item_a_and_both_discount_and_not():
    given_items = {"A": 4, "B": 0, "C": 0, "D": 0, "E": 0}

    calc_value = checkout_solution.PriceCalculator(given_items).calculate_value()

    assert calc_value == 180


def test_calculate_value_given_item_a_and_two_discounts_and_not():
    given_items = {"A": 9, "B": 0, "C": 0, "D": 0, "E": 0}

    calc_value = checkout_solution.PriceCalculator(given_items).calculate_value()

    assert calc_value == 380


def test_calculate_value_given_item_b_and_no_discount():
    given_items = {"A": 0, "B": 1, "C": 0, "D": 0, "E": 0}

    calc_value = checkout_solution.PriceCalculator(given_items).calculate_value()

    assert calc_value == 30


def test_calculate_value_given_item_b_and_only_discount():
    given_items = {"A": 0, "B": 2, "C": 0, "D": 0, "E": 0}

    calc_value = checkout_solution.PriceCalculator(given_items).calculate_value()

    assert calc_value == 45


def test_calculate_value_given_item_b_and_both_discount_and_not():
    given_items = {"A": 0, "B": 5, "C": 0, "D": 0, "E": 0}

    calc_value = checkout_solution.PriceCalculator(given_items).calculate_value()

    assert calc_value == 120


def test_calculate_value_given_item_c():
    given_items = {"A": 0, "B": 0, "C": 2, "D": 0, "E": 0}

    calc_value = checkout_solution.PriceCalculator(given_items).calculate_value()

    assert calc_value == 40


def test_calculate_value_given_item_d():
    given_items = {"A": 0, "B": 0, "C": 0, "D": 2, "E": 0}

    calc_value = checkout_solution.PriceCalculator(given_items).calculate_value()

    assert calc_value == 30


def test_calculate_value_given_item_e_no_b():
    given_items = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 1}

    calc_value = checkout_solution.PriceCalculator(given_items).calculate_value()

    assert calc_value == 40


def test_calculate_value_given_item_e_and_b_but_no_discount():
    given_items = {"A": 0, "B": 1, "C": 0, "D": 0, "E": 1}

    calc_value = checkout_solution.PriceCalculator(given_items).calculate_value()

    assert calc_value == 70


def test_calculate_value_given_item_e_and_b_and_discount():
    given_items = {"A": 0, "B": 1, "C": 0, "D": 0, "E": 2}

    calc_value = checkout_solution.PriceCalculator(given_items).calculate_value()

    assert calc_value == 80


def test_calculate_value_given_item_f_no_discount():
    given_items = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 1}

    calc_value = checkout_solution.PriceCalculator(given_items).calculate_value()

    assert calc_value == 10


def test_calculate_value_given_item_f_and_two_items():
    given_items = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 2}

    calc_value = checkout_solution.PriceCalculator(given_items).calculate_value()

    assert calc_value == 20


def test_calculate_value_given_item_f_and_discount_one_item():
    given_items = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 5}

    calc_value = checkout_solution.PriceCalculator(given_items).calculate_value()

    assert calc_value == 40


def test_calculate_value_given_item_f_and_discount_two_items():
    given_items = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 6}

    calc_value = checkout_solution.PriceCalculator(given_items).calculate_value()

    assert calc_value == 40


def test_checkout_given_valid_request():
    request = "ABAACBAD"

    calc_value = checkout_solution.checkout(request)

    assert calc_value == 260


def test_checkout_given_invalid_request():
    request = "ABAACBAD+"

    calc_value = checkout_solution.checkout(request)

    assert calc_value == -1


def test_checkout_given_group_discount():
    request = "SSTXYZZZ"

    calc_value = checkout_solution.checkout(request)

    assert calc_value == 137


def test_checkout_given_group_discount_susbset_of_items():
    request = "SSTXY"

    calc_value = checkout_solution.checkout(request)

    assert calc_value == 82
