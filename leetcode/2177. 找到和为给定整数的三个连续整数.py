class Solution(object):
    def sumOfThree(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        tmpn = num // 3
        if (tmpn-1) + tmpn + (tmpn+1) == num:
            return [(tmpn-1), tmpn, (tmpn+1)]
        elif (tmpn-1) + tmpn + (tmpn+1) > num:
            tmpn -= 1
            if (tmpn - 1) + tmpn + (tmpn + 1) == num:
                return [(tmpn - 1), tmpn, (tmpn + 1)]
            else:
                return []
        else:
            while 1:
                tmpn += 1
                if (tmpn - 1) + tmpn + (tmpn + 1) == num:
                    return [(tmpn - 1), tmpn, (tmpn + 1)]
                elif (tmpn-1) + tmpn + (tmpn+1) > num:
                    return []
