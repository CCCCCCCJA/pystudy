class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        tmpnum = nums1.copy()
        tmpnum = tmpnum[:m]
        i = 0
        j = 0
        index = 0
        while (i < m) & (j < n):
            if tmpnum[i] == nums2[j]:
                nums1[index] = tmpnum[i]
                i += 1
                index += 1
                continue
            if tmpnum[i] < nums2[j]:
                nums1[index] = tmpnum[i]
                i += 1
                index += 1
                continue
            if tmpnum[i] > nums2[j]:
                nums1[index] = nums2[j]
                j += 1
                index += 1
        print(nums1)
        print(i, j)
        if j == n:
            tmp = tmpnum[i:len(tmpnum)]
            print(tmp)
            for tn in tmp:
                nums1[index] = tn
                index += 1
        if i == m:
            tmp = nums2[j:len(nums2)]
            print(tmp)
            for tn in tmp:
                nums1[index] = tn
                index += 1
        print(nums1)
        return nums1
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
ss = Solution()
print(ss.merge(nums1, m, nums2, n))