from scipy import stats
import matplotlib.pyplot as plt

from a.a1_loi_discretes import poisson_log

rate = 2
k = range(0, 10)
# lib python (to compare with my results)
y = stats.poisson.pmf(k, rate)
print(y)

poisson_result = []
for i in k:
    poisson_result.append(round(poisson_log(rate, i), 9))
print(poisson_result)

plt.plot(k, poisson_result, 'o-')
plt.title("poisson %i" % rate, fontsize=15)
plt.xlabel("accidents")
plt.ylabel("probability")
plt.show()

"""
result of the lib python:
[  1.35335283e-01   2.70670566e-01   2.70670566e-01   1.80447044e-01
   9.02235222e-02   3.60894089e-02   1.20298030e-02   3.43708656e-03
   8.59271640e-04   1.90949253e-04]
"""
