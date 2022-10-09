class Solution(object):
    def makeFancyString(self, s):
        info = list(s)
        a = []
        tag = info[0]
        count = 1
        # for i in range(1, len(info)):
        #     if info[i] == tag:
        #         count += 1
        #     elif count >= 3:
        #         info_info.remove(info[i])
        #     else:
        #         tag = info[i]
        for i in range(1, len(info)):
            if info[i] == tag:
                count += 1
                if count >= 3:
                    a.append(i)
                    count = 1
                    tag = info[i]
            else:
                tag = info[i]
        res = ''

        for i in range(len(info)):
            for j in a:
                if i != j:
                    res += info[i]
        return res

s = "leeetcode"
ss = Solution()
print(ss.makeFancyString(s))