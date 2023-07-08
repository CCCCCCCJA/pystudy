class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        count = []
        tmp = 1
        print(nums)
        for i in range(len(nums)-1):
            if nums[i] + 1 == nums[i+1]:
                tmp += 1
            elif nums[i] == nums[i+1]:
                continue
            else:
                count.append(tmp)
                tmp = 1
        count.append(tmp)
        print(count)
        return max(count)


nums = [1,2,0,1]
ss = Solution()
ss.longestConsecutive(nums)