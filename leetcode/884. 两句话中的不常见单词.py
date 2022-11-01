from collections import Counter


class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        # 执行用时：16ms
        lists1 = s1.split(' ')
        lists2 = s2.split(' ')
        dicts1 = Counter(lists1)
        dicts2 = Counter(lists2)
        res = []
        for ls in lists1:
            if dicts1[ls] == 1 and ls not in lists2:
                res.append(ls)
        for ls in lists2:
            if dicts2[ls] == 1 and ls not in lists1:
                res.append(ls)
        print(res)
        return res

s1 = "apple apple"
s2 = "banana"
ss = Solution()
ss.uncommonFromSentences(s1, s2)