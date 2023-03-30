import collections
class Solution:
    def firstUniqChar(self, s: str) -> str:
        frequency = collections.Counter(s)
        for i, ch in enumerate(s):
            if frequency[ch] == 1:
                return ch
        return ' '


s = "abaccdeff"
ss = Solution()
print(ss.firstUniqChar(s))