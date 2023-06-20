class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # res = []
        # for i in range(len(nums)):
        #     count = 0
        #     for j in range(len(nums)):
        #         if nums[i] > nums[j]:
        #             count += 1
        #     res.append(count)
        # print(res)
        # return res
        cns = [0]*100
        for ns in nums:
            cns[ns] += 1
        res = []
        for ns in nums:
            print(cns[:ns])
            res.append(sum(cns[:ns]))
        # print(cns)
        print(res)
        return res




nums = [8, 1, 2, 2, 3]
ss = Solution()
ss.smallerNumbersThanCurrent(nums)