import numpy as np

data1 = np.array([1,2,3,4,5])
print(data1)
# 可以通过方括号加下标进行索引
print(data1[0])
print(data1[1])
print('---------------------------')
data2 = np.array([[1,3,4],[1,23,4]])
print(data2)
print(data2[0])
# print(data2[0][2])
print(data2[0,2])
print('---------------------------')
data3 = np.array([[[1]],[[2]]])

print(data3)
print(data3[1, 0, 0])
print('==================')

# 一维切片
# 前三个  0可以省略print(data1[:3])
print(data1[0:3])

# 取出奇数位置的数据
# start_index:end_index:step
print(data1[::2])
print('==================')
data4 = np.arange(10)
print(data4)
# 奇数位置
print(data4[::2])
# 偶数位置
print(data4[1::2])

# 奇数位置+1
data5 = data4[::2] + 1
print(data5)
print('==================')
# 二维数组切片

data6 = np.array([[1,2,3],[4,5,6]])

print(data6.shape)
# 前两列
print(data6[:,:2])
#
print(data6[:1,:1])
print('==================')
# 三维数组切片

data7 = np.array([[[1,2],[3,4]]])
print(data7.shape)
print(data7)

print(data7[:, :, :1])


