# class Solution(object):
#     def freqAlphabets(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         i = 0
#         res = ''
#         while i < len(s):
#             if i < len(s) - 4:
#                 if (s[i+2] == '#') :
#                     res += self.switchfun(s[i]+s[i+1]+s[i+2])
#                     i += 3
#             else:
#                 res += self.switchfun(s[i])
#                 i += 1
#         print(res)
#
#
#     def switchfun(self, str):
#         if str == '1':
#             return 'a'
#         elif str == '2':
#             return 'b'
#         elif str == '3':
#             return 'c'
#         elif str == '4':
#             return 'd'
#         elif str == '5':
#             return 'e'
#         elif str == '6':
#             return 'f'
#         elif str == '7':
#             return 'g'
#         elif str == '8':
#             return 'h'
#         elif str == '9':
#             return 'i'
#         if str == '10#':
#             return 'j'
#         elif str == '11#':
#             return 'k'
#         elif str == '12#':
#             return 'l'
#         elif str == '13#':
#             return 'm'
#         elif str == '14#':
#             return 'n'
#         elif str == '15#':
#             return 'o'
#         elif str == '16#':
#             return 'p'
#         elif str == '17#':
#             return 'q'
#         elif str == '18#':
#             return 'r'
#         elif str == '19#':
#             return 's'
#         elif str == '20#':
#             return 't'
#         elif str == '21#':
#             return 'u'
#         elif str == '22#':
#             return 'v'
#         elif str == '23#':
#             return 'w'
#         elif str == '24#':
#             return 'x'
#         elif str == '25#':
#             return 'y'
#         elif str == '26#':
#             return 'z'
class Solution:
    def freqAlphabets(self, s: str) -> str:
        def get(st):
            return chr(int(st) + 96)

        i, ans = 0, ""
        while i < len(s):
            if i + 2 < len(s) and s[i + 2] == '#':
                ans += get(s[i : i + 2])
                i += 2
            else:
                ans += get(s[i])
            i += 1
        return ans
s = "10#11#12"
ss = Solution()
ss.freqAlphabets(s)