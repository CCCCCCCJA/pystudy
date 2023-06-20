class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        if nums.count(0) == len(nums):
            return 0
        while 1:
            minnum = min(filter(lambda x: x > 0, nums))
            print(minnum)
            for i in range(len(nums)):
                if nums[i] != 0:
                    nums[i] = nums[i] - minnum
            print(nums)
            count += 1
            if nums.count(0) == len(nums):
                break
        return count


nums = [0]
ss = Solution()
ss.minimumOperations(nums)