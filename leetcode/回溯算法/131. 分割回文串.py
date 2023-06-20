class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        path = []
        res = []
        def backtracking(s, startIndex):
            if(startIndex >= len(s)):
                res.append(path[:])
                return
            for i in range(startIndex, len(s)):
                if(self.isHuiwen(s, startIndex, i)):
                    path.append(s[startIndex:i+1])
                else:
                    continue
                backtracking(s, i+1)
                path.pop()

        backtracking(s, 0)
        return res




    def isHuiwen(self, s, start, end):
        tmps = s[start:end+1]
        i = 0
        j = len(tmps)-1
        while i < j:
            if tmps[i] == tmps[j]:
                i += 1
                j -= 1
                continue
            else:
                return False
        return True


s = "aab"
ss = Solution()
ss.partition(s)