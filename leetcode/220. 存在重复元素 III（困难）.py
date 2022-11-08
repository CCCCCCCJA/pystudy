class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        # 超时！！！！！！！！！！！！！
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if abs(nums[i] - nums[j]) <= valueDiff and abs(i - j) <= indexDiff:
                    return True
        return False


nums = [1, 5, 9, 1, 5, 9]
k = 2
t = 3
ss = Solution()
print(ss.containsNearbyAlmostDuplicate(nums, k, t))
