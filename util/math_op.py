import math
from mpmath import mp, log


def comb(n, k):
    return mp.factorial(n) / (mp.factorial(k) * mp.factorial(n - k))


def log_com(n, k):
    return log(factorial(n), 2) - (log(factorial(k), 2) + log(factorial(n - k), 2))


def factorial(x):
    res = 1
    for i in xrange(2, x + 1):
        res *= i
    return res


def pow_high_value(p, i):
    return math.log(p) * math.log(i)