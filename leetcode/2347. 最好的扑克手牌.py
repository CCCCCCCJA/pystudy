class Solution(object):
    def bestHand(self, ranks, suits):
        """
        :type ranks: List[int]
        :type suits: List[str]
        :rtype: str
        """
        ranks_num = []
        suits_num = []
        for r in ranks:
            ranks_num.append(ranks.count(r))
        for s in suits:
            suits_num.append(suits.count(s))
        print(ranks_num, suits_num)
        if suits_num.count(suits_num[0]) == len(suits):
            return "Flush"
        if (3 in ranks_num) | (4 in ranks_num) | (5 in ranks_num):
            return "Three of a Kind"
        if 2 in ranks_num:
            return "Pair"
        if ranks_num.count(1) == 5:
            return "High Card"
ranks = [13,2,3,1,9]
suits = ["a","a","a","a","a"]
ss = Solution()
ss.bestHand(ranks, suits)