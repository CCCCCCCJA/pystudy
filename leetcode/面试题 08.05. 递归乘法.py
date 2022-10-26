class Solution(object):
    def multiply(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: int
        """
        res = 0
        maxn = max(A, B)
        if maxn == A:
            if B == 0:
                return 0
            else:
                res += A + self.multiply(A, B-1)
                return res
        else:
            if A == 0:
                return 0
            else:
                res += B + self.multiply(A-1, B)
                return res


A = 1
B = 10
ss = Solution()
print(ss.multiply(B, A))