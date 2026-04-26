import sys, os
import numpy as np
from tools import sigmod 
from tools import identity_function
from tools import init_network
from tools import forward
from tools import softmax
X = np.array([[1., 0.5]])
network = init_network()
Y = forward(network, X)
print(Y)

print(softmax(np.array([0.3,2.9,4.0])))
print(sys.platform)