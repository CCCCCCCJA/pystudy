class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        tmp1 = nums[len(nums)-3:]
        chenji1 = 1
        for nn in tmp1:
            chenji1 *= nn
        tmp2 = nums[0:2]
        tmp2.append(nums[-1])
        chenji2 = 1
        for nn in tmp2:
            chenji2 *= nn
        return max(chenji1, chenji2)


nums = [-100,-98,-1,2,3,4]
ss = Solution()
print(ss.maximumProduct(nums))