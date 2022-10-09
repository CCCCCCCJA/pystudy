class Solution(object):
    def missingNumber(self, nums):
        nums.sort()
        count = 0
        for i in range(len(nums)):
            if nums[i] == i:
                count += 1
                continue
            else:
                return i
        return count

nums = [9,6,4,2,3,5,7,0,1]
ss = Solution()
print(ss.missingNumber(nums))


