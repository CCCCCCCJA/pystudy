class Solution(object):
    def monotoneIncreasingDigits(self, n):
        # 超时
        # if n < 10:
        #     return n
        # for i in reversed(range(n+1)):
        #     tmp = i
        #     tmplist = []
        #     tag = 1
        #     while tmp > 0:
        #         k = tmp % 10
        #         tmplist.append(k)
        #         tmp = tmp // 10
        #     for m in range(len(tmplist)-1):
        #         if tmplist[m] >= tmplist[m+1]:
        #             continue
        #         else:
        #             tag = 0
        #             break
        #     if tag:
        #         return i
        listn = list(str(n))
        for i in range(len(listn)):
            if int(listn[i]) > int(listn[i+1]):
                tmp = i
                while tmp >= 0:
                    if tmp == 0:
                        break
                    if listn[tmp] == listn[tmp-1]:
                        tmp -= 1
                    else:
                        break
                listn[tmp] = str(int(listn[tmp]) - 1)
                for j in range(tmp+1, len(listn)):
                    listn[j] = '9'
                res = ''.join(listn)
                return int(res)

n = 101
ss = Solution()
print(ss.monotoneIncreasingDigits(n))