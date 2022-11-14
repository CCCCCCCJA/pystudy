class Solution(object):
    def wordBreak(self, s, wordDict):
        for wd in wordDict:
            while wd in s:
                s = s.replace(wd, '', 1)
        if len(s) == 0:
            return True
        else:
            return False

s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
ss = Solution()
print(ss.wordBreak(s, wordDict))