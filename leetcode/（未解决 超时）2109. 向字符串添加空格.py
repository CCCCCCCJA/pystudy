# 超时  超时


class Solution(object):
    def addSpaces(self, s, spaces):
#         """
#         :type s: str
#         :type spaces: List[int]
#         :rtype: str
#         """
#         res = ''
#         tag = 0
#         for i in range(len(spaces) + 1):
#             if i != len(spaces):
#                 res += s[tag:spaces[i]] + " "
#                 tag = spaces[i]
#             else:
#                 res += s[tag:]
#         print(res)
#         return res
        ans = ""
        spaces = [0] + spaces + [len(s)]  # 加上开始和结尾的下标
        for i in range(1, len(spaces)):
            ans += f"{s[spaces[i - 1]:spaces[i]]} "  # 注意最后面有个空格～
        return ans[:-1]  # 最后会多出一个空格， 不取


s = "icodeinpython"
spaces = [1,5,7,9]
ss = Solution()
ss.addSpaces(s, spaces)