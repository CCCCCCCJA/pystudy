import pandas as pd
data = pd.read_csv('data/学生信息.csv', engine='python', encoding='gbk')

# 序列数据排序
# 从小到大
# print(data['身高'].sort_values())
# 只看前几个
# print(data['身高'].sort_values().head())
# 从大到小   指定参数ascending=False变为降序
# print(data['身高'].sort_values(ascending=False))

# 数据框排序
# by指定参数进行排序
# print(data.sort_values(by='身高')) # 升序
# print(data.sort_values(by='身高', ascending=False)) # 降序

# 多个参数排序
print(data.sort_values(by=['身高', '体重']))











