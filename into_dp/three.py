import numpy as np
import matplotlib.pylab as plt

#阶跃函数
def step_function(x):
    return (x>0).astype(int)

#sigmoid函数
def sigmoid(x):
    return 1 / (1+np.exp(-x))

#ReLu函数
def relu(x):
    return np.maximum(0,x)

x = np.arange(-5.0,5.0,0.1)
y = step_function(x)
plt.plot(x, y)
plt.ylim(-0.1,1.1) #指定y轴范围
plt.show()

y = sigmoid(x)
plt.plot(x,y)
plt.ylim(-0.1,1.1) #指定y轴范围
plt.show()
