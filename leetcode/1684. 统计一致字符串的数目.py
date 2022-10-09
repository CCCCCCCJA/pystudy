class Solution(object):
    def countConsistentStrings(self, allowed, words):
        count = 0
        tag = 0
        for word in words:
            for w in word:
                if w not in allowed:
                    tag = 1
                    break
            if(tag == 0):
                count += 1
            tag = 0
        return count

allowed = "ab"
words = ["ad","bd","aaab","baa","badab"]
ss = Solution()
print(ss.countConsistentStrings(allowed, words))