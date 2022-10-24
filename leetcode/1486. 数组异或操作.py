class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        nums = []
        for i in range(n):
            nums.append(start + 2 * i)
        res = 0
        for num in nums:
            res ^= num
        print(res)
        return res


n = 5
start = 0
ss = Solution()
ss.xorOperation(n, start)