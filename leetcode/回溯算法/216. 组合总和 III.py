class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        def backtracking(n, k, startIndex):
            if sum(path) > n:
                return
            if sum(path) == n and len(path) == k:
                res.append(path[:])
                return
            for i in range(startIndex, 9-(k-len(path))+1):
                path.append(i + 1)
                backtracking(n, k, i + 1)
                path.pop(-1)
        res = []
        path = []
        startIndex = 0
        backtracking(n, k, startIndex)
        # print(res)
        return res



k = 3
n = 9
ss = Solution()
ss.combinationSum3(k, n)