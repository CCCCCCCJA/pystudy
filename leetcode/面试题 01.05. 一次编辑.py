class Solution(object):
    def oneEditAway(self, first, second):
        lenf = len(first)
        lens = len(second)
        listf = list(first)
        lists = list(second)
        print(lenf, lens)
        if abs(lens - lenf) > 1:
            return False
        if lenf > lens:
            for i in range(lenf):
                if i == lenf - 1:
                    lists.append(listf[i])
                    break
                if listf[i] != lists[i]:
                    lists.insert(i, listf[i])
                    break
            strs = ''.join(lists)
            if strs == first:
                return True
            else:
                return False
        if lenf < lens:
            for j in range(lens):
                if j == lens - 1:
                    listf.append(lists[j])
                    break
                if listf[j] != lists[j]:
                    listf.insert(j, lists[j])
                    break
            strf = ''.join(listf)
            if strf == second:
                return True
            else:
                return False
        if lenf == lens:
            for k in range(lenf):
                if listf[k] != lists[k]:
                    lists[k] = listf[k]
                    break
            strs = ''.join(lists)
            if strs == first:
                return True
            else:
                return False
first = "pale"
second = "ple"
ss = Solution()
print(ss.oneEditAway(first, second))