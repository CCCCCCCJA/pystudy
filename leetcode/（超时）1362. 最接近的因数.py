class Solution(object):
    def closestDivisors(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = []
        for i in range(1, num+2//2+1):
            if (num+1)//i == (num+1)/i:
                res.append([i, (num+1)//i])
            elif (num+2)//i == (num+2)/i:
                res.append([i, (num + 2) // i])
        resres = []
        if len(res) == 0:
            return []
        for r in res:
            resres.append(abs(r[0] - r[1]))
        maxres = min(resres)
        return res[resres.index(maxres)]



num = 8
ss = Solution()
print(ss.closestDivisors(num))