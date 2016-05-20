from a import a1_loi_discretes


def _poisson(l, e, n, i):
    if not 0 <= l / n <= 1:
        return False

    b = a1_loi_discretes.binomial_cdf(n, l / n, i)
    p = a1_loi_discretes.poisson_cdf(l, i)
    result = abs(b - p)

    if result < e:
        return True
    else:
        return False


def validator(l, e, n):
    validation = True
    for i in range(0, n + 1):
        if not _poisson(l, e, n, i):
            validation = False
    return validation


def poisson(l, e):
    for n in range(1, 2000):
        if validator(l, e, n):
            return n
    return -1


if __name__ == '__main__':
    f = open('result.log', 'w+')
    values_l = [0.5, 1., 5., 15.]
    values_e = [0.1, 0.01, 0.001]
    for e in values_e:
        for l in values_l:
            f.write("n = {0:3}  l = {1:4}  e = {2}".format(poisson(l, e), l, e))
            f.write("\n")
