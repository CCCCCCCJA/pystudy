class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        path = []
        def backtracking(candidates, index, target):

            if sum(path) == target:
                res.append(path[:])
                return
            for i in range(index, len(candidates)):
                if sum(path) > target:
                    break
                path.append(candidates[i])
                backtracking(candidates, i, target)
                path.pop()
        backtracking(candidates, 0, target)
        print(res)
        return res



candidates = [2,3,5]
target = 8
ss = Solution()
ss.combinationSum(candidates, target)