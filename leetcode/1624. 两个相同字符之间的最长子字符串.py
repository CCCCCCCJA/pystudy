class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        """
        :type s: str
        :rtype: int
        """
        set_s = set(s)
        print(set_s)
        
s = 'abca'
ss = Solution()
ss.maxLengthBetweenEqualCharacters(s)