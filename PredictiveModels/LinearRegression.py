#%%
# Creating Datas
from code import interact
import numpy as np
from scipy import stats
pageSpeeds=np.random.normal(3,1,1000)
purchaseAmount = (pageSpeeds+np.random.normal(0,0.5,1000))+3
#%%
#slopes intercept,r_value,p_value,std_err
slope,intercept,r_value,p_value,std_error=stats.linregress((pageSpeeds,purchaseAmount))
#%%
#R value
print(r_value**2)

# %%
#plotting
import matplotlib.pyplot as plt

def predict(x):
    return slope *x +intercept
fitline=predict(pageSpeeds)

plt.scatter(pageSpeeds,purchaseAmount)
plt.plot(pageSpeeds,fitline,c='g')
plt.xlabel('PageSpeeds')
plt.ylabel('PurchaseAmount')
plt.show()

# %%
#Exercise

age=np.random.normal(18,5,1000)
deaths=np.random.normal(100,77,1000)

##plt.scatter(deaths,age)
slope,intercept,r_value,p_value,std_error=stats.linregress(age,deaths)

print(r_value**2)

def line(x):
    return slope*x+intercept

print(slope)
print(intercept)
#%%
axes=plt.axes()
axes.set_yticks([100.0049])
axes.set_xticks([18])
axes.grid()
plt.scatter(deaths,age)
plt.plot(age,line(age),c='b')
plt.show()
# %%
