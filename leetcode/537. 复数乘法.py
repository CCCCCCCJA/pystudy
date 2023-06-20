class Solution(object):
    def complexNumberMultiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        n1 = num1.split('+')
        n2 = num2.split('+')
        res1 = int(n1[0]) * int(n2[0])
        res2 = int(n1[1].replace('i', '')) * int(n2[1].replace('i', ''))
        print(res1, res2)
        res3 = int(n1[0]) * int(n2[1].replace('i', '')) + int(n2[0]) * int(n1[1].replace('i', ''))
        print(res3)
        return str(res1-res2) + "+" + str(res3) + 'i'


num1 = "1+-1i"
num2 = "1+-1i"
ss = Solution()
print(ss.complexNumberMultiply(num1, num2))