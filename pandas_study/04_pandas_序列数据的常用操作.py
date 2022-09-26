import pandas as pd
data = pd.read_csv('data/学生信息.csv', engine='python', encoding='gbk')

print(data['班级'].dtype)
print(data['学号'].dtype)
# 返回一个ndarray
# 获取班级这一列不同的取值
print(data['班级'].unique())
print(data['性别'].unique())
# 获取每一项不同取值的数量
print(data['性别'].value_counts())
# 获取某一列最大值
print(data['身高'].max())
# 获取某一列最小值
print(data['身高'].min())
# 获取某一列平均值
print(data['身高'].mean())
# 获取某一列中位数
print(data['身高'].median())