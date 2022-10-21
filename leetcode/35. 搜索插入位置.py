class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums)-1
        while start <= end:
            mid = int((start + end) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
        print(start, end)
        return start

nums = [1,3,5,6]
target = 0
ss = Solution()
print(ss.searchInsert(nums, target))