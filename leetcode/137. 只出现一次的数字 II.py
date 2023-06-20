import collections


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        frequency = collections.Counter(nums)
        print(frequency)
        tmpset = set(nums)
        for ts in tmpset:
            if frequency[ts] == 1:
                return ts



nums = [2,2,3,2]
ss = Solution()
ss.singleNumber(nums)