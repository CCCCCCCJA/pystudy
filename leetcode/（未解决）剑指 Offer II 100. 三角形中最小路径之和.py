class Solution(object):
    def minimumTotal(self, triangle):
        res = []
        tmpi = 0
        res.append(triangle[0][0])
        for i in range(1, len(triangle)):
            minn = min(triangle[i][tmpi], triangle[i][tmpi+1])
            res.append(minn)
            tmpi = triangle[i].index(minn)
        print(res)
        return sum(res)


triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
ss = Solution()
ss.minimumTotal(triangle)