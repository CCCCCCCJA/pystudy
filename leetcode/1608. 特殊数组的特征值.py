class Solution(object):
    def specialArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_max = max(nums)
        count = 0
        for i in range(nums_max+1):
            for n in nums:
                if n >= i:
                    count += 1
            if i == count:
                return count
            else:
                count = 0
                continue
        return -1

nums = [3,5]
ss = Solution()
print(ss.specialArray(nums))