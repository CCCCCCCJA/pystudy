class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 执行用时：80ms
        if k == 1:
            minn = min(nums)
            indexn = nums.index(minn)
            nums[indexn] = -nums[indexn]
            print(sum(nums))
            return sum(nums)
        for i in range(k):
            if min(nums) < 0:
                minn = min(nums)
                indexn = nums.index(minn)
                nums[indexn] = -nums[indexn]
                continue
            if min(nums) == 0:
                continue
            if min(nums) > 0:
                minn = min(nums)
                indexn = nums.index(minn)
                nums[indexn] = -nums[indexn]
                continue
        print(sum(nums))
        return sum(nums)





nums = [3,-1,0,2]
k = 3
ss = Solution()
ss.largestSumAfterKNegations(nums, k)
