from collections import Counter


class Solution(object):
    def maxNumberOfBalloons(self, text):
        dict1 = Counter(text)
        count = 0
        res = []
        s = "balon"
        for ss in s:
            tmp = dict1[ss]
            if ss == 'l' or ss == 'o':
                res.append(tmp//2)
            else:
                res.append(tmp)
        print(res)
        return min(res)


text = "nlaebolko"
ss = Solution()
ss.maxNumberOfBalloons(text)
