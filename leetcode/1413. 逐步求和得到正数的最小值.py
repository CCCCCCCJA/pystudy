class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = abs(nums[0])
        while 1:
            tag = 0
            sum = res
            for nn in nums:
                sum += nn
                if sum > 0:
                    continue
                else:
                    tag = 1
                    break
            if tag:
                res += 1
            else:
                return res

nums = [-3,2,-3,4,2]
ss = Solution()
print(ss.minStartValue(nums))