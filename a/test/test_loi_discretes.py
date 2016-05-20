import unittest

from a.a1_loi_discretes import dice_cdf, geo_cdf, binomial_cdf, poisson_cdf, binomial, poisson


class TestStringMethods(unittest.TestCase):
    def test_dice_cdf(self):
        self.assertEqual(dice_cdf(10, 15), 1.5)

    def test_geo_cdf(self):
        self.assertEqual(round(geo_cdf(0.1, 10), 6), 0.651322)

    def test_binomial_cdf(self):
        self.assertEqual(round(binomial_cdf(10, 0.3, 3), 4), 0.6496)
        self.assertEqual(round(binomial_cdf(2, 0.25, 0), 4), 0.5625)
        self.assertEqual(round(binomial_cdf(2, 0.25, 1), 4), 0.9375)

    def test_binomial(self):
        self.assertEqual(round(binomial(2, 0.25, 2), 4), 0.0625)

    def test_poisson(self):
        self.assertEqual(round(poisson(0.5, 0), 3), 0.607)
        self.assertEqual(round(poisson(0.5, 1), 3), 0.303)
        self.assertEqual(round(poisson(0.5, 2), 3), 0.076)

    def test_poisson_cdf(self):
        self.assertEqual(round(poisson_cdf(0.5, 0), 3), 0.607)
        self.assertEqual(round(poisson_cdf(0.5, 1), 3), 0.910)
        self.assertEqual(round(poisson_cdf(0.5, 2), 3), 0.986)

if __name__ == '__main__':
    unittest.main()
