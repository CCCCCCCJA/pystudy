# class Solution(object):
#     def totalMoney(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         if n <= 7:
#             return int((n*(n+1))/2)
#         else:
#             num = int(n / 7)
#             tmp = n - num * 7
#             if num > 2:
#                 sum = num * 28 + int((tmp*(tmp+1))/2) + (2*(num-1) - 1) * 7 + num * tmp
#             else:
#                 sum = num * 28 + int((tmp*(tmp+1))/2) + num * tmp
#             return sum
class Solution:
    def totalMoney(self, n):
        week, day = 1, 1
        res = 0
        for i in range(n):
            res += week + day - 1
            day += 1
            if day == 8:
                day = 1
                week += 1
        return res

n = 26
ss = Solution()
print(ss.totalMoney(n))