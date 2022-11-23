class Solution(object):
    def plusOne(self, digits):
        lenlen = len(digits) - 1
        global tag
        if digits[lenlen] + 1 == 10:
            if len(digits) == 0:
                return [1, 0]
            tag = 1
            digits[lenlen] = 0
            lenlen -= 1
        else:
            digits[lenlen] = digits[lenlen] + 1
            tag = 0
            return digits
        while lenlen >= 0:
            if tag == 1:
                if digits[lenlen] + tag == 10:
                    if lenlen == 0:
                        digits[lenlen] = 0
                        digits.insert(0, 1)
                        return digits
                    digits[lenlen] = 0
                    tag = 1
                    lenlen -= 1
                else:
                    digits[lenlen] = digits[lenlen] + tag
                    return digits



digits = [9,9,9]
ss = Solution()
print(ss.plusOne(digits))


