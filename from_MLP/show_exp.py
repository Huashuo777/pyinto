import tools
import numpy as np
import matplotlib.pyplot as plt

a = np.array([0,1])
print(tools.step_function(a))

a = np.arange(-5,5,0.1)
y1 = tools.step_function(a)
y2 = tools.sigmod(a)
y3 = tools.relu(a)

plt.plot(a, y1, label = "step",linestyle = ":")
plt.plot(a, y2, label = "sigmoid", linestyle = "--")
plt.plot(a, y3, label = "relu", linestyle = "-")
plt.xlabel("x")
plt.ylabel("y")
plt.title("functions")
plt.ylim(-0.1,1.1)
plt.legend()

plt.show()

