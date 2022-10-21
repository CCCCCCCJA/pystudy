class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        tmp = text.split(' ')
        len_len = len(tmp)
        print(tmp)
        count = 0
        for t in tmp:
            for s in brokenLetters:
                if s in t:
                    count += 1
                    break
        print(count)
        return len_len - count

text = "leet code"

brokenLetters = "lt"
ss = Solution()
ss.canBeTypedWords(text, brokenLetters)