class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if s1 == s2:
            return True
        tmp = []
        for i in range(len(s1)):
            if s1[i] == s2[i]:
                continue
            else:
                tmp.append(i)
        len_tmp = len(tmp)
        if (len_tmp > 2) | (len_tmp == 1):
            return False
        if len(tmp) == 2:
            if len(s1) == 2:
                s1 = s1[::-1]
                if s1 == s2:
                    return True
                else:
                    return False
            s1_list = list(s1)
            s2_list = list(s2)
            self.swap(s1_list, tmp[0], tmp[1])
            if s1_list == s2_list:
                return True
            else:
                return False
    def swap(self, arr, i, j):
        tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp
s1 = "attack"
s2 = "defend"
ss = Solution()
print(ss.areAlmostEqual(s1, s2))
