class Solution(object):
    def waysToBuyPensPencils(self, total, cost1, cost2):
        """
        :type total: int
        :type cost1: int
        :type cost2: int
        :rtype: int
        """
        gang_nums = int(total / cost1)
        pan_nums = int(total / cost2)
        count = 0
        # print(gang_nums, pan_nums)
        for i in range(0, gang_nums+1):
            for j in range(0, pan_nums+1):
                if (i * cost1 + j * cost2) <= total:
                    count += 1
        print(count)
        return count
total = 20
cost1 = 10
cost2 = 5
ss = Solution()
ss.waysToBuyPensPencils(total, cost1, cost2)