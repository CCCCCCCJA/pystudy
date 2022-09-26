import pandas as pd
data = pd.read_csv('data/学生信息.csv', engine='python', encoding='gbk')

# 查看数据框的前几条数据
# 预览数据
print(data.head(10))

# 数据属性
print(data.info())

# 统计信息
print(data.describe())

# 表头信息
print(data.columns)
print(data.columns[1])
# 改变表头信息
print(data.rename(columns={'体重': '测试'}))



