class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        len_nums = len(nums)
        sets = set(nums)
        len_sets = len(sets)
        if len_nums == len_sets:
            return False
        else:
            return True
