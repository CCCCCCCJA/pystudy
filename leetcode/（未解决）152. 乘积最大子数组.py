import math


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sumsum = []
        for i in range(len(nums)):
            for j in range(1, len(nums) - i + 1):
                print(i, j, nums[i:i+j])
                sumsum.append(math.prod(nums[i:i+j]))
        print(sumsum)
        print(max(sumsum))
        return max(sumsum)



nums = [2, 3, -1, 4]
ss = Solution()
ss.maxProduct(nums)