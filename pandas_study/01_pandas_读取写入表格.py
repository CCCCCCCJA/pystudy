import pandas as pd

data = pd.read_excel("data/学生信息.xlsx")
# print(data)
# print(data.shape)

# 通过sheet_name参数来控制读取指定的工作表
data1 = pd.read_excel("data/学生信息.xlsx", sheet_name='测试')
print(data1)
print(data1.shape)

# 导出到excel
data1.to_excel('导出数据.xlsx')
# 导出的编号是不需要的   只需要数据
# 添加index = None
data1.to_excel('导出数据.xlsx', index=None)