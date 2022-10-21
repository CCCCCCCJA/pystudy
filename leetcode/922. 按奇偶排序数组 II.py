class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums_j = []
        nums_o = []
        for n in nums:
            if n % 2 == 0:
                nums_o.append(n)
            else:
                nums_j.append(n)
        # print(nums_o, nums_j)
        len_len = len(nums)
        j = 0
        o = 0
        for i in range(len_len):
            if i % 2 == 0:
                nums[i] = nums_o[j]
                j += 1
            else:
                nums[i] = nums_j[o]
                o += 1
        # print(nums)
        return nums
nums = [4,2,5,7]
ss = Solution()
ss.sortArrayByParityII(nums)