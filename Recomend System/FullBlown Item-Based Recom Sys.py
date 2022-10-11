#%%
import pandas as pd
r_cols=['user_id','movie_id','rating']
ratings=pd.read_csv("C:\\Users\\Ghost\\Desktop\\LearningML\\materials\\ml-100k\\u_data.data",sep='\t',names=r_cols,usecols=range(3),encoding='latin-1')

m_cols=['movie_id','title']
movies=pd.read_csv("C:\\Users\\Ghost\\Desktop\\LearningML\\materials\\ml-100k\\u_item.item",sep='|',names=m_cols,usecols=range(2),encoding='latin-1')

ratings=pd.merge(movies,ratings)

print(ratings.head())

# %%
#making matrices of user as rows movies as columns
userRatings=ratings.pivot_table(index=['user_id'],columns=['title'],values='rating')
print(userRatings.head())
# %%
#now corr() will compute a correlation score for every column pair in matrix
corrMatrix=userRatings.corr()
print(corrMatrix.head())
 
# %%
#now we have to avoid spuirous result
corrMatrix=userRatings.corr(method='pearson',min_periods=300)#can use other coeffeicints method and min values
print(corrMatrix.head())
# %%
#drop NAN
myRatings=userRatings.loc[0].dropna()#loc[0] user id 0
print(myRatings)
# %%
#now finding recomendations for fictious user loc[0]
simCandidates=pd.Series()
for i in range(0,len(myRatings.index)):
    print("Adding sims for "+ myRatings.index[i] + "...")
    #Retrieve similar movies to this one that I rated
    sims=corrMatrix[myRatings.index[i]].dropna()
    #Now scale its similarity by how well I rated this movie
    sims=sims.map(lambda x: x*myRatings[i])
    #Add the score to the list of similarity candidates
    simCandidates=simCandidates.append(sims)
#Glance at our results so far:
print ("sorting...")
simCandidates.sort_values(inplace=True,ascending=False)
print (simCandidates.head(20))
# %%
#apparantly duplicates of movies came to be so summing up
simCandidates=simCandidates.groupby(simCandidates.index).sum()

# %%
simCandidates.sort_values(inplace=True,ascending=False)
print(simCandidates.head(10))

# %%

#filter movies I have watched
filteredSims=simCandidates.drop(myRatings.index)
#for ratings on 5
#for i in range(0,len(filteredSims.index)):
#    filteredSims[i]=filteredSims[i]/10*5
print(filteredSims.head(20))
# %%
