class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        tmplist = list(haystack)
        if needle in haystack:
            while 1:
                resindex = tmplist.index(needle[0])
                tmp = haystack[resindex:resindex+len(needle)]
                if tmp == needle:
                    # print(resindex)
                    return resindex
                tmplist[resindex] = '#'
        else:
            return -1