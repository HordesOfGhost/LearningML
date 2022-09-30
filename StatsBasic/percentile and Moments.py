#%%
import numpy as np
import matplotlib.pyplot as plt

vals=np.random.normal(85,8889,50)

plt.hist(vals,50)
plt.show()
# %%
print(np.percentile(vals,50))
# %%
print(np.percentile(vals,90))
# %%
print(np.percentile(vals,20))
# %%
#moments
#first moment
print(np.mean(vals))
#second moment
print(np.var(vals))
# %%
import scipy.stats as sp
#skew
print(sp.skew(vals))
#kurtosis
print(sp.kurtosis(vals))
# %%
