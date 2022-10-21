# class Solution(object):
#     def minSubArrayLen(self, target, nums):
#         """
#         :type target: int
#         :type nums: List[int]
#         :rtype: int
#         """
#         nums.sort()
#         print(nums)
#         tag = len(nums)
#         res = 0
#         count = 0
#         for i in reversed(range(tag)):
#             res += nums[i]
#             count += 1
#             if res >= target:
#                 return count
#             else:
#                 continue
#         return 0


# 时间复杂度过高！！！
# class Solution(object):
#     def minSubArrayLen(self, target, nums):
#         len_len = len(nums)
#         res = []
#         sum = 0
#         count = 0
#         for i in range(len_len):
#             j = i
#             while j < len_len:
#                 sum += nums[j]
#                 count += 1
#                 if sum >= target:
#                     res.append(count)
#                     break
#
#                 j += 1
#             count = 0
#             sum = 0
#         if len(res) == 0:
#             return 0
#         else:
#             res_num = min(res)
#             return res_num
import bisect
class Solution:
    def minSubArrayLen(self, s, nums):
        if not nums:
            return 0

        n = len(nums)
        ans = n + 1
        sums = [0]
        for i in range(n):
            sums.append(sums[-1] + nums[i])

        for i in range(1, n + 1):
            target = s + sums[i - 1]
            bound = bisect.bisect_left(sums, target)
            if bound != len(sums):
                ans = min(ans, bound - (i - 1))

        return 0 if ans == n + 1 else ans

target = 213
nums = [12,28,83,4,25,26,25,2,25,25,25,12]
ss = Solution()
print(ss.minSubArrayLen(target, nums))