class Solution(object):
    def duplicateZeros(self, arr):
        indexL = []
        tmparr = arr.copy()
        lenlen = len(tmparr)
        for i in range(arr.count(0)):
            indexl = tmparr.index(0)
            tmparr[indexl] = '-1'
            indexL.append(indexl)
        # print(indexL)
        for i in range(len(indexL)):
            if indexL[i]+i < lenlen:
                if arr[indexL[i]+i] == 0:
                    arr.pop(-1)
                    arr.insert(indexL[i]+i, 0)
        print(arr)
        # arr = arr[:lenlen]
        return arr


arr = [1,0,2,3,0,4,5,0]
ss = Solution()
print(ss.duplicateZeros(arr))
