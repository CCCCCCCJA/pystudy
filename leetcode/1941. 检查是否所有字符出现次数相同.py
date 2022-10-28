from collections import Counter


class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        set_s = set(s)
        freq = Counter(s)
        print(freq)
        count = []
        for ss in set_s:
            count.append(s.count(ss))
        if count.count(count[0]) == len(count):
            return True
        else:
            return False


s = "abacbc"
ss = Solution()
print(ss.areOccurrencesEqual(s))