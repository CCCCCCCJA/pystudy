class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        res = 0
        while word * (res + 1) in sequence:
            res += 1
        return res



sequence = "ababc"
word = "ab"

ss = Solution()
print(ss.maxRepeating(sequence, word))