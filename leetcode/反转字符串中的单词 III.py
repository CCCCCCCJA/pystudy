class Solution(object):
    def reverseWords(self, s):
        lists = s.split(' ')
        resstr = ''
        for i in range(len(lists)):
            lists[i] = lists[i][::-1]
        return ' '.join(lists)