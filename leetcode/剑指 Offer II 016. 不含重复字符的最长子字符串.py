class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = []
        count = 0
        if(len(s) == 0): return 0
        if(len(s) == 1): return 1
        for j in range(1, len(s)):
            for i in range(j, len(s)):
                if s[i] not in s[j-1:i]:
                    count += 1
                    continue
                else:
                    break
            res.append(count+1)
            # print(count)
            count = 0
        if len(res)>0:
            return max(res)
        else:
            return 0

s = "dvdf"
ss = Solution()
print(ss.lengthOfLongestSubstring(s))