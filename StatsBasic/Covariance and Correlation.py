#%%
#random data
import numpy as np
import matplotlib.pyplot as plt

def de_mean(x):
    xmean=np.mean(x)
    return [xi-xmean for xi in x]

def covariance(x,y):
    n=len(x)
    return np.dot(de_mean(x),de_mean(y))/(n-1)

def correlation(x,y):
    stdofx=x.std()
    stdofy=y.std()
    return covariance(x,y)/stdofx/stdofy

pageSpeeds=np.random.normal(3,1,1000)
purchaseAmount=np.random.normal(50,10,1000)

plt.scatter(pageSpeeds,purchaseAmount)
print(covariance(pageSpeeds,purchaseAmount))
print (correlation(pageSpeeds,purchaseAmount))
print(np.corrcoef(pageSpeeds,purchaseAmount))


# %%
# negative covariance
purchaseAmount=np.random.normal(50,10,1000)/pageSpeeds
plt.scatter(pageSpeeds,purchaseAmount)
print(covariance(pageSpeeds,purchaseAmount))
print (correlation(pageSpeeds,purchaseAmount))
print(np.corrcoef(pageSpeeds,purchaseAmount))

# %%
#positive maybe
purchaseAmount=np.random.normal(50,10,1000)*pageSpeeds
plt.scatter(pageSpeeds,purchaseAmount)
print(covariance(pageSpeeds,purchaseAmount))
print (correlation(pageSpeeds,purchaseAmount))
print(np.corrcoef(pageSpeeds,purchaseAmount)[0][1])
# %%

print (correlation(pageSpeeds,purchaseAmount))

# %%
##   NUMPY WAY

print(np.corrcoef(pageSpeeds,purchaseAmount))
# %%
# Forcing Correlation
purchaseAmount=100-pageSpeeds*3
plt.scatter(pageSpeeds,purchaseAmount)
print(correlation(pageSpeeds,purchaseAmount))
# %%
purchaseAmount=pageSpeeds*3+100
plt.scatter(pageSpeeds,purchaseAmount)
print(correlation(pageSpeeds,purchaseAmount))
# %%
purchaseAmount=pageSpeeds*9
print(np.cov(pageSpeeds,purchaseAmount))
# %%
