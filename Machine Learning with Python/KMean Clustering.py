#%%
#Creating fake datas
from msilib import CreateRecord
import numpy as np
def createClusterData(N,k):
    np.random.seed(10)
    pointPerCluster=float(N)/k
    X=[]
    for i in range(k):
        incomeCentroid=np.random.uniform(20000,200000)
        ageCentroid=np.random.uniform(20,70)
        for j in range(int(pointPerCluster)):
            X.append([np.random.normal(incomeCentroid,10000),np.random.normal(ageCentroid,2)])
    X=np.array(X)
    return X
# %%
#using K-Means to rediscover the clusters
from sklearn.cluster import KMeans
import matplotlib.pyplot as  plt
from sklearn.preprocessing import scale

data=createClusterData(100,3)

model=KMeans(n_clusters=3)

#scaling data to normalize it. Imp for good results
model=model.fit(scale(data))

#looking at the clusters each data point was assigned to
print(model.labels_)

#vizualizing it
plt.figure(figsize=(8,6))
#c varying color for each value
plt.scatter(data[:,0],data[:,1],c=model.labels_.astype(np.float))
plt.show()
# %%
