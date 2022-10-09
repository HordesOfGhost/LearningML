#%%
#randomly generating data
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(2)

pageSpeeds=np.random.normal(3,1,100)
purchaseAmount=np.random.normal(50,30,100)*pageSpeeds

plt.scatter(pageSpeeds,purchaseAmount)
plt.show()

# %%
#differentiating train and test data sets
trainX=pageSpeeds[:80]
testX=pageSpeeds[80:]

trainY=purchaseAmount[:80]
testY=purchaseAmount[80:]
# %%
# train data sets 
plt.scatter(trainX,trainY)
# %%
#test data sets
plt.scatter(testX,testY)

# %%
#fitting to a polynomial
x=np.array(trainX)
y=np.array(trainY)
#not fitted for poly 8
#p8=np.poly1d(np.polyfit(x,y,8))
#choosing better fit
p8=np.poly1d(np.polyfit(x,y,9))
# %%
#plotting against train data

xp=np.linspace(0,7,100)
axes=plt.axes()
axes.set_xlim([0,11])
axes.set_ylim([-100,700])
plt.scatter(x,y)
plt.plot(xp,p8(xp),c='r')
plt.show()

# %%
testx=np.array(testX)
testy=np.array(testY)

axes=plt.axes()
axes.set_xlim([0,11])
axes.set_ylim([-100,700])
plt.scatter(testx,testy)
plt.plot(xp,p8(xp),c='r')
plt.show()
# %%
#for test data
from sklearn.metrics import r2_score
r2=r2_score(testy,p8(testx))
print(r2)
# %%
#for train data
r2=r2_score(np.array(trainY),p8(np.array(trainX)))
print(r2)
# %%
