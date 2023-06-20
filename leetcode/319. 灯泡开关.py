# class Solution(object):
#     def bulbSwitch(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         if n == 0:
#             return 0
#         if n == 1:
#             return 1
#         res = [1] * n
#         for i in range(2, n+1):
#             index = i-1
#             while index < n:
#                 if res[index] == 1:
#                     res[index] = 0
#                 else:
#                     res[index] = 1
#                 index += i
#         print(res)
#         return res.count(1)
from math import sqrt


# 数论
class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(sqrt(n + 0.5))



n = 9999999
ss = Solution()
print(ss.bulbSwitch(n))