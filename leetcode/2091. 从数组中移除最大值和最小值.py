class Solution(object):
    def minimumDeletions(self, nums):
        len_nums = len(nums)
        min_num = min(nums)
        max_num = max(nums)
        index_min = nums.index(min_num)
        index_max = nums.index(max_num)
        test = int(len_nums/2)
        if (index_min <= int(len_nums/2)) & (index_max <= int(len_nums/2)):
            if index_min > index_max:
                return index_min + 1
            else:
                return index_max + 1
        if (index_min >= int(len_nums/2)) & (index_max >= int(len_nums/2)):
            if index_min < index_max:
                return len_nums - index_min
            else:
                return len_nums - index_max
        if (index_min <= int(len_nums/2)) & (index_max >= int(len_nums/2)):
            if (len_nums - index_max + index_min + 1) > index_max:
                return index_max + 1
            else:
                return len_nums - index_max + index_min + 1
        if (index_min >= int(len_nums / 2)) & (index_max <= int(len_nums / 2)):
            if index_max == int(len_nums / 2): return len_nums - index_max
            if (index_max + len_nums - index_min + 1) > index_min:
                return index_min + 1
            else:
                return index_max + len_nums - index_min + 1


nums = [72956,-44432,78333,31358,-96449,-24776]
ss = Solution()
print(ss.minimumDeletions(nums))