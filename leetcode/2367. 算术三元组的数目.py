class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        """
        :type nums: List[int]
        :type diff: int
        :rtype: int
        """
        count = 0
        len_len = len(nums)
        for i in range(len_len):
            for j in range(i+1, len_len):
                for k in range(j+1, len_len):
                    if (i < j < k) & (nums[j] - nums[i] == diff) & (nums[k] - nums[j] == diff):
                        count += 1
        return count

nums = [0,1,4,6,7,10]
diff = 3
ss = Solution()
print(ss.arithmeticTriplets(nums, diff))