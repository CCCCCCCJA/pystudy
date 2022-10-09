class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = nums1 + nums2
        nums.sort()
        len_nums = len(nums)
        if len_nums % 2 == 0:
            tag = int(len(nums)/2)
            res = (nums[tag] + nums[tag-1])/2
            print(res)
        else:
            tag = int(len(nums) / 2)
            res = nums[tag]
            print(res)
        # print(nums)
        return res
nums1 = [1,2]
nums2 = [3,4]

ss = Solution()
ss.findMedianSortedArrays(nums1, nums2)