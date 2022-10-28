class Solution(object):
    def missingNumber(self, nums):
        # 执行用时：40ms
        # nums.sort()
        # if nums[0] != 0:
        #     return 0
        # for i in range(len(nums)-1):
        #     if nums[i]+1 != nums[i+1]:
        #         return nums[i]+1
        # return nums[len(nums)-1] + 1
        lenlen = len(nums)
        truesum = lenlen * (lenlen + 1) / 2
        totalnum = sum(nums)
        return int(truesum - totalnum)

nums = [9,6,4,2,3,5,7,0,1]
ss = Solution()
print(ss.missingNumber(nums))