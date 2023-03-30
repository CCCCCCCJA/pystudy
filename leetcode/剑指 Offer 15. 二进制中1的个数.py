class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        strstr = bin(n).replace('0b', '')
        print(strstr)
        return strstr.count('1')

n = 4294967293
ss = Solution()
print(ss.hammingWeight(n))