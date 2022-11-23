class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """

        st = []
        for c in s:
            if c == '*':
                st.pop()
            else:
                st.append(c)
        return ''.join(st)



s = "leet**cod*e"
ss = Solution()
print(ss.removeStars(s))