class Solution(object):
    def mergeAlternately(self, word1, word2):
        len1 = len(word1)
        len2 = len(word2)
        i = 0
        j = 0
        res = ''
        while i < len1 and j < len2:
            res += word1[i] + word2[j]
            i += 1
            j += 1
        if i < len1:
            while i < len1:
                res += word1[i]
                i += 1
        if j < len2:
            while j < len2:
                res += word2[j]
                j += 1
        return res
word1 = "ab"
word2 = "pqrs"
ss = Solution()
ss.mergeAlternately(word1, word2)
