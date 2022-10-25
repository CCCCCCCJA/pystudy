class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        tmp = []
        cha = []
        res = []
        for i in range(len(arr)-1):
            for j in range(i+1, len(arr)):
                if arr[i] < arr[j]:
                   tmp.append([arr[i], arr[j]])
                   cha.append(arr[j] - arr[i])
                else:
                    tmp.append([arr[j], arr[i]])
                    cha.append(arr[i] - arr[j])
        print(tmp, cha)
        min_cha = min(cha)
        count_cha = cha.count(min_cha)
        for i in range(count_cha):
            index_cha = cha.index(min_cha)
            res.append(tmp[index_cha])
            cha[index_cha] = 10**6+1
        res = res.sort()
        print(res)
        return res


arr = [4,2,1,3]
ss = Solution()
ss.minimumAbsDifference(arr)