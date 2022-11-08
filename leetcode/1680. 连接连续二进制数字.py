class Solution(object):
    def concatenatedBinary(self, n):
        res = ''
        resnum = 0
        for i in range(1, n+1):
            tmp = bin(i).replace('0b', '')
            res += tmp
        # res = res[::-1]
        # print(res)
        # for i in range(0, len(res)):
        #     if res[i] == '1':
        #         resnum += 2 ** i
        #         resnum = resnum % (10 ** 9 + 7)
        # print(resnum % (10 ** 9 + 7))
        return int(res, 2) % (10 ** 9 + 7)

n = 12
ss = Solution()
print(ss.concatenatedBinary(n))