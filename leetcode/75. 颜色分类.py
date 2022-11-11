from collections import Counter

# 执行用时：8 ms, 在所有 Python 提交中击败了99.24%的用户
class Solution(object):
    def sortColors(self, nums):
        dictnum = Counter(nums)
        count = 0
        for i in range(3):
            tmp = dictnum[i]
            for j in range(tmp):
                nums[count] = i
                count += 1
        print(nums)
        return nums


nums = [2,0,2,1,1,0]
ss = Solution()
ss.sortColors(nums)