class Solution(object):
    def areNumbersAscending(self, s):
        lists = s.split(' ')
        print(lists)
        tmp = []
        for ls in lists:
            if ord(ls[0]) >= ord('0') and ord(ls[0]) <= ord('9'):
                tmp.append(int(ls))
        for i in range(len(tmp)-1):
            if tmp[i] > tmp[i+1]:
                return False
        return True


s = "1 box has 3 blue 4 red 6 green and 12 yellow marbles"
ss = Solution()
ss.areNumbersAscending(s)