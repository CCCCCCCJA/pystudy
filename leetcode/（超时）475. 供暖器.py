# class Solution(object):
#     def findRadius(self, houses, heaters):
#         """
#         :type houses: List[int]
#         :type heaters: List[int]
#         :rtype: int
#         """
#         tag = []
#         max1 = max(houses)
#         max2 = max(heaters)
#         for i in range(max(max1, max2)):
#             tag.append(0)
#         r = 0
#         tip = 0
#         while 1:
#             tip = 0
#             for h in heaters:
#                 h = h - 1
#                 tag[h] = 1
#                 for rr in range(r):
#                     if (h - (rr + 1)) >= 0:
#                         tag[h - (rr + 1)] = 1
#                     if (h + rr + 1) <= max(houses) - 1:
#                         tag[h + rr + 1] = 1
#             print(tag)
#             for hs in houses:
#                 if tag[hs - 1] != 1:
#                     r += 1
#                     break
#                 else:
#                     tip += 1
#             if tip == len(houses):
#                 return r


houses = [1]
heaters = [1, 2, 3, 4]
ss = Solution()
print(ss.findRadius(houses, heaters))
