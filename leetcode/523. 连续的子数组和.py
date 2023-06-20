# class Solution(object):
#     def checkSubarraySum(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: bool
#         """
#         for i in range(2, len(nums)+1):
#             for j in range(len(nums)-i+1):
#                 sumn = sum(nums[j:j + i])
#                 if sumn % k == 0 or sumn == 0:
#                     return True
#         return False

# 同余定理
class Solution:
    def checkSubarraySum(self, nums, k):
        if len(nums) < 2: return False
        dp, cur = {0: -1}, 0
        for idx, num in enumerate(nums):
            cur += num
            if k != 0:
                cur %= k
            pre = dp.setdefault(cur, idx)
            if idx - pre > 1:
                return True
        return False


nums = [23, 2, 4, 6, 7]
k = 6
ss = Solution()
print(ss.checkSubarraySum(nums, k))
