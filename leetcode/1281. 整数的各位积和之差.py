class Solution(object):
    def subtractProductAndSum(self, n):
        strn = str(n)
        sumn = 0
        jin = 1
        for sn in strn:
            sumn += int(sn)
            jin *= int(sn)
        return jin - sumn


n = 234
ss = Solution()
print(ss.subtractProductAndSum(n))