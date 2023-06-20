class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # 49   "1"
        len1 = len(num1)
        len2 = len(num2)
        tmp1 = 0
        tmp2 = 0
        for i in range(len1):
            tmpac = ord(num1[i])
            tmp1 += (tmpac - 49 + 1) * 10**(len1-1)
            len1 -= 1
        for i in range(len2):
            tmpac = ord(num2[i])
            tmp2 += (tmpac - 49 + 1) * 10**(len2-1)
            len2 -= 1
        print(tmp1 * tmp2)
        return str(tmp1 * tmp2)



num1 = '123'
num2 = '456'
ss = Solution()
ss.multiply(num1, num2)