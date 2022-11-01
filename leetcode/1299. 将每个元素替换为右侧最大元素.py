class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        for i in range(len(arr)):
            if i == len(arr) - 1:
                arr[i] = -1
                break
            res = max(arr[i+1:])
            arr[i] = res
        print(arr)
        return arr

arr = [17,18,5,4,6,1]
ss = Solution()
ss.replaceElements(arr)