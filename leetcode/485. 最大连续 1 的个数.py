class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        tmp = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                tmp += 1
            else:
                if tmp > count:
                    count = tmp
                tmp = 0
        if tmp > count:
            count = tmp
        print(count)
        return count


nums = [1,1,0,1,1,1]
ss = Solution()
ss.findMaxConsecutiveOnes(nums)


frequency = collections.Counter(s)