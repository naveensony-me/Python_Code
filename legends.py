import matplotlib.pyplot as plt
import numpy as np
y=np.array([20,25,15,35])
mylabels=["Apple","Banana","orange","Dates"]
plt.pie(y,labels=mylabels)
plt.legend()
plt.show()
