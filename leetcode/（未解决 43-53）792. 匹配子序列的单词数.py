from collections import Counter

# 没有检查相对顺序是否相同。。。。。。。。。。。。。。。。。。。
class Solution(object):
    def numMatchingSubseq(self, s, words):
        dict1 = Counter(s)
        count = 0
        for ws in words:
            tmpdict = Counter(ws)
            tag = 0
            for i in range(len(ws)):
                if ws[i] in dict1:
                    if dict1[ws[i]] >= tmpdict[ws[i]]:
                        continue
                    else:
                        tag += 1
                        break
                else:
                    tag += 1
                    break

            if tag == 0:
                count += 1
        return count


s = "dsahjpjauf"
words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
ss = Solution()
print(ss.numMatchingSubseq(s, words))