#%%
from this import d
from matplotlib import style
from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

x=np.arange(-3,5,0.001)
plt.plot(x,norm.pdf(x))
plt.show()

# %%
plt.plot(x,norm.pdf(x))
plt.plot([9,4],[4,3])
plt.plot(x,norm.pdf(x,4,.5))
plt.show()
# %%
#save plot
plt.plot(x,norm.pdf(x))
plt.plot([9,4],[4,3])
plt.plot(x,norm.pdf(x,4,.5))
plt.savefig('C:\\Users\\Ghost\\Desktop\\plot.png',format='png')
# %%
#controlled axis attributes
axes=plt.axes()
axes.set_xlim([-5,5])
axes.set_ylim([0,1])
axes.set_xticks([-5,-4,-3,-2,0,1,2,3,4,4.4,5])
axes.set_yticks([0,0.2,0.4,0.6,0.8,1])
plt.plot(x,norm.pdf(x))
plt.plot(x,norm.pdf(x,0,.5))
plt.show()

# %%
#adding grid
axes=plt.axes()
axes.set_xlim([-5,5])
axes.set_ylim([0,1])
axes.set_xticks([-5,-4,-3,-2,0,1,2,3,4,4.4,5])
axes.set_yticks([0,0.2,0.4,0.6,0.8,1])
#here
axes.grid()
plt.plot(x,norm.pdf(x))
plt.plot(x,norm.pdf(x,0,.5))
plt.show()
# %%
#change line  types and colors
axes=plt.axes()
axes.set_xlim([-5,5])
axes.set_ylim([0,1])
axes.set_xticks([-5,-4,-3,-2,0,1,2,3,4,4.4,5])
axes.set_yticks([0,0.2,0.4,0.6,0.8,1])
axes.grid()
plt.plot(x,norm.pdf(x),'b--')
plt.plot(x,norm.pdf(x,0,.5),'g:')
plt.show()

# %%
#labelling axes and adding legend
axes=plt.axes()
axes.grid()
x=np.arange(1,100,0.2)
plt.ylabel('Seconds')
plt.xlabel('Decay')
plt.plot(x,norm.pdf(x,25,9))
plt.plot(x,norm.pdf(x,50,20))
plt.legend(['Uranium','Radium'],loc=4)
plt.show()
# %%
#XKCD style
plt.xkcd()

fig=plt.figure()
ax=fig.add_subplot(1,1,1)
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.set_ylim([-30,10])

data=np.ones(100)
data[70:] -=np.arange(30)

plt.annotate(
    "THE DAY I REALIZED  \n I CAN CODE PYTHON",
    xy=(70,1),arrowprops=dict(arrowstyle='->'),xytext=(15,-10)
    )
plt.plot(data)

plt.xlabel('days')
plt.ylabel('My insecurities')


# %%
#PIE chart
plt.rcdefaults()
value=[30,15,15,5,3,2,20]
explode=[0.05,0,0,0,0,0,.15]
labels=['Python','JS','R','C++','Java','C#','WordPress']
plt.pie(value,labels=labels,explode=explode)
plt.title('Major Languages')
plt.show()
# %%
#Bar Chart
values=[12,23,55,42,23,4]
colors=['r','c','m','y','k','b']
plt.bar(range(2,8),values,color=colors)
plt.show()
# %%
#scatter
x=np.random.randn(5)
y=np.random.randn(5)
plt.scatter(x,y)
plt.show()

# %%
#histogram
income=np.random.normal(2700,15000,10000)
plt.hist(income,50)
plt.show()

# %%
#Whisker Plot
uniformSkewed=np.random.rand(1000)*100-40
high_outliers=np.random.rand(10)*50+100
low_outliers=np.random.rand(10)*-50-100
data=np.concatenate((uniformSkewed,high_outliers,low_outliers))
plt.boxplot(data)
plt.show()
# %%
x=np.random.normal(19,4,50)
y=np.random.normal(7,2.5,50)
plt.xlabel('Age By Years')
plt.ylabel('Average of time spent in TV(hours)')
plt.scatter(x,y)
plt.show()
# %%
