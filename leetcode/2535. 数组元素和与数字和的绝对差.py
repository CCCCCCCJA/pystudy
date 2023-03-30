class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum1 = sum(nums)
        print(sum1)
        sum2 = 0
        for i in range(len(nums)):
            tmp = nums[i]
            while tmp >= 10:
                gewei = tmp % 10
                sum2 += gewei
                tmp = tmp // 10
            sum2 += tmp
        print(sum2)
        print(abs(sum1-sum2))
        return abs(sum1-sum2)


nums = [2,7,8,10,8,10,1,10,5,9]
ss = Solution()
ss.differenceOfSum(nums)