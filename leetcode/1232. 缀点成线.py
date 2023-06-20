class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        point1 = coordinates[0]
        point2 = coordinates[1]
        x1 = point1[0]
        y1 = point1[1]
        x2 = point2[0]
        y2 = point2[1]
        if x1 == x2:
            for i in range(2, len(coordinates)):
                if x1 != coordinates[i][0]:
                    return False
            return True
        for i in range(2, len(coordinates)):
            x = coordinates[i][0]
            y = coordinates[i][1]
            if y != ((y2-y1) * (x-x1)) / (x2-x1) + y1:
                return False
        return True

coordinates = [[0,0],[0,1],[0,-1]]
ss = Solution()
print(ss.checkStraightLine(coordinates))