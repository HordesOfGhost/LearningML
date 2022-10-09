#%%
#importing file
import numpy as np
import pandas as pd
from sklearn import tree

df=pd.read_csv("C:/Users/Ghost/Desktop/LearningML/materials/PastHires(modified).csv",header=0)


# %%
print(df.head())
# %%
#preparing data
#sklearn works on all number so
d={'Y':1,'N':0}
df['Hired']=df['Hired'].map(d)
df['Employed?']=df['Employed?'].map(d)
df['Top-tier school']=df['Top-tier school'].map(d)
df['Interned']=df['Interned'].map(d)
d={'BS':0,'MS':1,'PhD':2} 
df['Level of Education']=df['Level of Education'].map(d)
print(df.head())
# %%
#separating features from target column that we are trying to build a decision tree for
features=list(df.columns[:6])
print (features)

# %%
#constructing decision tree
y=df["Hired"]
x=df[features]
clf=tree.DecisionTreeClassifier()
clf=clf.fit(x,y)

#%%
from sklearn import tree
from six import StringIO
dot_data=StringIO()

tree.export_graphviz(clf,out_file=dot_data,
                     feature_names=features)
print(tree.plot_tree(clf))
#[    x[0]                x[1]            x[2]                  x[3]                x[4]              x[5]]
#['Years Experience', 'Employed?', 'Previous employers', 'Level of Education', 'Top-tier school', 'Interned']

# %%
