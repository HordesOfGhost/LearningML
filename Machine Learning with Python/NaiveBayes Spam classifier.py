#%%
#importing datas
import os
import io
import numpy as np
from pandas import DataFrame
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

def readFile(path):
    for root,dirname,filenames in os.walk(path):
        for filename in filenames:
            path=os.path.join(root,filename)
            
            inBody=False
            lines=[]
            f=io.open(path,'r',encoding='latin1')
            for line in f:
                if inBody:
                    lines.append(line)
                elif line== '\n':
                    inBody=True
            f.close()
            message='\n'.join(lines)
            yield path,message

def dataFrameFromDirectory(path,classification):
    rows=[]
    index=[]
    for filename,message in readFile(path):
        rows.append({'message':message,'class':classification})
        index.append(filename)
        
    return DataFrame(rows,index=index)
data=DataFrame({'message':[],'class':[]})

data=data.append(dataFrameFromDirectory('C:\\Users\\Ghost\\Desktop\\LearningML\\materials\\emails\\spam','spam'))
data=data.append(dataFrameFromDirectory('C:\\Users\\Ghost\\Desktop\\LearningML\\materials\\emails\\ham','ham'))
# %%
print(data)
# %%
# using CountVectorizer to split msg into its list of words
vectorizer=CountVectorizer()
counts=vectorizer.fit_transform(data['message'].values)

classifier=MultinomialNB()
targets=data['class'].values

classifier.fit(counts,targets)
print (counts)
# %%
examples=['Hello and thank you for staying with us!','Free sales','Call Me','Hi Bob,how about a game of golf tommorrow?']
example_counts=vectorizer.transform(examples)
predictions=classifier.predict(example_counts)
print(predictions)

# %%
