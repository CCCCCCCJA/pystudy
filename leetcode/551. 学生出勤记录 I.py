class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s.count('P') < 2 or 'LLL' in s:
            return False
        else:
            return True