class Solution(object):
    def findKthPositive(self, arr, k):
        lenlen = len(arr)
        res = []
        for i in range(1, lenlen+k+1):
            if i not in arr:
                res.append(i)
        print(res)
        return res[k-1]


arr = [1,2,3,4]
k = 2
ss = Solution()
print(ss.findKthPositive(arr, k))