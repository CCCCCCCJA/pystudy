class Solution(object):
    def swap(self, arr, i, j):
        tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp
    def exchange(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i = 0
        j = len(nums) - 1
        while i <= j:
            if (nums[i] % 2 == 0) & (nums[j] % 2 == 1):
                self.swap(nums, i, j)
                i += 1
                j -= 1
                continue
            elif nums[i] % 2 == 0:
                j -= 1
                continue
            elif nums[j] % 2 == 1:
                i += 1
                continue
            i += 1
            j -= 1
        print(nums)
        return nums

nums = [1,2,5,8,11,6,8,5,1,4,2,1,4,5]

ss = Solution()
ss.exchange(nums)
