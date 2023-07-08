class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        path = []
        res = []
        used = [0] * len(nums)
        def backtracking(nums, used):
            if len(path) == len(nums):
                respaht = path.copy()
                res.append(respaht)
                return
            for i in range(len(nums)):
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


nums = [1,2,3]
ss = Solution()
ss.permute(nums)