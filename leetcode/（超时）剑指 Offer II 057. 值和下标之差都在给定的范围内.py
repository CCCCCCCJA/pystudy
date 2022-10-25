class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        for i in range(len(nums)-1):
            for j in range(0, k):
                if i+j+1 > len(nums) - 1:
                    break
                if abs(nums[i] - nums[i+j+1]) <= t:
                    return True
        return False
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if (abs(nums[i] - nums[j]) <= t) & (abs(i - j) <= k):
        #             print(i, j)
        #             return True
        # return False


nums = [1,5,9,1,5,9]
k = 2
t = 3
ss = Solution()
print(ss.containsNearbyAlmostDuplicate(nums, k, t))