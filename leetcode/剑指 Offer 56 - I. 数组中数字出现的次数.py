class Solution(object):
    def singleNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        tmp = nums[0]
        for i in range(1, len(nums)):
            tmp ^= nums[i]
        for j in range(len(nums)):
            if nums[j].count == 1:
                num1 = nums[j]
                break
        return [num1, tmp ^ num1]
