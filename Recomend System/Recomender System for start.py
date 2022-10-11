#%%
#Finding Similar Movies

import pandas as pd

r_cols=['user_id','movie_id','rating']
ratings=pd.read_csv("C:\\Users\\Ghost\\Desktop\\LearningML\\materials\\ml-100k\\u_data.data", sep='\t',names=r_cols,usecols=range(3),encoding='latin-1')
print(ratings.head())
m_cols=['movie_id','title']
movies=pd.read_csv("C:\\Users\\Ghost\\Desktop\\LearningML\\materials\\ml-100k\\u_item.item", sep='|',names=m_cols,usecols=range(2),encoding='latin-1')
print(movies.head())
ratings=pd.merge(movies,ratings)
# %%
print(ratings.head())
# %%
#making a user/movie Matrix
movieRatings=ratings.pivot_table(index=['user_id'],columns=['title'],values='rating')
print(movieRatings.head())

# %%
#extract a series of users who watched StarWars
starWarsRatings=movieRatings['Star Wars (1977)']

print(starWarsRatings.dropna())
# %%
#correlate other movies to star wars
similarMovies=movieRatings.corrwith(starWarsRatings)
similarMovies=similarMovies.dropna()
df=pd.DataFrame(similarMovies)
print(df.head())

# %%
#sort
print(similarMovies.sort_values(ascending=False))

# %%
#getting rid of movies that were watched by few people that are producing spurious results
import numpy as np
movieStats=ratings.groupby('title').agg({'rating':[np.size,np.mean]})
print(movieStats.head())

# %%
#in up we found movies with >100 is more heard
popularMovies=movieStats['rating']['size']>=300 #initially it was 100
movieStats[popularMovies].sort_values([('rating','mean')],ascending=False)[:15]
                         
# %%
#join similar movies with movies that have >100 ratings
df=movieStats[popularMovies].join(pd.DataFrame(similarMovies,columns=['similarity']))
# %%
print(df.head())
# %%
df.sort_values(['similarity'],ascending=False)[:20]
# %%
