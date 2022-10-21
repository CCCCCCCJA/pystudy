class Solution(object):
    def findLonely(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        set_nums = set(nums)
        # print(set_nums)
        list_nums = list(set_nums)
        # print(list_nums)
        count = []
        for sn in list_nums:
            count.append(nums.count(sn))
        # print(count)
        for i in range(len(count)):
            if count[i] == 1:
                print(list_nums[i])
                if (nums.count(list_nums[i] - 1) == 0) & (nums.count(list_nums[i] + 1) == 0):
                    res.append(list_nums[i])
        # print(res)
        return res


nums = [1,3,5,3]
ss = Solution()
print(ss.findLonely(nums))
