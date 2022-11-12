from collections import Counter


class Solution(object):
    def CheckPermutation(self, s1, s2):
        # 执行用时：20ms, 在所有Python提交中击败了38.21 %的用户
        # dict1 = Counter(s1)
        # dict2 = Counter(s2)
        # len1 = len(s1)
        # len2 = len(s2)
        # if len1 != len2:
        #     return False
        # for ss in s1:
        #     if ss not in s2:
        #         return False
        #     else:
        #         if dict1[ss] == dict2[ss]:
        #             continue
        #         else:
        #             return False
        # return True
        # 执行用时：4ms, 在所有Python提交中击败了100.00 %的用户
        lists1 = list(s1)
        lists1.sort()
        lists2 = list(s2)
        lists2.sort()
        s1 = ''.join(lists1)
        s2 = ''.join(lists2)
        if s1 == s2:
            return True
        else:
            return False


s1 = "abb"
s2 = "aab"
ss = Solution()
print(ss.CheckPermutation(s1, s2))
