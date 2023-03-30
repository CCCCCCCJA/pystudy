class Solution(object):
    def kthGrammar(self, n, k):
        res = ['0']
        for i in range(1, n):
            tmp = ''
            for j in range(len(res[i-1])):
                if res[i-1][j] == '0':
                    tmp += '01'
                else:
                    tmp += '10'
            res.append(tmp)
        print(res)
        return res[-1][k-1]


n = 30
k = 434991989
ss = Solution()
print(ss.kthGrammar(n, k))