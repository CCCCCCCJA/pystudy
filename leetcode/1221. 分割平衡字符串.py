class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        L = 0
        R = 0
        count = 0
        for i in range(len(s)):
            if s[i] == "L":
                L += 1
            else:
                R += 1
            if R == L:
                count += 1
                L = 0
                R = 0
        print(count)
        return count




s = "RLRRRLLRLL"
ss = Solution()
ss.balancedStringSplit(s)
