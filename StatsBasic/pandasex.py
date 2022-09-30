


#%matplotlib inline
import matplotlib.pylab as plt
import numpy as np
import pandas as pd
from IPython.display import display

df=pd.read_csv("DataScience-Python3\PastHires.csv")
print(df.shape)
print(df.columns)
degree_counts=df['Level of Education'].value_counts()
print(df[["Previous employers","Hired"]][5:11])
newd=df[["Previous employers","Hired"]][5:11]
d=np.histogram(df['Previous employers'])
fig, ax = plt.subplots(figsize =(10, 7))
plt.figure()
degree_counts.plot(kind='bar')
ax.hist(d)

plt.show()
dfa=pd.DataFrame(df)
print(display(dfa))