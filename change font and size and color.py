import matplotlib.pyplot as plt
import numpy as np

x = np.array([80, 85, 95, 65, 84, 12, 35, 52])
y = np.array([250, 350, 541, 854, 325, 321, 120, 420])  # Added extra y value

font1 = {'family': 'serif', 'color': 'blue', 'size': 20}
font2 = {'family': 'serif', 'color': 'darkred', 'size': 15}  # Corrected color name

plt.title("Sports Watch Data", fontdict=font1)  # Added fontdict argument
plt.xlabel("Average Pulse", fontdict=font2)  # Added fontdict argument
plt.ylabel("Calories Burnage", fontdict=font2)  # Added fontdict argument
plt.plot(x, y)
plt.grid()
plt.show()