import numpy as np
# 布尔索引

# 二维数组
name = np.array(['小明', '小红', '校长', '小王'])
height = np.array([1,2,3,4])
scores= np.array([[94,34,34,46], [43,78,96,66], [65,67,78,45], [45,58,89,35]])
print(name)
print(scores)

print(name == '小王')

a = name == '小王'
# 布尔类索引  只有true才返回
print(scores[a])
print(scores[a].shape)
print('----------')
# 身高大于3
print(scores[height>3])
print('----------')
# 名字叫小王和身高大于3
print(scores[(name == '小王') & (height<3)])


# 将数组内的负数变成0
nums = np.array([[1,2,-3,4], [2,3,-4,5],[3,-4,5,-6],[-4,5,6,-7],[5,6,7,-8]])
print(nums)
print(nums < 0)
c = nums < 0
print(nums[c])
# 将负数赋值为0
nums[c] = 0
print(nums )