from collections import Counter


class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        setnums = set(nums)
        frep = dict(Counter(nums))
        res = []
        for sn in setnums:
            if frep[sn] == 2:
                res.append(sn)
        print(res)
        return res


nums = [4,3,2,7,8,2,3,1]
ss = Solution()
ss.findDuplicates(nums)