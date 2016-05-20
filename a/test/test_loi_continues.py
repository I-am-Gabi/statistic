import unittest
import scipy.stats

from a.a2_loi_continues import normal_cdf, normal_pdf


class TestStringMethods(unittest.TestCase):
    def test_normal_pdf(self):
        self.assertEqual(normal_pdf(5, 5, 7), scipy.stats.norm(5, 5).pdf(7))

    def test_normal_cdf(self):
        self.assertEqual(round(normal_cdf(1000, 300, 10), 7), 4.834 * 10**(-4))
        self.assertEqual(normal_cdf(5, 5, 7), scipy.stats.norm(5, 5).cdf(7))


if __name__ == '__main__':
    unittest.main()
