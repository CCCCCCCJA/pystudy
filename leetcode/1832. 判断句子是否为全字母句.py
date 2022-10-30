class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        for i in range(0, 26):
            if chr(97+i) not in sentence:
                return False
        return True


s = "thequickbrownfoxjumpsoverthelazydog"
ss = Solution()
print(ss.checkIfPangram(s))