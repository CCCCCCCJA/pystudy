class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        set_n = set(nums)
        count = []
        list_n = list(set_n)
        lenlen = len(nums)
        for sn in set_n:
            count.append(nums.count(sn))
        # print(count)
        resindex = count.index(lenlen/2)
        return list_n[resindex]


nums = [2,1,2,5,3,2]
ss = Solution()
print(ss.repeatedNTimes(nums))