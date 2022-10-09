class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        count = nums.count(target)
        return count

nums = [5,7,7,8,8,10]
target = 6
ss = Solution()
print(ss.search(nums, target))