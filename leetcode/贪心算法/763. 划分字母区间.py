class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        hashlist = [0] * 26
        for i in range(len(s)):
            # print(ord(s[i]) - ord('a'), i)
            hashlist[ord(s[i]) - 97] = i
        # print(hashlist)
        res = []
        left = 0
        right = 0
        for i in range(len(s)):
            right = max(right, hashlist[ord(s[i]) - 97])
            if i == right:
                res.append(right - left + 1)
                left = i + 1
        # print(res)
        return res


s = "ababcbacadefegdehijhklij"
print(len(s))
ss = Solution()
ss.partitionLabels(s)