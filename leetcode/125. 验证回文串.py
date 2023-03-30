class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        res = ''
        for i in range(len(s)):
            if (ord(s[i]) >= 65 and ord(s[i]) <=90) or (ord(s[i]) >= 97 and ord(s[i]) <= 122) or (ord(s[i]) >= 48 and ord(s[i]) <= 57):
                if (ord(s[i]) >= 65 and ord(s[i]) <=90):
                    res += chr(ord(s[i]) + 32)
                else:
                    res += s[i]
        return res == res[::-1]

s = "0P"
ss = Solution()
print(ss.isPalindrome(s))