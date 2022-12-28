import unittest
import utils.helper_functions as helper_functions


class TestCliFunctions(unittest.TestCase):
    def test_add_x(self):
        self.assertEqual(helper_functions.add_x(2, 2), 4)


if __name__ == "__main__":
    unittest.main()
