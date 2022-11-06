class Solution(object):
    def getMaximumGenerated(self, n):
        if n == 0:
            return 0
        res = [0 for x in range(n+1)]
        res[1] = 1
        for i in range(2,n+1):
            if i % 2 == 0:
                res[i] = res[i//2]
            else:
                res[i] = res[i//2] + res[i//2+1]
        print(res)
        return max(res)

n = 7
ss = Solution()
ss.getMaximumGenerated(n)