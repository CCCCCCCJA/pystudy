class Solution(object):
    def validIPAddress(self, queryIP):
        """
        :type queryIP: str
        :rtype: str
        """
        iplist1 = queryIP.split('.')
        iplist2 = queryIP.split(':')
        if len(iplist1) > 1:
            iplist = iplist1
        else:
            iplist = iplist2
        print(iplist)
        if len(iplist) != 4 and len(iplist) != 8:
            return 'Neither'
        if len(iplist) == 4:
            for il in iplist:
                if il[0] == '0' and len(il) != 1:
                    return 'Neither'
                for ss in il:
                    if ord(ss) < ord('0') or ord(ss) > ord('9'):
                        return 'Neither'
                if il == '':
                    return 'Neither'
                intil = int(il)
                if intil >= 0 and intil <= 255:
                    if intil == 0 and len(il) != 1:
                        return 'Neither'
                    continue
                else:
                    return 'Neither'
            return "IPv4"
        else:
            for i in range(len(iplist)):
                if i != 0 and iplist[i] == '':
                    return 'Neither'
                if len(iplist[i]) > 4:
                    return 'Neither'
                for j in range(len(iplist[i])):
                    if (ord(iplist[i][j]) > ord('f') and ord(iplist[i][j]) <= ord('z')) \
                        or (ord(iplist[i][j]) > ord('F') and ord(iplist[i][j]) <= ord('Z')):
                        return 'Neither'
            return "IPv6"


queryIP = "192.0.0.1"
ss = Solution()
print(ss.validIPAddress(queryIP))