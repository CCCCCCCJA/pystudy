class Solution(object):
    def convertInteger(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: int
        """
        count = 0
        for i in range(32):
            a_i = A & (1 << i)
            b_i = B & (1 << i)
            if a_i ^ b_i :
                count += 1
        return count



A = -2859
B = 2
ss = Solution()
print(ss.convertInteger(A, B))