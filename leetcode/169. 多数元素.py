from collections import Counter


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        frep = Counter(nums)
        lenlen = len(nums)
        for fr in frep:
            if frep[fr] > int(lenlen / 2):
                return fr

nums = [3,2,3]
ss = Solution()
print(ss.majorityElement(nums))