class Solution(object):
    def mySqrt(self, x):
        if x == 0:
            return 0
        for i in range(1, 2**10):
            if i ** 2 == x:
                return i
            if i ** 2 < x and (i+1) ** 2 > x:
                return i


x = 4
ss = Solution()
print(ss.mySqrt(x))