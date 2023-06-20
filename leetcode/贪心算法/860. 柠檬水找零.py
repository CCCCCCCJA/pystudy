class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        moneydict = dict()
        moneydict['5'] = 0
        moneydict['10'] = 0
        for i in range(len(bills)):
            if bills[i] == 5:
                moneydict['5'] += 1
            elif bills[i] == 10:
                if moneydict['5'] != 0:
                    moneydict['10'] += 1
                    moneydict['5'] -= 1
                else:
                    return False
            else:
                if moneydict['10'] != 0 and moneydict['5'] != 0:
                    moneydict['10'] -= 1
                    moneydict['5'] -= 1
                elif moneydict['5'] >= 3:
                    moneydict['5'] -= 3
                else:
                    return False
        return True

bills = [5,5,10,10,20]
ss = Solution()
print(ss.lemonadeChange(bills))