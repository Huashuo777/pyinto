import numpy as np

def AND(x1,x2):
    x = np.array([x1,x2])
    w = np.array([0.5,0.5])
    theta = -0.7
    tmp = np.sum(x*w) + theta
    if tmp <= 0:
        return 0
    else:
        return 1

def NAND(x1,x2):
    x = np.array([x1,x2])
    w = np.array([-0.5, -0.5])
    theta = 0.7
    tmp = np.sum(w * x) +theta
    if tmp <=0 :
        return 0
    else:
        return 1

def OR(x1,x2):
    x = np.array([x1,x2])
    w = np.array([0.5,0.5])
    theta = -0.2
    tmp = np.sum(x*w) + theta
    if tmp <= 0:
        return 0
    else:
        return 1
    
def XOR(x1, x2):
    tmp1 = OR(x1,x2)
    tmp2 = NAND(x1,x2)
    tmp3 = AND(tmp1,tmp2)
    if tmp3 <= 0:
        return 0
    else:
        return 1
    
def step_function(x):
    y = x > 0
    return y.astype(int)

def sigmod(x):
    return 1/(1+np.exp(-x))

def relu(x):
    return np.maximum(0,x)

def identity_function(x):
    return x

def softmax(x):
    x = x - np.max(x)
    exp_x = np.exp(x)
    sum_exp_x = np.sum(exp_x)
    y = exp_x / sum_exp_x
    return y

## page 87/314
def init_network():
    network = {}
    # Wij 第i行第j列是第i个元素对第j个元素的权重
    network['W1'] = np.array([[0.1,0.3,0.5],[0.2,0.4,0.6]])
    network['b1'] = np.array([[0.1,0.2,0.3]])    
    network['W2'] = np.array([[0.1,0.4],[0.2,0.5],[0.3,0.6]])
    network['b2'] = np.array([[0.1,0.2]])
    network['W3'] = np.array([[0.1,0.3],[0.2,0.4]])
    network['b3'] = np.array([[0.1,0.2]])
    return network

def forward(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    A1 = np.dot(x,W1) + b1
    Z1 = sigmod(A1)
    A2 = np.dot(Z1,W2) + b2
    Z2 = sigmod(A2)
    A3 = np.dot(Z2,W3) + b3
    Y = identity_function(A3)
    
    return Y
##手写初始化神经网络