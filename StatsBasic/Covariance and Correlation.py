#%%
import numpy as np

def de_mean(x):
    xmean=np.mean(x)
    return [xi-xmean for xi in x]

def covariance(x,y):
    n=len(x)
    return np.dot((de_mean(x),de_mean(y))/(n-1))

pageSpeeds=np.random.normal(3,1,1000)
purchaseAmount=np.random.normal(50,10,1000)
