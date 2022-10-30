from collections import Counter


class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        setnums = set(nums)
        frep = dict(Counter(nums))
        res = []
        print(setnums, frep)
        for sn in nums:
            if frep[sn] == 1:
                res.append(sn)

        print(res)
        return sum(res)

nums = [1,2,3,2]
ss = Solution()
ss.sumOfUnique(nums)
