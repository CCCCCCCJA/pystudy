class Solution(object):
    def thousandSeparator(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n < 1000:
            return str(n)
        strn = str(n)
        strn = strn[::-1]
        res = ''
        count = 0
        for i in range(len(strn)):
            count += 1
            if count == 3 and i != len(strn)-1:
                res = res + strn[i] + '.'
                count = 0
            else:
                res += strn[i]
        # print(strn)
        print(res[::-1])
        return res[::-1]


n = 123456789
ss = Solution()
ss.thousandSeparator(n)