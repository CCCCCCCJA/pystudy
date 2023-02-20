class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minn = min(nums)
        maxn = max(nums)
        if maxn % minn == 0:
            return minn
        for i in reversed(range(1, minn)):
            if maxn % i == 0 and minn % i == 0:
                return i