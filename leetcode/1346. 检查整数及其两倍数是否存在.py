class Solution(object):
    def checkIfExist(self, arr):
        # """
        # :type arr: List[int]
        # :rtype: bool
        # """
        # 执行用时：32 ms  在所有 Python 提交中击败了28.79%的用户
        # 内存消耗 13.2 MB 在所有 Python 提交中击败了6.06%的用户
        # for i in range(len(arr)-1):
        #     for j in range(i+1, len(arr)):
        #         if (arr[i] == arr[j] + arr[j]) | (arr[j] == arr[i] + arr[i]):
        #             # print(arr[i], arr[j])
        #             return True
        # return False
        # 执行用时：20 ms, 在所有 Python 提交中击败了90.91%的用户
        for ss in arr:
            if (ss * 2 in arr) & (ss != 0):
                return True
            if (ss == 0) & (arr.count(0) >= 2):
                return True
        return False




arr = [7,1,14,11]
ss = Solution()
print(ss.checkIfExist(arr))