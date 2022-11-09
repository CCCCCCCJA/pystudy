class Solution(object):
    def topKFrequent(self, nums, k):
        setn = set(nums)
        listn = list(setn)
        count = []
        res = []
        for sn in setn:
            count.append(nums.count(sn))
        for i in range(k):
            maxn = max(count)
            indexmax = count.index(maxn)
            res.append(listn[indexmax])
            count[indexmax] = -1
        print(res)
        return res

nums = [1,1,1,2,2,3]
k = 2
ss = Solution()
ss.topKFrequent(nums, k)