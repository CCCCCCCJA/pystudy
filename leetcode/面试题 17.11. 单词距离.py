class Solution(object):
    def findClosest(self, words, word1, word2):
        index1 = []
        index2 = []
        for i in range(len(words)):
            if words[i] == word1:
                index1.append(i)
                continue
            if words[i] == word2:
                index2.append(i)
                continue
        minnum = 10 ** 5 + 1
        for i1 in index1:
            for i2 in index2:
                if minnum > abs(i1 - i2):
                    minnum = abs(i1 - i2)
        # print(minnum)
        return minnum


words = ["I","am","a","student","from","a","university","in","a","city"]
word1 = "a"
word2 = "student"
ss = Solution()
ss.findClosest(words, word1, word2)
