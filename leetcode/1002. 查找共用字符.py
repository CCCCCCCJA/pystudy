class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        res = []
        tag = 0
        for ws in words[0]:
            for i in range(1, len(words)):
                if ws in words[i]:
                    tag += 1
                    words[i] = words[i].replace(ws, '-', 1)
                else:
                    tag = 0
                    break
            if tag == len(words) - 1:
                res.append(ws)
                tag = 0
        print(words)
        return res



words = ["cool","lock","cook"]
ss = Solution()
ss.commonChars(words)
