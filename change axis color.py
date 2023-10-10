import matplotlib.pyplot as plt
import numpy as np
x=np.array([5,6,7,8,9,2,1,3,11,12,13,16])
y=np.array([99,86,77,48,79,82,91,83,81,92,103,76])
colors=np.array(["red","green","orange","purple","yellow","pink","black","gray","cyan","magenta","blue","brown"])
plt.scatter(x,y,c=colors)
plt.show()