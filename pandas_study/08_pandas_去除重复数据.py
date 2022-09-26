import pandas as pd

data = pd.read_excel('data/重复数据样本.xlsx')
print(data)
print(data.shape)
print('___________')

# 计算重复数据的数量
# 重复返回true   不重复返回false
print(data.duplicated().sum())
# print(data[data.duplicated()])

# 快速去除重复数据

print(data.drop_duplicates().shape)