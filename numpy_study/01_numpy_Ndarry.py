# 认识Ndarry
import numpy as np

# np.array就是创建一个Ndarray
# 一维
data = np.array([1,2,3,5])
print(data)
# print(type(data))
# 1 2 3 5四个数分别加上1
# Ndarray本身当做一个整体来计算
data = data + 1
print(data)

# 二维
data2 = np.array([[1,2,1],[2,1,2]])
print(data2)
# 同样可以当成一个整体来进行运算

