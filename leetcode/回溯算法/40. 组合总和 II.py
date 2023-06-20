class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        path = []
        used = [0] * len(candidates)
        candidates.sort()
        def backtracking(candidates, used, target, startIndex):
            if sum(path) > target:
                return
            if sum(path) == target:
                res.append(path[:])
                return
            for i in range(startIndex, len(candidates)):
                if sum(path) > target:
                    break
                if i > 0 and candidates[i] == candidates[i - 1] and used[i - 1] == 0:
                    continue
                used[i] = 1
                path.append(candidates[i])
                backtracking(candidates, used, target, i + 1)
                used[i] = 0
                path.pop()
        backtracking(candidates, used, target, 0)
        print(res)
        return res


candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
ss = Solution()
ss.combinationSum(candidates, target)
