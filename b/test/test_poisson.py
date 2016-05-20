import unittest

from b.b1_poisson import poisson

from a.a2_loi_continues import normal_cdf


class TestStringMethods(unittest.TestCase):
    def test_dice_cdf(self):
        self.assertEqual(poisson(0.5, 0.1), 1.5)


if __name__ == '__main__':
    unittest.main()
