import unittest

from hypothesis import given
from hypothesis import strategies as st

import utils.helper_functions as helper_functions


class TestCliFunctions(unittest.TestCase):
    @given(
        st.floats(
            min_value=-100,
            max_value=100,
            width=16,
            allow_infinity=False,
            allow_subnormal=False,
        ),
        st.floats(
            min_value=-100,
            max_value=100,
            width=16,
            allow_infinity=False,
            allow_subnormal=False,
        ),
    )
    def test_add_x(self, x, y):
        self.assertEqual(helper_functions.add_x(x, y), x + y)


if __name__ == "__main__":
    unittest.main()
