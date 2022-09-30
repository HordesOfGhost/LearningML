

#%%
import numpy as np
income=np.random.normal(27000,15000,10000)
print(np.mean(income))
print(np.median(income))
# %%
import matplotlib.pyplot as plt
plt.hist(income,50)
plt.show()

# %%

income=np.append(income,[1000000000000])
print(np.mean(income))
print(np.median(income))
# %%
ages=np.random.randint(19,high=33,size=333)
print(ages)
# %%
from scipy import stats
stats.mode(ages)

# %%
sales =np.random.normal(100,20,10000)
plt.hist(sales,100)
plt.show()
# %%
sales=np.append(income,[23])
print(np.mean(sales))
print(np.median(sales))
# %%
stats.mode(sales)
# %%
