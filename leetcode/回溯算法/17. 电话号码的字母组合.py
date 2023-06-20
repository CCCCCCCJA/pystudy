class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        letterMap = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        path = []
        res = []
        def backstrcaking(digits, index):
            if index == len(digits):
                res.append(''.join(path))
                return
            digit = int(digits[index])
            letter = letterMap[digit]
            for i in range(len(letter)):
                path.append(letter[i])
                backstrcaking(digits, index+1)
                path.pop(-1)
        index = 0
        backstrcaking(digits, index)
        print(res)
        return res




digits = '23'
ss = Solution()
ss.letterCombinations(digits)


