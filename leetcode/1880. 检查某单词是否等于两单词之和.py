class Solution(object):
    def panduan(self, c):
        if c == 'a': return '0'
        elif c == 'b': return '1'
        elif c == 'c': return '2'
        elif c == 'd': return '3'
        elif c == 'e': return '4'
        elif c == 'f': return '5'
        elif c == 'g': return '6'
        elif c == 'h': return '7'
        elif c == 'i': return '8'
        elif c == 'j': return '9'
        elif c == 'k': return '10'
        elif c == 'l': return '11'
        elif c == 'm': return '12'
        elif c == 'n': return '13'
        elif c == 'o': return '14'
        elif c == 'p': return '15'
        elif c == 'q': return '16'
        elif c == 'r': return '17'
        elif c == 's': return '18'
        elif c == 't': return '19'
        elif c == 'u': return '20'
        elif c == 'v': return '21'
        elif c == 'w': return '22'
        elif c == 'x': return '23'
        elif c == 'y': return '24'
        elif c == 'z': return '25'

    def isSumEqual(self, firstWord, secondWord, targetWord):
        """
        :type firstWord: str
        :type secondWord: str
        :type targetWord: str
        :rtype: bool
        """
        res1 = ''
        res2 = ''
        res3 = ''
        for fw in firstWord:
            res1 += self.panduan(fw)
        for sw in secondWord:
            res2 += self.panduan(sw)
        for tw in targetWord:
            res3 += self.panduan(tw)
        res = int(res1) + int(res2)
        res3 = int(res3)
        if res == res3:
            return True
        else:
            return False


firstWord = "acb"
secondWord = "cba"
targetWord = "cdb"
ss = Solution()
print(ss.isSumEqual(firstWord, secondWord, targetWord))
