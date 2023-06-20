class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        i = 0
        j = len(s) - 1
        s = list(s)
        while i < j:
            if s[i].isalpha() and s[j].isalpha():
                tmp = s[i]
                s[i] = s[j]
                s[j] = tmp
                i += 1
                j -= 1
            elif not s[i].isalpha() and not s[j].isalpha():
                i += 1
                j -= 1
                print(s[i], s[j])
            else:
                if not s[i].isalpha():
                    i += 1
                else:
                    j -= 1
        print(s)
        return ''.join(s)





s = "a-bC-dEf-ghIj"
ss = Solution()
print(ss.reverseOnlyLetters(s))