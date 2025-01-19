import unittest

from langfarm_tracing import adder3


class MyTestCase(unittest.TestCase):
    def test_add_3(self):
        a = adder3.add3(1, 2, 3)
        assert a == 6


if __name__ == "__main__":
    unittest.main()
