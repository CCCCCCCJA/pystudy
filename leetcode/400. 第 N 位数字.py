class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 10:
            return n
        if n == 10:
            return 1
        if n == 11:
            return 0
        bisa = 2
        start = 9
        sumsum = 9
        while 1:
            sumsum += 10 * start * bisa
            if n > sumsum:
                bisa += 1
                start = start * 10
            else:
                tmpn = n - sumsum + 10 * start * bisa
                a = tmpn // bisa
                b = tmpn % bisa
                if b == 0:
                    resstr = str(a - 1 + 10**(bisa-1))[-1]
                else:
                    resstr = str(a - 1 + 10**(bisa-1) + 1)[b-1]
                print(resstr)
                return int(resstr)



n = 1000
ss = Solution()
ss.findNthDigit(n)
