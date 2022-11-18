class Solution(object):
    def findLongestWord(self, s, dictionary):
        tmps = list(s)
        tmp = tmps.copy()
        res = []
        for i in range(len(dictionary)):
            index1 = 0
            index2 = 0
            ddd = dictionary[i]
            while index2 < len(dictionary[i]) and index1 < len(tmps):
                if dictionary[i][index2] == tmps[index1]:
                    index1 += 1
                    index2 += 1
                else:
                    tmps.pop(index1)
            if dictionary[i] == ''.join(tmps[:index2]):
                res.append(dictionary[i])
            tmps = tmp.copy()
        print(res)
        if len(res) == 0:
            return ''
        res.sort()
        count = []
        for i in range(len(res)):
            count.append(len(res[i]))
        print(count)
        maxn = max(count)
        indexmaxn = count.index(maxn)
        print(res[indexmaxn])
        return res[indexmaxn]


s = "okbmfyugqqongobwofraotanviqjraaktmmwyxzdnnwwaqsnvfxwngglybtiqwblprgvbgmolotnppzbovnstxmcmocixresdpojmntcdkyjzgbhhigkiyatrgzayivjyqiopvvdftkbsgwgnidsecvydvltaxxywydawrsseyolixznuyhjolngdsmjhepregixtklanjjggzssrbtmhhpamcfeghgssmrjrpelabojfhkdfvscjwhqxubwrhryqmtkiksljezeembngdjyhgmdzahxvvpkqwvhkqlensuxbrcdctqojqnlogjbpovdsbvurwcoehtmtkwxswrwhszuyesdqspnwqxlmjxrbdqbnbbyxhhlabxrdjxtjgpugojsexmrhrfzryapdzglalqzuzfpxeaemjkyfhpbnmdxjtxnxyjecfsapcjyglmtivnsfalpxzdkylgcixjljaqjwminyaodeekpzzpchhceguzayeul"
dictionary = ["mfuraildmrjhdjtctdxejgdurr"]
ss = Solution()
print(ss.findLongestWord(s, dictionary))