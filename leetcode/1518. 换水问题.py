class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        count = 0
        while 1:
            if count == 0:
                count += numBottles
            tmp = int(numBottles / numExchange)
            if count != 0:
                count += tmp
            rm = numBottles - (numExchange * tmp)
            numBottles = tmp + rm
            if numBottles < numExchange:
                return count


numBottles = 9
numExchange = 3
ss = Solution()
print(ss.numWaterBottles(numBottles, numExchange))
