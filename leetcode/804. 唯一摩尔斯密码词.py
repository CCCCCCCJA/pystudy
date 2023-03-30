class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        res = set()
        tag = ord('a')
        wordList = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        for ws in words:
            tmp = ''
            for i in range(len(ws)):
                flag = ord(ws[i]) - tag
                tmp += wordList[flag]
            res.add(tmp)
        return len(res)



words = ["gin", "zen", "gig", "msg"]
ss = Solution()
print(ss.uniqueMorseRepresentations(words))
