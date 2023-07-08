from sympy import Matrix

M = Matrix([[17, 0, -25], [0, 1, 0], [9, 0, -13]])
print(M)
print("计算矩阵的特征值")
print(M.eigenvals())

