# 超时！！！
# class Solution(object):
#     def findPairs(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
#         res = []
#         for i in range(len(nums)-1):
#             for j in range(i+1, len(nums)):
#                 if abs(nums[i] - nums[j]) == k:
#                     if ([nums[i], nums[j]] not in res) & ([nums[j], nums[i]] not in res):
#                         res.append([nums[i], nums[j]])
#         print(res)
#         return len(res)
class Solution:
    def findPairs(self, nums, k):
        visited, res = set(), set()
        for num in nums:
            if num - k in visited:
                res.add(num - k)
            if num + k in visited:
                res.add(num)
            visited.add(num)
        return len(res)


nums = [3, 1, 4, 1, 5]
k = 2
ss = Solution()
print(ss.findPairs(nums, k))