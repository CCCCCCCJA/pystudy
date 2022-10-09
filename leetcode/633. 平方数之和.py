# 时间复杂度太高# 时间复杂度太高
# 时间复杂度太高# 时间复杂度太高# 时间复杂度太高# 时间复杂度太高# 时间复杂度太高# 时间复杂度太高# 时间复杂度太高
# class Solution(object):
#     def judgeSquareSum(self, c):
#         """
#         :type c: int
#         :rtype: bool
#         """
#         for i in range(c+1):
#             tmp = (c - int(i**2))**0.5
#             if tmp == int(tmp):
#                 return True
#         return False
import time
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        low, high = 0, int(c**0.5)
        while low <= high:
            sumOf = low * low + high * high
            if sumOf == c:
                return True
            elif sumOf < c:
                low += 1
            else:
                high -= 1
        return False
start_time = time.time()
c = 10000000
ss = Solution()
print(ss.judgeSquareSum(c))
end_time = time.time()
sum_time = end_time - start_time
print(start_time, end_time, sum_time)