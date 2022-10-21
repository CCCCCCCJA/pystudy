class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_list = s.split(' ')
        count = []
        res = []
        print(s_list)
        for s in s_list:
            str1 = s[len(s)-1:]
            count.append(int(str1))
        i = 0
        while i < len(count):
            max_con = min(count)
            index_con = count.index(max_con)
            res_str = s_list[index_con]
            res_str = res_str[:len(res_str)-1]
            res.append(res_str)
            count[index_con] = 1000000
            i += 1
        return ' '.join(res)


s = "is2 sentence4 This1 a3"
ss = Solution()
print(ss.sortSentence(s))