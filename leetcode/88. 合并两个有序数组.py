class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        num = []
        i = 0
        j = 0
        while (i < m) & (j < n):
            if nums1[i] == 0 | nums2[j] == 0:
                continue
            if nums1[i] <= nums2[j]:
                num.append(nums1[i])
                i += 1
            else:
                num.append(nums2[j])
                j += 1

        print(i, j)
        if i >= m:
            for k in range(j, n):
                num.append(nums2[k])
        if j >= n:
            for k in range(i, m):
                num.append(nums1[k])
        print(nums1)
        for o in range(len(num)):
            nums1[o] = num[o]
        print(nums1)
        return nums1
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
ss = Solution()
print(ss.merge(nums1, m, nums2, n))