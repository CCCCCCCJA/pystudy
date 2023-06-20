class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def backtracking(n, k, startIndex):
            if len(path) == k:
                res.append(path[:])
                return
            for i in range(startIndex, n):
                path.append(i+1)
                backtracking(n, k, i+1)
                path.pop(-1)
        path = []
        res = []
        startIndex = 0
        backtracking(n, k, startIndex)
        print(res)
        return res



n = 4
k = 2
ss = Solution()
ss.combine(n, k)