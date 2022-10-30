class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 执行用时：28ms
        # res = []
        # for i in range(len(nums)):
        #     if i == 0:
        #         res.append(nums[i])
        #         continue
        #     res.append(nums[i] + res[i-1])
        # print(res)
        # return res

        # 执行用时：20ms
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i-1]
        print(nums)
        return nums


nums = [1,2,3,4]
ss = Solution()
ss.runningSum(nums)
