class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        used = [0] * len(nums)
        path = []
        res = []
        def backtracking(nums, used, startIndex):
            res.append(path[:])
            if startIndex >= len(nums):
                return
            for i in range(startIndex, len(nums)):
                if i > 0 and nums[i] == nums[i - 1] and used[i - 1] == 0:
                    continue
                path.append(nums[i])
                used[i] = 1
                backtracking(nums, used, i+1)
                path.pop()
                used[i] = 0

        backtracking(nums, used, 0)
        # print(res)
        return res


nums = [0]
ss = Solution()
ss.subsetsWithDup(nums)