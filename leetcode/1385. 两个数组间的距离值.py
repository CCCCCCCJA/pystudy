class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        count = 0
        for i in range(len(arr1)):
            tag = 0
            for j in range(len(arr2)):
                if abs(arr1[i] - arr2[j]) <= d:
                    tag += 1
                    break
            if tag == 0:
                count += 1
        return count


arr1 = [4,5,8]
arr2 = [10,9,1,8]
d = 2
ss = Solution()
print(ss.findTheDistanceValue(arr1, arr2, d))