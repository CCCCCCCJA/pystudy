class Solution(object):
    def countWords(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: int
        """
        count = 0
        lenw1 = len(words1)
        lenw2 = len(words2)
        if lenw1 >= lenw2:
            for i in range(lenw2):
                if (words1.count(words2[i]) == 1) & (words2.count(words2[i]) == 1):
                    count += 1
        else:
            for i in range(lenw1):
                if (words1.count(words1[i]) == 1) & (words2.count(words1[i]) == 1):
                    count += 1
        print(count)
        return count

words1 = ["leetcode","is","amazing","as","is"]
words2 = ["amazing","leetcode","is"]
ss = Solution()
ss.countWords(words1, words2)