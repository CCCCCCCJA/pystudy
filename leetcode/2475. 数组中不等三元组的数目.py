class Solution(object):
    def unequalTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = []
        for i in range(len(nums)-2):
            tmp = [nums[i]]
            for j in range(i+1, len(nums)-1):
                tmp2 = tmp.copy()
                if nums[j] in tmp:
                    continue
                tmp.append(nums[j])
                for m in range(j+1, len(nums)):
                    tmp3 = tmp.copy()
                    if nums[m] in tmp:
                        continue
                    tmp.append(nums[m])
                    if len(tmp) == 3:
                        res.append(tmp)
                    tmp = tmp3
                tmp = tmp2.copy()
        return len(res)



nums = [1,3,1,2,4]
ss = Solution()
print(ss.unequalTriplets(nums))