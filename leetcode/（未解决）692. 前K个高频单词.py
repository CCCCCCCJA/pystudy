from collections import Counter


class Solution(object):
    def topKFrequent(self, words, k):
        wsdict = Counter(words)
        setws = set(words)
        listws = list(setws)
        tmp = []
        for i in range(len(words)):
            tmp.append('#')
        count = []
        res = []
        for sws in setws:
            count.append(wsdict[sws])
        print(listws)
        print(count)
        for i in range(k):
            maxn = max(count)
            indexmax = count.index(maxn)
            count[indexmax] = -1
            res.append(listws[indexmax])
        print(res)
        for rs in res:
            indexres = words.index(rs)
            tmp[indexres] = rs
        print(tmp)
        resres = []
        for ts in tmp:
            if ts != '#':
                resres.append(ts)
        print(resres)
        return resres



words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 2
ss = Solution()
ss.topKFrequent(words, k)