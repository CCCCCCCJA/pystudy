class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        nums_set = set(nums)
        n = int(len(nums)/3) # 计算机技术与发展 计算机应用
        for s in nums_set:
            num = nums.count(s)
            if num > n:
                res.append(s)
        print(res)
        return res


nums = [3,2,3]
ss = Solution()
ss.majorityElement(nums)