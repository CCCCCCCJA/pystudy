class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        strn = bin(n)
        return strn.count('1')


n = 11
ss = Solution()
print(ss.hammingWeight(n))