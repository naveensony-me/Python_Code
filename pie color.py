import matplotlib.pyplot as plt
import numpy as np
y=np.array([20,25,15,35])
mylabels=["Apple","Banana","orange","Dates"]
mycolors=["green","orange","red","b"]
plt.pie(y,labels=mylabels,shadow=True,colors=mycolors)
plt.show()
