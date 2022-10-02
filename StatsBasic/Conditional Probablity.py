#%%
from numpy import random
random.seed(0)

totals={20:0,30:0,40:0,50:0,60:0,70:0}
purchases ={20:0,30:0,40:0,50:0,60:0,70:0}
totalPurchases=0
for _ in range(100000):
    ageDecade=random.choice([20,30,40,50,60,70])
    purchaseProbability=float(ageDecade)/100.0
    totals[ageDecade] += 1
    if(random.random()<purchaseProbability):
        totalPurchases+=1
        purchases[ageDecade] +=1
# %%
print(totals)
# %%
print(purchases)
# %%
print(totalPurchases)
# %%
PEF=float(purchases[30])/float(totals[30])
print("P(purchase|30s)",PEF)
# %%
PF =float(totals[30]/100000)
print("P(30s)= ",PF)
# %%
PE=float(totalPurchases)/100000
print("P(Purchases):",PE)
# %%
print("P(E|F)=",float(purchases[30]/100000)/PF)

# %%
#EXERCISE
totals={20:0,30:0,40:0,50:0,60:0,70:0}
purchases={20:0,30:0,40:0,50:0,60:0,70:0}
i=0
for _ in range(600):
    ageDecade=random.choice([20,30,40,50,60,70])
    purchaseProbability=40.0/100.0
    totals[ageDecade] += 1
    if(random.random()<purchaseProbability):
        totalPurchases+=1
        purchases[ageDecade] +=1
# %%
print (totals)
# %%
print(purchases)

# %%
PEF=float(purchases[50])/float(totals[50])
print("P(purchase|30s)",PEF)
# %%
PF =float(totalPurchases/100000)
print("P(Purchases)= ",PF)
# %%
print("P(E|F)=",float(purchases[30]/100000)/PF)