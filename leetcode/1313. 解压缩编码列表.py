class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(0, len(nums), 2):
            # print(i)
            for j in range(nums[i]):
                res.append(nums[i + 1])
        # print(res)
        return res


nums = [1, 2, 3, 4]
ss = Solution()
ss.decompressRLElist(nums)
