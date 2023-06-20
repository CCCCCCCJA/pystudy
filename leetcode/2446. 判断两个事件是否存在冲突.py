class Solution(object):
    def haveConflict(self, event1, event2):
        """
        :type event1: List[str]
        :type event2: List[str]
        :rtype: bool
        """
        tmp1 = event1[0]
        tmp2 = event1[1]
        startmin1 = int(tmp1[0:2]) * 60 + int(tmp1[3:])
        endmin1 = int(tmp2[0:2]) * 60 + int(tmp2[3:])
        print(startmin1, endmin1)
        tmp3 = event2[0]
        tmp4 = event2[1]
        startmin2 = int(tmp3[0:2]) * 60 + int(tmp3[3:])
        endmin2 = int(tmp4[0:2]) * 60 + int(tmp4[3:])
        print(startmin2, endmin2)
        if (startmin2 >= startmin1 and startmin2 <= endmin1) or (endmin2 >= startmin1 and endmin2 <= endmin1)\
                or (startmin2 <=startmin1 and endmin2 >= endmin1):
            return True
        else:
            return False


event1 = ["01:15", "02:00"]
event2 = ["02:00", "03:00"]
ss = Solution()
ss.haveConflict(event1, event2)