class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        print(s)
        tmp = ''
        i = 0
        j = len(s) - 1
        while i < j:
            if ((ord(s[i]) >= ord('a') and ord(s[i]) <= ord('z')) or (ord(s[i]) >= ord('0') and ord(s[i]) <= ord('9'))) and\
                    ((ord(s[j]) >= ord('a') and ord(s[j]) <= ord('z')) or (ord(s[j]) >= ord('0') and ord(s[j]) <= ord('9'))):
                i += 1
                j -= 1
                continue
            if ((ord(s[i]) <= ord('a') and ord(s[i]) >= ord('z')) or (ord(s[i]) >= ord('0') and ord(s[i]) <= ord('9')))


s = "race a car"
ss = Solution()
print(ss.isPalindrome(s))