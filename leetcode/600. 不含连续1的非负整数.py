class Solution(object):
    def findIntegers(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        for i in range(n+1):
            tmp = bin(i).replace('0b', '')
            if '11' not in tmp:
                count += 1
        return count




n = 5
ss = Solution()
ss.findIntegers(n)