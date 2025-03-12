import scipy
from scipy.stats import norm

cau = scipy.stats.cauchy()
distribution = np.linspace(0, np.minimum(cau.dist.b, 5))

plot = plt.plot(distribution, cau.pdf(distribution))

cau_mean = lambda n: [cau.rvs(size=n).mean() for i in range(1000)]

x_norm = lambda n: np.linspace(norm.ppf(0.01,loc=mean,scale=var/np.sqrt(n)),
                               norm.ppf(0.99,loc=mean,scale=var/np.sqrt(n)), 100)
data = [(cau_mean(n), x_norm(n),
         norm.pdf(x_norm(n), loc=mean,scale=var/np.sqrt(n)), n) for n in (5,10,50,100,200,500)]

fig, axs = plt.subplots(3,2, figsize=(15,10))
axs = axs.ravel()

for idx,ax in enumerate(axs):
    ax.hist(data[idx][0], bins=200, density=True, color='g')
    ax.set_title('N = '+ str(data[idx][3]))
    label = 'sigma: ' + str(round(var/np.sqrt(data[idx][3]),3)) + '\nmu: ' + str(round(mean,3))
    ax.plot(data[idx][1], data[idx][2],'r-', lw=5, label=label)
    ax.legend(loc='best')

k = 7
lamb = 2
erlang_dist = scipy.stats.erlang(k, scale=lamb)
distribution = np.linspace(0, np.minimum(erlang_dist.dist.b, 5))

plot = plt.plot(distribution, erlang_dist.pdf(distribution))

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

