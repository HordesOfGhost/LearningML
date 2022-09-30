listOfNumber=[1,2,3,4,5]

for number in listOfNumber:
    print (number),
    if (number%2==0):
        print ("is even")
    else:
        print ("is odd")
        
print ("done")

import numpy as np

a=np.random.normal(23.0,5.0,19)

print(a)

#lists
x=[1,2,3,4,3,4]
print (len(x))
print(x[2:])
x.extend([34,34,22,3400])
print(x)
y=[32,44,22,33,22,33,33,33]
lists=[x,y]
print(lists)
x.sort()
lists.sort()
print (x)
print (lists)

#Dictionaries
t=(1,23,4,4,4)
(age,income)="32,1200".split(',')
print (age)
print(income)

#Dictionaries
captains={}
captains["Enterprise"]="Kirk"
captains["Enterprise D"]="dd"

print (captains.get["Ent"])