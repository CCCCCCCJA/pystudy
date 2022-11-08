# 超时 ！！！！！！！！！
# class Solution(object):
#     def triangleNumber(self, nums):
#         # for i in range(len(nums)):
#         #     nums[i] = nums[i] ** 2
#         count = 0
#         nums.sort()
#         for i in range(len(nums)-2):
#             for j in range(i+1, len(nums)-1):
#                 for k in range(j+1, len(nums)):
#                     if nums[i] + nums[j] > nums[k] and nums[i] + nums[k] > nums[j] and nums[j] + nums[k] > nums[i]:
#                         count += 1
#         # print(count)
#         return count
# 排序+二分查找
class Solution:
    def triangleNumber(self, nums):
        n = len(nums)
        nums.sort()
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                left, right, k = j + 1, n - 1, j
                while left <= right:
                    mid = (left + right) // 2
                    if nums[mid] < nums[i] + nums[j]:
                        k = mid
                        left = mid + 1
                    else:
                        right = mid - 1
                ans += k - j
        print(ans)
        return ans
nums = [2,2,3,4]
ss = Solution()
ss.triangleNumber(nums)