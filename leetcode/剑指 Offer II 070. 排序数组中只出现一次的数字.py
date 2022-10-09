class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tag = nums[0]
        len_nums = len(nums)
        if len_nums == 1: return tag
        for i in range(1, len_nums):
            if nums[i] != tag:
                if i == len_nums-1: return nums[i]
                if nums[i+1] != nums[i]:
                    return nums[i]
                elif i == 1:
                    return tag
                else:
                    tag = nums[i]
                    continue
            else:
                continue
nums = [1,2,2,3,3]
ss = Solution()
print(ss.singleNonDuplicate(nums))
