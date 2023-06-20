class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        fen = minutes / 60
        fendu = 360 * fen
        shidu = 360 / 12 * ((hour + fen) % 12)
        if shidu > 180:
            shidu = shidu - 180.0
        if fendu > 180:
            fendu = fendu - 180.0
        print(shidu, fendu)
        return abs(fendu-shidu)


hour = 12
minutes = 30
ss = Solution()
print(ss.angleClock(hour, minutes))