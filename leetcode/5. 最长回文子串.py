class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        tmp = []
        tmp.append('#')
        count = []
        for ss in s:
            tmp.append(ss)
            tmp.append('#')
        print(tmp)
        for i in range(len(tmp)):
            k = i
            m = i
            con = 0
            while 1:
                if (i == 0) | (i == len(tmp)-1):
                    count.append(0)
                    break
                k -= 1
                m += 1
                if (k >= 0) & (m <= len(tmp)-1):
                    if tmp[k] == tmp[m]:
                        con += 1
                    else:
                        count.append(con)
                        break
                else:
                    count.append(con)
                    break
        print(count)
        maxcount = max(count)
        indexmax = count.index(maxcount)
        d = maxcount
        res = tmp[indexmax-d:indexmax+d+1]
        print(res)
        resstr = ''.join(res).replace('#', '')
        print(resstr)
        return resstr
# 有更好的方法





s = "aaaaa"
ss = Solution()
ss.longestPalindrome(s)