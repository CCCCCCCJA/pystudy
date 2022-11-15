class Solution(object):
    def hasAlternatingBits(self, n):
        binstr = bin(n).replace('0b', '')
        for i in range(len(binstr)-1):
            if binstr[i] == binstr[i+1]:
                return False
        return True