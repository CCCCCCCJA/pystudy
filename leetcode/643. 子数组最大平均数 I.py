class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        # 超时
        # res = []
        # if len(nums) == 1:
        #     return nums[0]
        # for i in range(len(nums)-k+1):
        #     tmp = nums[i:i+k]
        #     res.append(sum(tmp))
        # print(res)
        # return max(res)
        maxTotal = total = sum(nums[:k])
        n = len(nums)
        for i in range(k, n):
            total = total - nums[i - k] + nums[i]
            maxTotal = max(maxTotal, total)
        return maxTotal / k


nums = [0,1,1,3,3]
k = 4
ss = Solution()
print(ss.findMaxAverage(nums, k))