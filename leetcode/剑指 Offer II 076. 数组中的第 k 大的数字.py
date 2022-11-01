import heapq


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k == 0:
            return
        hp = [-x for x in nums]
        heapq.heapify(hp)
        res = []
        for i in range(k):
            res.append(-heapq.heappop(hp))
        print(hp)
        print(res)
        print(res[-1])
        return res[-1]


nums = [3,2,1,5,6,4]
k = 2
ss = Solution()
ss.findKthLargest(nums, k)
