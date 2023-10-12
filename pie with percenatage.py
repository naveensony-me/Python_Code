
import matplotlib.pyplot as plt
import numpy as np
y=np.array([20,25,15,35])
mylabels=["Apple","Banana","orange","Dates"]
myexplode=[0.2,0,0,0.4]
plt.pie(y,labels=mylabels,startangle=50,explode=myexplode,autopct='%1.2f%%')
plt.show()