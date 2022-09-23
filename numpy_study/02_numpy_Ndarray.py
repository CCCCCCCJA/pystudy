# Ndarray属性

# Ndarray.ndim   查看Ndarray的维度
# Ndarray.shape  查看Ndarray的形状
# Ndarray.size   查看Ndarray的元素个数
# Ndarray.dtype  查看Ndarray的元素数据类型
# Ndarray.itemsize   查看Ndarray中的每个元素的字节大小

import numpy as np
data1 = np.array([1,55,8.2])
data2 = np.array([[1,2,4,5],[2,5,8,9]])
print(data1.ndim)
print(data2.ndim)
print('------')
print(data2.shape)
# 小心下标越界
print(data1.shape[0])

# 4 表示4个字节
print(data2.itemsize)
# 8 表示8个字节
print(data1.itemsize)
