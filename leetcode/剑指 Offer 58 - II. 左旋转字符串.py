# class Solution(object):
#     def reverseLeftWords(self, s, n):
#         """
#         :type s: str
#         :type n: int
#         :rtype: str
#         """
#         tmps = s[0:n]
#         tmptmp = s[n:]
#         return tmptmp+tmps




# 更好的操作
class Solution:
    def reverseLeftWords(self, s, n):
        res = []
        for i in range(n, n + len(s)):
            res.append(s[i % len(s)]) # 取余骚操作
        return ''.join(res)


