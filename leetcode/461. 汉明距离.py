class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        strx = bin(x).replace('0b', '')
        stry = bin(y).replace('0b', '')
        if len(strx) > len(stry):
            stry = '0'*(len(strx)-len(stry)) + stry
        elif len(strx) < len(stry):
            strx = '0' * (len(stry) - len(strx)) + strx
        count = 0
        for i in range(len(strx)):
            if stry[i] != strx[i]:
                count += 1
        print(count)
        return count


x = 1
y = 4
ss = Solution()
ss.hammingDistance(x, y)