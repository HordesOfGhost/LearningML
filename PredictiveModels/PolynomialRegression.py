#%%
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import recall_score
np.random.seed(2)
pageSpeeds=np.random.normal(3,1,1000)
purchaseAmount=np.random.normal(50,10,1000)*pageSpeeds**4  
plt.scatter(pageSpeeds,purchaseAmount)
# %%
# ARRAYED
x=np.array(pageSpeeds)
y=np.array(purchaseAmount)


p3=np.poly1d(np.polyfit(x,y,4))
print (p3)
#p = np.poly1d([1, 2, 3])
#print(np.poly1d(p))
#   2
#1 x + 2 x + 3
# %%
xp=np.linspace(0,9,1000)
axes=plt.axes()
axes.set_yticks([206458.72])
axes.set_xticks([9])
axes.grid()
plt.scatter(x,y)
print(len(xp))
plt.plot(xp,p3(xp),c='r')
plt.show()

# %%
# R-Squared
from sklearn.metrics import r2_score
r2=r2_score(y,p3(x))
print (r2)
# %%
## linspace

y=np.random.normal(10,2,10)
x=np.linspace(0,10,10)
plt.plot(x,y,c='b')
plt.show()
# %%
#linespace continue
y=np.poly1d([2,0,0])
x=np.linspace(0,10,10)
plt.plot(x,y(x))
plt.show()

# %%
