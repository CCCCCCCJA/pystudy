class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []
        ch = ['.' * n for _ in range(n)]
        def backtracking(ch, n, row):
            if row == n:
                res.append(ch[:])
                return
            for i in range(n):
                if isValid(row, i, ch):
                    ch[row] = ch[row][:i] + 'Q' + ch[row][i + 1:]  # 放置皇后
                    backtracking(ch, n, row+1)  # 递归到下一行
                    ch[row] = ch[row][:i] + '.' + ch[row][i + 1:]  # 回溯，撤销当前位置的皇后

        def isValid(row, col, ch):
            # 检查列
            for i in range(row):
                if ch[i][col] == 'Q':
                    return False  # 当前列已经存在皇后，不合法

            # 检查 45 度角是否有皇后
            i, j = row - 1, col - 1
            while i >= 0 and j >= 0:
                if ch[i][j] == 'Q':
                    return False  # 左上方向已经存在皇后，不合法
                i -= 1
                j -= 1

            # 检查 135 度角是否有皇后
            i, j = row - 1, col + 1
            while i >= 0 and j < len(ch):
                if ch[i][j] == 'Q':
                    return False  # 右上方向已经存在皇后，不合法
                i -= 1
                j += 1

            return True  # 当前位置合法

        backtracking(ch, n, 0)
        # print(res)
        return res
ss = Solution()
ss.solveNQueens(1)


