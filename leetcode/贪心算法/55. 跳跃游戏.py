class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 自己写的  4600ms
        # tag = [0] * len(nums)
        # tag[0] = 1
        # for i in range(len(nums)):
        #     if tag[i] == 1:
        #         index = i+1
        #         while index <= i + nums[i]:
        #             if index > len(nums)-1:
        #                 return True
        #             tag[index] = 1
        #             index += 1
        #     else:
        #         return False
        # return True
        # 60ms
        cover = 0
        for i in range(len(nums)):
            if cover < i:
                return False
            cover = max(cover, i + nums[i])
            if cover >= len(nums)-1:
                return True
        return False



nums = [3,2,1,0,4]
ss = Solution()
print(ss.canJump(nums))