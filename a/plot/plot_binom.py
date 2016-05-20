import matplotlib.pyplot as plt

from a.a1_loi_discretes import binomial

n = 10
p = 0.3
k = range(0, 20)

print(n, p, k)

# binomial_result = stats.binom.pmf(k, n, p)

binomial_result = []
for i in k:
    binomial_result.append(round(binomial(n, p, i), 8))
print(binomial_result)


plt.plot(k, binomial_result, 'o-')
plt.title("binomial %i %.2f" %(n, p), fontsize=15)
plt.xlabel("success")
plt.ylabel("probability")
plt.show()
