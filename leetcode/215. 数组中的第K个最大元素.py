class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        for i in range(k-1):
            maxNum = max(nums)
            # print(maxNum)
            maxIndex = nums.index(maxNum)
            nums[maxIndex] = -10 ** 4
        return max(nums)


nums = [3,2,3,1,2,4,5,5,6]
k = 4
ss = Solution()
print(ss.findKthLargest(nums, k))