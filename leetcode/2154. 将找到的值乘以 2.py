class Solution(object):
    def findFinalValue(self, nums, original):
        while 1:
            if original in nums:
                original *= 2
            else:
                return original

