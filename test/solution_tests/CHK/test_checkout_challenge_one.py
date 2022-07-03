import unittest
from solutions import CHK


class MyTestCase(unittest.TestCase):
    def test_parse_request_given_uppercase_and_valid_letters(self):
        request = "AABC"

        # item_list = CHK.parse_request(request)
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()

