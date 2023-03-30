class Solution(object):
    def isBoomerang(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        if (points[0][0] == points[1][0]) and (points[0][1] == points[1][1]):
            return False
        if (points[2][0] == points[1][0]) and (points[2][1] == points[1][1]):
            return False
        if (points[0][0] == points[2][0]) and (points[0][1] == points[2][1]):
            return False
        res = []
        if points[0][1] - points[1][1] != 0:
            res.append((points[0][0] - points[1][0]) / (points[0][1] - points[1][1]))
        else:
            res.append(10000)
        if points[2][1] - points[1][1] != 0:
            res.append((points[2][0] - points[1][0]) / (points[2][1] - points[1][1]))
        else:
            res.append(10000)
        if points[0][1] - points[2][1] != 0:
            res.append((points[0][0] - points[2][0]) / (points[0][1] - points[2][1]))
        else:
            res.append(10000)
        print(res)
        if res.count(res[0]) == 3:
            return False
        else:
            return True


points = [[18,49],[12,87],[14,71]]
ss = Solution()
print(ss.isBoomerang(points))
