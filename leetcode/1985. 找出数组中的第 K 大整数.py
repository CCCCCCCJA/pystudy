class Solution(object):
    def kthLargestNumber(self, nums, k):
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        for i in range(len(nums)):
            nums[i] = int(nums[i])
        nums.sort()
        print(nums)
        print('"' + str(nums[len(nums)-k]) + '"')
        return '"' + str(nums[k-1]) + '"'

nums = ["0","0"]
k = 2
ss = Solution()
ss.kthLargestNumber(nums, k)