class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        list_s = list(s)
        set_s = set(list_s)
        count = []
        con = 0
        for s in set_s:
            count.append(list_s.count(s))
        for c in count:
            if c % 2 == 1:
                con += 1
        return (con == 1) | (con == 0)
s = "tactcoa"
ss = Solution()
print(ss.canPermutePalindrome(s))
