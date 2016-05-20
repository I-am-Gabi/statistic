from mpmath import mp


def uniform(a, b):
    return 1 / (b - a)


def uniform_cdf(a, b, x):
    if x < a:
        return 0
    if x > b:
        return 1
    return (x - a) / (b - a)


def normal_cdf(m, s, x):
    return 1. / 2. * (1. + mp.erf((x - m) / (mp.sqrt(2) * s)))


def normal_pdf(m, s, x):
    var = mp.power(float(s), 2)
    den = mp.sqrt(2 * mp.pi * var)
    expo = -(mp.power(float(x) - float(m), 2) / (2 * var))
    return (1. / den) * mp.exp(expo)


def exp_cdf(l, x):
    return 1 - mp.exp(-l * x)


if __name__ == '__main__':
    pass
