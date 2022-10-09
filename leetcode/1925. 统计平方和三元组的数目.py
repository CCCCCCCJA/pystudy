class Solution(object):
    def countTriples(self, n):
        lists = []
        for i in range(1, n+1):
            lists.append(i)
        count = 0
        for i in range(len(lists)-2):
            for j in range(i+1, len(lists)-1):
                for k in range(j+1, len(lists)):
                    # print(lists[i], lists[j], lists[k])
                    if (lists[i]**2 + lists[j]**2 == lists[k]**2):
                        count +=2

        # print(count)
        return count
n = 10
ss = Solution()
ss.countTriples(n)