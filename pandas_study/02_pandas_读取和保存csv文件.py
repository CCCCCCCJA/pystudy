import pandas as pd

data = pd.read_csv('data/学生信息.csv', engine='python', encoding='gbk')
print(data)
# 与excel文件相同  保存时添加index=None  取消索引
data.to_csv('学生信息.csv', index=None)