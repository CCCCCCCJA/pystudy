class Solution(object):
    def countPrefixes(self, words, s):
        lenlen = len(s)
        count = 0
        for i in range(lenlen):
            tmp = s[:i+1]
            if tmp in words:
                count += words.count(tmp)
        print(count)
        return count


words = ["a","a"]
s = "aa"
ss = Solution()
ss.countPrefixes(words, s)