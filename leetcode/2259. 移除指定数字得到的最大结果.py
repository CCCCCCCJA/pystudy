class Solution(object):
    def removeDigit(self, number, digit):
        count = []
        tmp = list(number)
        for i in range(number.count(digit)):
            indexn = tmp.index(digit)
            count.append(indexn)
            tmp[indexn] = '#'
        # print(count)
        res = []
        for cn in count:
            tmp = list(number)
            tmp.pop(cn)
            tmptmp = ''.join(tmp)
            res.append(int(tmptmp))
        # print(res)
        return str(max(res))