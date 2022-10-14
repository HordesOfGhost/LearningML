#%%
#loading up every rating in data set to Pandas DataFrame
import pandas as pd
from sklearn import neighbors

r_cols=['user_id','movie_id','rating']
ratings=pd.read_csv("C:\\Users\\Ghost\\Desktop\\LearningML\\materials\\ml-100k\\u_data.data",sep='\t',names=r_cols,usecols=range(3),encoding="latin-1")

print(ratings.head())

# %%
#now we will group everything by MovieID and compute the total number of ratings(each movie's popularity) and the avg of every movie
import numpy as np
movieProperties=ratings.groupby('movie_id').agg({'rating':[np.size,np.mean]})
print(movieProperties.head())
# %%
#normalize the number of ratings for a movie 0 being noone rating it and 1 being mostly rated
movieNumRatings=pd.DataFrame(movieProperties['rating']['size'])
movieNormalizedNumRatings=movieNumRatings.apply(lambda x:((x-np.min(x))/(np.max(x)-np.min(x))))
print(movieNormalizedNumRatings.head())

# %%
#now lets gather genre information
movieDict={}

with open(r"C:\\Users\\Ghost\\Desktop\\LearningML\\materials\\ml-100k\\u_item.item") as f:
    temp =''
    for line in f:
        fields=line.rstrip('\n').split('|')
        movieID=int(fields[0])
        name=fields[1]
        genres=fields[5:25]
        genres = [eval(i) for i in genres]
        #genres=map(int,genres)
        
        movieDict[movieID]=(name,genres,movieNormalizedNumRatings.loc[movieID].get('size'),movieProperties.loc[movieID].rating)
        

# %%
movieDict
print(movieDict[2])
print(movieDict[1])
# %%
#lets define a function that computes distance between two movies based on how similar genres are
#greater the distance the less similar they are
from scipy import spatial

def ComputeDistance(a,b):
    genresA=a[1]
    genresB=b[1]
    genreDistance=spatial.distance.cosine(genresA,genresB)
    popularityA=a[2]
    popularityB=b[2]
    popularityDistance=abs(popularityA-popularityB)
    return genreDistance+popularityDistance
print(ComputeDistance(movieDict[2],movieDict[4]))

# %%
import operator

def getNeighbors(movieID,K):
    distances=[]
    for movie in movieDict:
        if(movie!=movieID):
            dist=ComputeDistance(movieDict[movieID],movieDict[movie])
            distances.append((movie,dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors=[]
    for x in range(K):
        neighbors.append(distances[x][0])
    return neighbors
K=10
avgRating=0
print(movieDict[10])
neighbors=getNeighbors(10,K)
for neighbor in neighbors:
    avgRating += movieDict[neighbor][3]
    print (movieDict[neighbor][0]+" "+str(movieDict[neighbor][3])) 
avgRating /= float(K)
# %%
print(avgRating)
print(movieDict[10])

# %%
