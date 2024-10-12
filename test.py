import unittest
from main import rest


class TestRest(unittest.TestCase):
    def test_rest(self):
        self.assertEqual(rest(10, 2), 0)
        self.assertEqual(rest(5, 3), 2)
        self.assertEqual(rest(35, 6), 5)

    def test_divide_by_zero(self):
        self.assertRaises(ValueError, rest, 6, 0)


if __name__ == '__main__':
    unittest.main()