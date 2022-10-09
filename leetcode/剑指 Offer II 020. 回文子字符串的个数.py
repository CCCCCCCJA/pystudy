class Solution(object):
    def countSubstrings(self, s):
        len_s = len(s)
        count = 0
        lists = []
        for j in range(len(s)):
            for i in range(j+1, len_s+1):
                res_s = s[j:i]
                print(res_s)
                k = 0
                m = len(res_s) - 1
                while (k <= m):
                    if (res_s[k] == res_s[m]):
                        k += 1
                        m -= 1
                    else:
                        break
                else:
                    count += 1
                    continue
        return count

s = 'aba'
ss = Solution()
print(ss.countSubstrings(s))

# if k > m:
#     if res_s not in lists:
#         lists.append(res_s)
#         count += 1