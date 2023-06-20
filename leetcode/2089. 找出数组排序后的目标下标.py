class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if target not in nums:
            return []
        count = nums.count(target)
        nums.sort()
        index = nums.index(target)
        res = []
        for i in range(count + 1):
            res.append(index + i)
        return res

nums = [1,2,5,2,3]
target = 4

