class Solution(object):
    def isAlienSorted(self, words, order):
        for i in range(len(words)-1):
            len1 = len(words[i])
            len2 = len(words[i+1])
            minlen = min(len1, len2)
            count = 0
            for j in range(minlen):
                if order.index(words[i][j]) == order.index(words[i+1][j]):
                    count += 1
                    continue
                elif order.index(words[i][j]) > order.index(words[i+1][j]):
                    return False
                else:
                    break
            if len1 > len2 and count == minlen:
                return False
        return True


words = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
ss = Solution()
print(ss.isAlienSorted(words, order))