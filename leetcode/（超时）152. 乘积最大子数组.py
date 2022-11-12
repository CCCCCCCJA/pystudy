from functools import reduce


class Solution(object):
    def maxProduct(self, nums):
        lenlen = len(nums)
        maxnum = -1
        for i in range(2, lenlen + 1):
            for j in range(lenlen - i + 1):
                tmp = nums[j:j + i]
                sum = reduce((lambda x, y: x * y), tmp)
                if sum > maxnum:
                    maxnum = sum
        # print(maxnum)
        return maxnum


nums = [-4, -3]
ss = Solution()
print(ss.maxProduct(nums))
