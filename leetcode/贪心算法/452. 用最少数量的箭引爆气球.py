class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        count = 1
        points.sort()
        minlist = points[0]
        print(points)
        for i in range(1, len(points)):
            if points[i][0] > minlist[1]:
                count += 1
                minlist = points[i]
                continue
            elif points[i][1] >= minlist[1]:
                continue
            elif points[i][1] < minlist[1]:
                minlist = points[i]

        print(count)
        return count

points = [[1,2],[2,3],[3,4],[4,5]]
ss = Solution()
ss.findMinArrowShots(points)