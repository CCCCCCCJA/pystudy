class Solution(object):
    def reformatDate(self, date):
        """
        :type date: str
        :rtype: str
        """
        datelist = date.split(' ')
        res = ''
        month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        for i in range(len(datelist)):
            if i == 0:
                if len(datelist[0]) == 3:
                    res = '-' + '0' + datelist[0][0:1] + res
                else:
                    res = '-' +  datelist[0][0:2] + res
            elif i == 1:
                num = month.index(datelist[1]) + 1
                if num < 10:
                    strn = '0' + str(num)
                else:
                    strn = str(num)
                res = '-' + strn + res
            else:
                res = datelist[2] + res
        print(res)
        return res

date = "20th Oct 2052"
ss = Solution()
ss.reformatDate(date)