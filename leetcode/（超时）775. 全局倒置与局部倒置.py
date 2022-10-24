class Solution(object):
    def isIdealPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count_all = 0
        count_local = 0
        len_len = len(nums)
        for i in range(len_len-1):
            for j in range(i+1, len_len):
                if nums[i] > nums[j]:
                    count_all += 1
            if nums[i] > nums[i+1]:
                count_local += 1
        print(count_all, count_local)
        if count_local == count_all:
            return True
        else:
            return False


nums = [1, 2, 0]
ss = Solution()
print(ss.isIdealPermutation(nums))