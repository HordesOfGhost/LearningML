#%%
import pandas as pd
df=pd.read_excel('http://cdn.sundog-soft.com/Udemy/DataScience/cars.xls')
print(df.head())
# %%
import statsmodels.api as sm
from sklearn.preprocessing import StandardScaler
scale=StandardScaler()

x=df[['Mileage','Cylinder','Doors']]
y=df['Price']
x[['Mileage','Cylinder','Doors']]=scale.fit_transform(x[['Mileage','Cylinder','Doors']].values)
#print(x)
est=sm.OLS(y,x).fit()
print("---Summarry---")
print(est.summary())
# %%
y.groupby(df.Doors).mean()
y.groupby(df.Cylinder).mean()
y.groupby(df.Mileage).mean()
 
