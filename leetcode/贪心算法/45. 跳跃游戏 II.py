class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        cur = 0
        next = 0
        count = 0
        for i in range(len(nums)):
            next = max(next, i+nums[i])
            if i == cur:
                if (cur != len(nums)-1):
                    count += 1
                    cur = next
                    if cur >= len(nums)-1:
                        break
                else:
                    break
        print(count)
        return count

nums = [5,9,3,2,1,0,2,3,3,1,0,0]
ss = Solution()
ss.jump(nums)
