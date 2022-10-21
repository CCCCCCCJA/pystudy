class Solution(object):
    def percentageLetter(self, s, letter):
        """
        :type s: str
        :type letter: str
        :rtype: int
        """
        len_str = len(s)
        num = s.count(letter)
        return int(num / len_str * 100)

s = "foobar"
letter = "o"
ss = Solution()
print(ss.percentageLetter(s, letter))