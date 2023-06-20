class Solution(object):
    def countKDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if abs(nums[i]-nums[j]) == k:
                    count += 1
        print(count)
        return count



nums = [1,2,2,1]
k = 1
ss = Solution()
ss.countKDifference(nums, k)