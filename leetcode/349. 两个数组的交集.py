class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        mixres = []
        a = len(nums1)
        b = len(nums2)
        if a < b:
            for i in range(a):
                if nums1[i] in nums2 and nums1[i] not in mixres:
                    mixres.append(nums1[i])
        else:
            for i in range(b):
                if nums2[i] in nums1 and nums2[i] not in mixres:
                    mixres.append(nums2[i])
        print(mixres)
        return mixres



nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
ss = Solution()
ss.intersection(nums1, nums2)