class Solution:
    def thirdMax(self, nums):
        set_nums = set(nums)
        len_num = len(set_nums)
        if len_num < 3:
            return max(set_nums)
        else:
            for i in range(2):
                max_num = max(set_nums)
                set_nums.remove(max_num)
            return max(set_nums)


nums = [1, 2, 2, 3]
ss = Solution()
print(ss.thirdMax(nums))