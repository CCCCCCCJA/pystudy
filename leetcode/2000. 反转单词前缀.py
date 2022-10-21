class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        if ch in word:
            index = word.index(ch)
        else:
            return word
        # print(index)
        w1 = word[:index+1]
        w2 = word[index+1:]
        w1 = w1[::-1]
        # print(w1+w2)
        return w1 + w2

word = "abcdefd"
ch = "d"
ss = Solution()
ss.reversePrefix(word, ch)