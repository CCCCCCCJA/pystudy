class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxn = max(nums)
        minn = min(nums)
        indexmax = nums.index(maxn)
        indexmin = nums.index(minn)
        print(maxn, minn, indexmax, indexmin)
        midlle = len(nums) // 2
        if indexmax + 1 == midlle or indexmin + 1 == midlle:
            if indexmax < midlle and indexmin < midlle:
                return midlle
            elif indexmax + 1 > midlle and indexmin + 1 > midlle:
                return
        elif indexmax < midlle and indexmin > midlle:
            return indexmax + 1 + len(nums) - indexmin
        elif indexmax > midlle and indexmin < midlle:
            return indexmin + len(nums) - indexmax



nums = [2,3,7,10,4,1,8,6]
ss = Solution()
print(ss.minimumDeletions(nums))