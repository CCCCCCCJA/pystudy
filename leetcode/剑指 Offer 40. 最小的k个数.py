import heapq
class Solution(object):
    def getLeastNumbers(self, arr, k):
        # arr.sort()
        # return arr[:k]
        # 小根堆
        if k == 0:
            return list()
        hp = [-x for x in arr[:k]]
        heapq.heapify(hp)
        for i in range(k, len(arr)):
            if -hp[0] > arr[i]:
                heapq.heappop(hp)
                heapq.heappush(hp, -arr[i])
        ans = [-x for x in hp]
        return ans

arr = [3,35,4,7,8,5]
k = 2
ss = Solution()
print(ss.getLeastNumbers(arr, k))
