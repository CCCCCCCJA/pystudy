class Solution(object):
    def swap(self, arr, i, j):
        tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i = 0
        j = len(nums) - 1
        while i < j:
            if (nums[i] % 2 == 1) & (nums[j] % 2 == 0):
                self.swap(nums, i, j)
                i += 1
                j -= 1
                continue
            if nums[i] % 2 == 0:
                i += 1
            if nums[j] % 2 == 1:
                j -= 1
        # print(nums)
        return nums

nums = [0]
ss = Solution()
ss.sortArrayByParity(nums)