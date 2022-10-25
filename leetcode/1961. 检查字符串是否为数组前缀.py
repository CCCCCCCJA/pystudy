class Solution(object):
    def isPrefixString(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: bool
        """
        tmp = ''
        for word in words:
            tmp += word
            if tmp == s:
                return True
        return False



s = "iloveleetcode"
words = ["i","love","leetcode","apples"]
ss = Solution()
print(ss.isPrefixString(s, words))
