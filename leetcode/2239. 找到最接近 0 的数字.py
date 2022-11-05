class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i, n in enumerate(nums):
            if n > 0:
                num1 = nums[i]
                num2 = nums[i-1]
                if abs(num1) > abs(num2):
                    return nums[i-1]
                else:
                    return nums[i]
            if n == 0:
                return 0
        return nums[-1]