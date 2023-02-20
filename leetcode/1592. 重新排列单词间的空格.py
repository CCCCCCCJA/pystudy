class Solution(object):
    def reorderSpaces(self, text):
        """
        :type text: str
        :rtype: str
        """
        listtext = text.split(' ')
        count = text.count(' ')
        countlist = listtext.count('')
        if count == 0:
            return text
        print(count, countlist)
        for i in range(countlist):
            listtext.remove('')
        print(listtext)
        if len(listtext) != 1:
            tmpn = (count//(len(listtext)-1)) * (len(listtext)-1)
            plusk = count - tmpn
            return (' '*(count//(len(listtext)-1))).join(listtext) + (' '*plusk)
        else:
            return listtext[0] + (' '*count)


text = "  this   is  a sentence "
ss = Solution()
print(ss.reorderSpaces(text))