import numpy as np
A = np.array([[[1,2,0],[3,4,0]],[[5,6,0],[7,8,0]]])
print(A)
print(np.ndim(A)) #获得多维数组的维数np.ndim(XXX)
print(A.shape)
#A.shape 返回 (4,)，所以 A.shape[0] 访问的是第一个（也是唯一一个）维度的长度，即 4
#(4,)表示一维数组，长度为4
print(A.shape[2])#注意写法 返回shape的第3个参数