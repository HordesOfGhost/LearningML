#%%
import numpy as np
import matplotlib.pyplot as plt
income=np.random.normal(100,30,10000)

plt.hist(income,50)
plt.show()
# %%
income=np.append(income,[22])
print (income.std())
# %%
print (income.var())
# %%
