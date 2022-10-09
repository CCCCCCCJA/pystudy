class Solution:
    def minDeletionSize(self, strs):
        len_len = len(strs[0])
        len_list = len(strs)
        count = 0
        for j in range(len_len):
            tag = strs[0][j]
            for i in range(1, len_list):
                if tag <= strs[i][j]:
                    tag = strs[i][j]
                else:
                    count += 1
                    break
        print(count)
        return count


strs = ["rrjk","furt","guzm"]
for str in strs:
    print(str)
ss = Solution()
ss.minDeletionSize(strs)