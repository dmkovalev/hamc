import scipy
from scipy.stats import cauchy
import numpy as np
import matplotlib.pyplot as plt

cauchy_dist = scipy.stats.cauchy()
distribution = np.linspace(0, np.minimum(cauchy_dist.dist.b, 5))
plot = plt.plot(distribution, cauchy_dist.pdf(distribution))
plt.title('Распределение Коши')

def cau_mean(n, num_samples=1000):
    return [cauchy.rvs(size=n).mean() for _ in range(num_samples)]

n_values = [5, 10, 50, 100, 200, 500]

data = [cau_mean(n) for n in n_values]

fig, axs = plt.subplots(3, 2, figsize=(12, 9))
axs = axs.ravel()

for idx, ax in enumerate(axs):
    n = n_values[idx]
    ax.hist(data[idx], bins=30, density=True, color='g', alpha=0.7, label=f'N = {n}')
    ax.set_title(f'N = {n}')
    ax.set_xlabel('Sample Mean')
    ax.set_ylabel('Density')
    ax.legend(loc='best')

plt.tight_layout()
plt.show()

#распределение Эрланга
k = 7
lamb = 2
erlang_dist = scipy.stats.erlang(k, scale=lamb)
distribution = np.linspace(0, np.minimum(erlang_dist.dist.b, 5))
plot = plt.plot(distribution, erlang_dist.pdf(distribution))
plt.title('Распределение Эрланга')

mean = erlang_dist.mean()
var =erlang_dist.var()

erlang_mean = lambda n: [erlang_dist.rvs(size=n).mean() for i in range(1000)]

x_norm = lambda n: np.linspace(norm.ppf(0.01,loc=mean,scale=var/np.sqrt(n)),
                               norm.ppf(0.99,loc=mean,scale=var/np.sqrt(n)), 100)
data = [(erlang_mean(n), x_norm(n),
         norm.pdf(x_norm(n), loc=mean,scale=var/np.sqrt(n)), n) for n in (5,10,50,100,200,500)]

fig, axs = plt.subplots(3,2, figsize=(15,10))
axs = axs.ravel()

for idx,ax in enumerate(axs):
    ax.hist(data[idx][0], bins=20, density=True, color='g')
    ax.set_title('N = '+ str(data[idx][3]))
    label = 'sigma: ' + str(round(var/np.sqrt(data[idx][3]),3)) + '\nmu: ' + str(round(mean,3))
    ax.plot(data[idx][1], data[idx][2],'r-', lw=5, label=label)
    ax.legend(loc='best')

