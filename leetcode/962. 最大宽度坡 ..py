class Solution(object):
    def maxWidthRamp(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmp = []
        len_nums = len(nums)
        res = 0
        for i in range(len_nums):
            for j in range(i, len_nums):
                if (j - i) < res:
                    continue
                if nums[i] <= nums[j]:
                    tmp.append(j - i)
                    res = max(tmp)
        return max(tmp)
        # print(max(tmp))

nums = [6,0,8,2,1,5]
ss = Solution()
ss.maxWidthRamp(nums)