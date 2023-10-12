import matplotlib.pyplot as plt
import numpy as np
y=np.array([20,25,15,35])
mylabels=["Apple","Banana","orange","Dates"]
myexplode=[0.2,0,0,0]
mycolors=["black","orange","red","b"]
plt.pie(y,labels=mylabels,explode=myexplode,shadow=True,colors=mycolors)
plt.show()