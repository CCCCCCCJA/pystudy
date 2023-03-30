class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 1
        for ns in nums:
            res *= ns
        if res > 0:
            return 1
        elif res == 0:
            return 0
        else:
            return -1
