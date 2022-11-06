class Solution(object):
    def twoSum(self, nums, target):
        # 超时！！！！！！！！！！！！！！！
        # tmp = []
        # for n in nums:
        #     if n <= target:
        #         tmp.append(n)
        # tmptmp = []
        # for i in range(len(tmp)):
        #     if target - tmp[i] in tmptmp:
        #         return [target-tmp[i], tmp[i]]
        #     else:
        #         tmptmp.append(tmp[i])
        i = 0
        j = len(nums) - 1
        while i < j:
            if nums[i] + nums[j] > target:
                j -= 1
            elif nums[i] + nums[j] < target:
                i += 1
            else:
                return [nums[i], nums[j]]

nums = [10,26,30,31,47,60]
target = 40
ss = Solution()
print(ss.twoSum(nums, target))