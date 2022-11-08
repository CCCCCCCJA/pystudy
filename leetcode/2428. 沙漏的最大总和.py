class Solution(object):
    def maxSum(self, grid):
        len1 = len(grid)
        len2 = len(grid[0])
        # print(len1, len2)
        maxsum = -1
        for i in range(len1-2):
            for j in range(len2-2):
                sum = grid[i][j] + grid[i][j+1] + grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j] \
                    + grid[i+2][j+1] + grid[i+2][j+2]
                if sum > maxsum:
                    maxsum = sum
        return maxsum



grid = [[1,2,3],[4,5,6],[7,8,9]]
ss = Solution()
print(ss.maxSum(grid))