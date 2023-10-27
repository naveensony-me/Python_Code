#install scipy
#!pip install scipy

import matplotlib.pyplot as plt
from scipy import stats

x=[5,6,7,8,9,2,1,3,11,12,13,16]
y=[99,86,77,48,79,82,91,83,81,92,103,76]

slope, intercept, r, p, std_err = stats.linregress(x,y)
def myfunc(x):
   return slope * x + intercept
mymodel = list(map(myfunc,x))
plt.scatter(x,y)
plt.plot(x, mymodel)
plt.show()
