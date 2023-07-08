class Solution(object):
    def numMatchingSubseq(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: int
        """
        count = 0
        for i in range(len(words)):
            if words[i] in s:
                count += 1
            else:
                index = 0
                for ss in s:
                    if index > len(words[i])-1:
                        count += 1
                        break
                    if ss == words[i][index]:
                        if index == len(words[i])-1:
                            count += 1
                            break
                        index += 1

        print(count)
        return count

s = "dsahjpjauf"
words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
ss = Solution()
ss.numMatchingSubseq(s, words)