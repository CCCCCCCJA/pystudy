class Solution(object):
    def reformat(self, s):
        numlist = []
        zimulist = []
        res = []
        for ss in s:
            if ord(ss) >= ord('a') and ord(ss) <= ord('z'):
                zimulist.append(ss)
            else:
                numlist.append(ss)
        lenn = len(numlist)
        lenz = len(zimulist)
        if abs(lenz-lenn) <= 1:
            tag = 0
            i = 0
            j = 0
            if lenn > lenz:
                while tag < len(s):
                    if tag % 2 == 0:
                        res.append(numlist[i])
                        i += 1
                    else:
                        res.append(zimulist[j])
                        j += 1
                    tag += 1
                return ''.join(res)
            else:
                while tag < len(s):
                    if tag % 2 == 0:
                        res.append(zimulist[i])
                        i += 1
                    else:
                        res.append(numlist[j])
                        j += 1
                    tag += 1
                return ''.join(res)
        else:
            return ''

s = "covid2019"
ss = Solution()
print(ss.reformat(s))
