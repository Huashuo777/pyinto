import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread
'''numpy的array方法生成numpy数组，广播，变一维，条件筛选方法（标记法）
x=np.array([[1,2,3.0],[4,5,6]])
print(x)
print(x.shape)
print(x.dtype)
print(x[0])
print(x.flatten())
print(x)
print(x[x>2])
'''
#从图像文件（如 JPEG、PNG、BMP 等）中读取像素数据，并将其转换为 NumPy 数组
img = imread('DSC_0663.jpg') #注意路径问题
plt.imshow(img)#将数据加载到图形和坐标轴中，可进行进一步调整
plt.show()#展示图像，（所有已加载的数据

x = np.arange(0,6,0.1)
y1 = np.sin(x)
y2 = np.cos(x)#生成参数

plt.plot(x,y1,label="sin")
plt.plot(x,y2,linestyle = '--',label = 'cos')
plt.legend()#plot曲线标签label生效

plt.xlabel('x')#x,y轴标签
plt.ylabel('y')

plt.title('sin&cos')#大标题
plt.show()