import math
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n % 3 != 0:
            return False
        while n % 3 == 0:
            n = int(n/3)
        return n == 1
        # while (tmp != 1) & (tmp > 1):
        #     tmp = int(tmp / 3)
        # if tmp == 1:
        #     return True
        # else:
        #     return False

n = 27
ss = Solution()
print(ss.isPowerOfThree(n))