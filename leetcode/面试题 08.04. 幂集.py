class Solution(object):


    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        path = []
        result = []

        def resing(nums, startIndex):
            result.append(path[:])
            # print(path, result)
            if len(nums) <= startIndex:
                return
            for i in range(startIndex, len(nums)):
                path.append(nums[i])
                resing(nums, i + 1)
                path.pop(-1)
        resing(nums, 0)
        return result