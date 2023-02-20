class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        res = []
        for a2 in arr2:
            if a2 in arr1:
                count = arr1.count(a2)
                for j in range(count):
                    res.append(a2)
                    arr1.remove(a2)
        arr1.sort()
        res = res + arr1
        return res
