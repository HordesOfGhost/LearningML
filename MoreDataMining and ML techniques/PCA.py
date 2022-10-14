#%%
#Iris data set comes with scikit learn. Its just small collection of data that has 4-D data for
# three diff types of Iris Flowers. Length and Width of both petal and sepals of many individual flowers from each species.
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
import pylab as pl
from itertools import cycle

iris=load_iris()

numSamples,numFeatures=iris.data.shape
print(numSamples)
print(numFeatures)
print(list(iris.target_names))
# %%
# So this tells us our data set has 150 samples.
# It has 4 dimensions called featuresand 3 distinct Iris species that each flower is classified into
# We can easily visualize in 2 or even 3 dimensinos of data easily but visualizing 4D data is something brains cant do.
# So lets boil down to 2 dimensions.
x=iris.data

pca=PCA(n_components=2,whiten=True).fit(x)
x_pca=pca.transform(x)

# %%
#what we have done is distilled our 4D data set down to 2D by projectiong down to two orthogonal 4D vectors that make up basis of our new 2D projection.

print(x)
print("****************")
print(pca.components_)

# %%
#Lets see how much information we managed to presrve
print(pca.explained_variance_ratio_)
print(sum(pca.explained_variance_ratio_))
# %%
# Although we have thrown away two of our four dimensions,PCA has chosen the remaining two dimensions well enough that
# We'have captured 92% variance in single dimension alone. The second dimension gives us additional 5%, all together we only lost less than 3 % of variance.
# Now Plot  2-D representation of our data

colors=cycle('rgb')
target_ids=range(len(iris.target_names))
pl.figure()
for i,c,label in zip(target_ids,colors,iris.target_names):
    pl.scatter(x_pca[iris.target==i,0],x_pca[iris.target==i,1],
               c=c,label=label)
pl.legend()
pl.show()    
# %%
