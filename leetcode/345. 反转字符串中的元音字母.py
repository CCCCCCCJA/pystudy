class Solution(object):
    def swap(self, arr, i, j):
        tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 执行用时：44ms
        tmp = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        tmptmp = []
        lists = list(s)
        for i in range(len(s)):
            if s[i] in tmp:
                tmptmp.append(i)
        print(tmptmp)
        i = 0
        j = len(tmptmp) - 1
        while i < j:
            self.swap(lists, tmptmp[i], tmptmp[j])
            i += 1
            j -= 1
        return ''.join(lists)

s = "leetcode"
ss = Solution()
print(ss.reverseVowels(s))