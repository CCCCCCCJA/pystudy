# class Solution(object):
#     def replaceWords(self, dictionary, sentence):
#         """
#         :type dictionary: List[str]
#         :type sentence: str
#         :rtype: str
#         """
#         tmp = sentence.split(' ')
#         print(tmp)
#         for i in range(len(tmp)):
#             for j in range(len(dictionary)):
#                 if dictionary[j] in tmp[i]:
#                     tmp[i] = dictionary[j]
#                     break
#         # print(tmp)
#         res_str = ''
#         for i in range(len(tmp)):
#             if i == len(tmp) - 1:
#                 res_str += tmp[i]
#             else:
#                 res_str += tmp[i] + ' '
#         # print(res_str)
#         return res_str


class Solution:
    def replaceWords(self, dictionary, sentence):
        dictionarySet = set(dictionary)
        words = sentence.split(' ')
        for i, word in enumerate(words):
            for j in range(1, len(words) + 1):
                if word[:j] in dictionarySet:
                    words[i] = word[:j]
                    break
        return ' '.join(words)

dictionary = ["cat","bat","rat"]
sentence = "the cattle was rattled by the battery"
ss = Solution()
print(ss.replaceWords(dictionary, sentence))
