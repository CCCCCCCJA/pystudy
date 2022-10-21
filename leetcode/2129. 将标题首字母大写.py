class Solution(object):
    def capitalizeTitle(self, title):
        """
        :type title: str
        :rtype: str
        """
        tmp = title.split(' ')
        for i in range(len(tmp)):
            if len(tmp[i]) <= 2:
                tmp[i] = tmp[i].lower()
            else:
                tmp[i] = tmp[i].lower().capitalize()
        print(tmp)
        return ' '.join(tmp)

title = "First leTTeR of EACH Word"
ss = Solution()
print(ss.capitalizeTitle(title))