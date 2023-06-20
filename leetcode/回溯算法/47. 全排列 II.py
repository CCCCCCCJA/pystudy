class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        path = []
        res = []
        used = [0] * len(nums)
        nums.sort()
        def backtracking(nums, used):
            if len(path) == len(nums):
                respaht = path.copy()
                res.append(respaht)
                return
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1] and used[i-1] == 0:
                    continue
                if used[i] == 1:
                    continue
                used[i] = 1
                path.append(nums[i])
                backtracking(nums, used)
                used[i] = 0
                path.pop(-1)
        backtracking(nums, used)
        print(res)
        return res


nums = [3,3,0,3]
ss = Solution()
ss.permuteUnique(nums)