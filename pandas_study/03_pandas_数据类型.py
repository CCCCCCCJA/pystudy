import pandas as pd

data = pd.read_csv('data/学生信息.csv', engine='python', encoding='gbk')
# 数据框
print(type(data))
print(data['班级'])
# 序列
print(type(data['班级']))
# 序列
print(data[['班级', '学号']])