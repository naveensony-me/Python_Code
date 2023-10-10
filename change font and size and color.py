import matplotlib.pyplot as plt
import numpy as np
x=np.array([80,85,95,65,84,12,35,52])
y=np.array([250,350,541,854,325,321])
font1={'family':'serif','color':'blue','size':20}
font2={'family':'serif','color':'darked','size':15}

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calories Burnage")
plt.plot(x,y)
plt.grid()
plt.show()