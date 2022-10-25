class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        index_res = []
        resres = []
        for point in points:
            tmp = point[0] ** 2 + point[1] ** 2
            res.append(tmp)
        print(res)
        for i in range(k):
            nummin = min(res)
            index_min = res.index(nummin)
            index_res.append(index_min)
            res[index_min] = 10 ** 8 + 1
        print(res)
        print(index_res)
        for ir in index_res:
            resres.append(points[ir])
        print(resres)
        return resres



points = [[1,3],[-2,2]]
k = 1
ss = Solution()
ss.kClosest(points, k)