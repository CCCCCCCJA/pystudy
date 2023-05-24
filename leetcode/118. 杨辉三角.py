class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 1:
            return [1]
        res = [[1], [1, 1]]
        for i in range(2, numRows):
            tmp = res[i-1]
            tmpres = [1]
            for j in range(len(tmp)-1):
                tmpres.append(tmp[j]+tmp[j+1])
            tmpres.append(1)
            res.append(tmpres)
        # print(res)
        return res


ss = Solution()
ss.generate(4)