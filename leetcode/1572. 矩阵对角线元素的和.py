class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        r = len(mat[0]) - 1
        l = 0
        sum = 0
        if r % 2 == 0:
            sum -= mat[r//2][r//2]
        while l != len(mat[0]):
            sum += mat[l][l]
            sum += mat[l][r]
            l += 1
            r -= 1
        print(sum)
        return sum


mat = [[7,3,1,9],
       [3,4,6,9],
       [6,9,6,6],
       [9,5,8,5]]
ss = Solution()
ss.diagonalSum(mat)