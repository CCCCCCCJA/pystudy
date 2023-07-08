class Solution(object):
    def lastSubstring(self, s):
        maxstr = s[0]
        for ss in s:
            if ss > maxstr:
                maxstr = ss
        lists = list(s)
        indexmaxstr = []
        for i in range(lists.count(maxstr)):
            index = lists.index(maxstr)
            indexmaxstr.append(index)
            lists[index] = '#'
        resstr = []
        tmp = s[indexmaxstr[0]:]
        for j in range(1, len(indexmaxstr)):
            if tmp < s[indexmaxstr[j]:]:
                tmp = s[indexmaxstr[j]:]
        print(tmp)
        return tmp

s = "sfsafdsfamsdasafasfasdnjasndnasndinaisdoamcsmcmnsfo"
ss = Solution()
ss.lastSubstring(s)