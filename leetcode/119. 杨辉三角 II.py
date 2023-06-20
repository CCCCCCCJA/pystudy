class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 1:
            return [1]
        res = [[1], [1, 1]]
        for i in range(2, rowIndex+1):
            tmp = res[i-1]
            tmpres = [1]
            for j in range(len(tmp)-1):
                tmpres.append(tmp[j]+tmp[j+1])
            tmpres.append(1)
            res.append(tmpres)
        # print(res)
        return res[-1]


rowIndex = 3
ss = Solution()
print(ss.getRow(rowIndex))