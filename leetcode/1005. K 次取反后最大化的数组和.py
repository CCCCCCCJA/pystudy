class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 执行用时：80ms
        # if k == 1:
        #     minn = min(nums)
        #     indexn = nums.index(minn)
        #     nums[indexn] = -nums[indexn]
        #     print(sum(nums))
        #     return sum(nums)
        # for i in range(k):
        #     if min(nums) < 0:
        #         minn = min(nums)
        #         indexn = nums.index(minn)
        #         nums[indexn] = -nums[indexn]
        #         continue
        #     if min(nums) == 0:
        #         continue
        #     if min(nums) > 0:
        #         minn = min(nums)
        #         indexn = nums.index(minn)
        #         nums[indexn] = -nums[indexn]
        #         continue
        # print(sum(nums))
        # return sum(nums)
        # 卡尔
        nums.sort(key=lambda x: abs(x))
        nums = nums[::-1]
        print(nums)
        for i in range(len(nums)):
            if k > 0 and nums[i] < 0:
                nums[i] = -nums[i]
                k -= 1
        if k % 2 == 1:
            nums[-1] = -nums[-1]
        return sum(nums)


nums = [3, -1, 0, 2]
k = 3
ss = Solution()
print(ss.largestSumAfterKNegations(nums, k))
