class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        numstr = bin(num).replace('0b', '')
        numlist = list(numstr)
        for i in reversed(range(len(numlist))):
            if numlist[i] == '0':
                numlist[i] = '1'
            else:
                numlist[i] = '0'
        print(numlist)
        res = 0
        index = 0
        for j in reversed(range(len(numlist))):
            res += int(numlist[j]) * (2 ** index)
            index += 1
        print(res)
        return res

num = 5
ss = Solution()
ss.findComplement(num)