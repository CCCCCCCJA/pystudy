class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        ss = s.split(' ')
        count = ss.count('')
        for i in range(count):
            ss.remove('')
        print(ss)
        return ' '.join(ss[::-1])


s = "  hello world!  "
ss = Solution()
ss.reverseWords(s)