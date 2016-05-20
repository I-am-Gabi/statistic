# coding=utf-8
"""

"""

from mpmath import mp, log

from util.math_op import log_com, factorial


def dice(n, i):
    """
    p(X = i) = 1/n
    """
    return 1 / n


def dice_cdf(n, i):
    """
    p(X ≤ i)= i/n
    """
    return float(i) / float(n)


def geo(p, i):
    """
    p(X = i) = p·(1−p)^(i−1)
    """
    return p * (1 - p) ** (i - 1)


def geo_cdf(p, i):
    """
    p(X ≤ i) = 1−(1−p)^i
    """
    return 1 - (1 - p) ** i


def binomial(n, p, i):
    result_log = log_com(n, i) + i * log(p, 2) + (n - i) * log(1 - p, 2)
    return pow(2, result_log)


def binomial_cdf(n, p, i):
    prob = 0
    for j in range(0, i + 1):
        prob += binomial(n, p, j)
    return prob


def poisson(l, i):
    """
    p(X = i) = e^(−λ) · (λi · i!)
    """
    return mp.power(mp.e, -l) * (mp.power(l, i) / factorial(i))


def poisson_log(l, i):
    result_log = log(mp.power(mp.e, -l), 2) + log(mp.power(l, i), 2) - log(factorial(i), 2)
    return mp.power(2, result_log)


def poisson_cdf(l, i):
    prob = 0
    for j in range(0, i + 1):
        prob += poisson(l, j)
    return prob


# method main
if __name__ == '__main__':
    pass
