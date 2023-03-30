class Solution(object):
    def commonFactors(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        count = 0
        for i in range(1, min(a, b)+1):
            if a % i == 0 and b % i == 0:
                count += 1
        return count