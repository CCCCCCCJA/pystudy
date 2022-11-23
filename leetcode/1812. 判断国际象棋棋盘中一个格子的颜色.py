class Solution(object):
    def squareIsWhite(self, coordinates):
        """
        :type coordinates: str
        :rtype: bool
        """
        tag1 = ord(coordinates[0])
        tag2 = int(coordinates[1])
        if (tag1 % 2 == 0 and tag2 % 2 == 0) or (tag1 % 2 != 0 and tag2 % 2 != 0):
            return False
        else:
            return True

coordinates = "c7"
ss = Solution()
print(ss.squareIsWhite(coordinates))