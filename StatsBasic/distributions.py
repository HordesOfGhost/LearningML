#%%
import numpy as np
import matplotlib.pyplot as plt
#uniform
values=np.random.uniform(-10,10,1000)
plt.hist(values,50)
plt.show()
# %%
from scipy.stats import norm
#normal
x=np.arange(-3,3,0.001)
plt.plot(x,norm.pdf(x))
# %%
import numpy as np
import matplotlib.pyplot as plt
#gaussian
mu=5
sigma=2
values=np.random.normal(mu,sigma,1000)
plt.hist(values,50)
plt.show()
# %%
#expo
from scipy.stats import expon
x=np.arange(0,10,.10)
plt.plot(x,expon.pdf(x))
# %%
from scipy.stats import binom
#pmf bionamial
n,p =10,0.1
x=np.arange(-5,5,0.001)
plt.plot(x,binom.pmf(x,n,p))

# %%
from scipy.stats import poisson
import matplotlib.pyplot as plt
#poisson
mu=700
x=np.arange(500,1000,.5)
plt.plot(x,poisson.pmf(x,mu))

# %%
