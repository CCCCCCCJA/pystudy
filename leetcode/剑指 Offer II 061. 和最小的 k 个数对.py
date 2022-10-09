
# res  中获取索引的时候有些问题
# 待解决


class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        tmp = []
        res = []
        cont_num = []
        res_res = []
        for n1 in nums1:
            for n2 in nums2:
                tmp.append(n1)
                tmp.append(n2)
                cont_num.append(n1 + n2)
                res.append(tmp)
                tmp = []
        temp_num = cont_num.copy()
        print(temp_num)
        print(res)
        if k > len(temp_num):
            k = len(temp_num)
        for i in range(k):
            min_num = min(temp_num)
            index_min = cont_num.index(min_num)
            temp_num.remove(min_num)
            res_res.append(res[index_min])
        return res_res


nums1 = [1,1,2]
nums2 = [1,2,3]
k = 10
ss = Solution()
print(ss.kSmallestPairs(nums1, nums2, k))