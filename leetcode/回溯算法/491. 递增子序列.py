class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        path = []
        res = []
        def backtracking(nums, startIndex):
            if len(path) >= 2:
                res.append(path[:])
            utils = set()
            for i in range(startIndex, len(nums)):
                if nums[i] in utils or len(path) > 0 and nums[i] < path[-1]:
                    continue
                utils.add(nums[i])
                path.append(nums[i])
                backtracking(nums, i+1)
                path.pop()
        backtracking(nums, 0)
        print(res)
        return res



nums = [4,7,6,7]
ss = Solution()
ss.findSubsequences(nums)