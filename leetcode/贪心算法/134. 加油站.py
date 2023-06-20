class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        tmp = []
        for i in range(len(gas)):
            tmp.append(gas[i] - cost[i])
        print(tmp)
        if sum(tmp) < 0:
            return -1
        start = 0
        cursum = tmp[0]
        for i in range(1, len(tmp)):
            cursum += tmp[i]
            if cursum < 0:
                start = i+1
                cursum = 0
        return start

gas = [3,1,1]
cost = [1,2,2]
ss = Solution()
print(ss.canCompleteCircuit(gas, cost))
