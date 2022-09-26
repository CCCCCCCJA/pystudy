import pandas as pd
data = pd.read_csv('data/学生信息.csv', engine='python', encoding='gbk')

# 单条件筛选数据
# print(data['性别']=='男')
print('------------------------------------')
# print(data[data['性别']=='男'])

# 身高大于180
# print(data[data['身高']>180])


# 多条件筛选数据
# 性别为女生   身高大于180
# data['性别']=='女' & data['身高']>180
print(data[(data['性别']=='女') & (data['身高']>180)])
print('-------------------')
# 性别为女生或者身高小于180
print(data[(data['性别']=='女') | (data['身高']<180)])
# 性别为女生且身高小于180且班级为一班
print('-------------------')
print(data[(data['性别']=='女') & (data['身高']<180) & (data['班级']=='1班')])

