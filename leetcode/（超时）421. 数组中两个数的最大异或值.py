class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = -1
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                res = max(nums[i] ^ nums[j], res)
        return res

nums = [0]
ss = Solution()
print(ss.findMaximumXOR(nums))
