class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        set_nums = set(nums)
        count = []
        num = []
        res = []
        for sn in set_nums:
            num.append(sn)
            count.append(nums.count(sn))
        print(count, num)
        for i in range(k):
            max_num = max(count)
            index_max = count.index(max_num)
            res.append(num[index_max])
            count[index_max] = -1
        print(res)
        return res

nums = [1,1,1,2,2,3]
k = 2
ss = Solution()
ss.topKFrequent(nums, k)