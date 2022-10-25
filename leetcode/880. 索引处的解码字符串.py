# 超时！！！
# class Solution(object):
#     def decodeAtIndex(self, s, k):
#         """
#         :type s: str
#         :type k: int
#         :rtype: str
#         """
#         res = ''
#         for ss in s:
#             if len(res) > k:
#                 return res[k-1]
#             tmp = res
#             if (ord(ss) >= 48) & (ord(ss) <= 57):
#                 # for i in range(int(ss)-1):
#                 #     res += tmp
#                 res += tmp * (int(ss)-1)
#             else:
#                 res += ss
#             # print(res)
#         # print(res)
#         return res[k - 1]
class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        while k > 0:
            l = 0
            for i in range(len(s)):
                if s[i].isalpha():
                    l += 1
                    if l == k:
                        return s[i]
                else:
                    if k <= l * int(s[i]):
                        k = (k-1) % l + 1 # ?????????????????????
                        break
                    else:
                        l *= int(s[i])

S = "ha22"
K = 5
ss = Solution()
print(ss.decodeAtIndex(S, K))


