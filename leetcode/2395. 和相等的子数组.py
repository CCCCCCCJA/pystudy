class Solution(object):
    def findSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        tmp =[]
        for i in range(len(nums)-1):
            sumNum = nums[i] + nums[i+1]
            if sumNum in tmp:
                return True
            else:
                tmp.append(sumNum)
        return False


nums = [0,0,0,0]
ss = Solution()
print(ss.findSubarrays(nums))
