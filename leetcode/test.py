# class Solution:
# 	def firstMissingPositive(self, nums):
# 		n = len(nums)
# 		for i in range(n):
# 			if nums[i] <= 0:
# 				nums[i] = n + 1
#
# 		for i in range(n):
# 			num = abs(nums[i])
# 			if num <= n:
# 				nums[num - 1] = -abs(nums[num - 1])
#
# 		for i in range(n):
# 			if nums[i] > 0:
# 				return i + 1
#
# 		return n + 1
#
# nums = [3,4,-1,1]
# ss = Solution()
# print(ss.firstMissingPositive(nums))
#
# i = 3**0.5
# print(type(i))
# if type(i) == int:
#     print('-')
# else:
#     print('--')

# def printOddTimesNum(arr):
#     eor = 0
#     for i in range(len(arr)):
#         eor ^= arr[i]
#
#     rightOne = eor & (~eor + 1)
#
#     onlyOne = 0
#     for cur in range(len(arr)):
#         if (cur & rightOne) == 0:
#             onlyOne ^= cur
#
#     print(onlyOne, (eor ^ onlyOne))
#
# printOddTimesNum([1,2,1,2,3,4,3,4,5,5,6,6,7,7,8,11])

# 归并
import sys
# sys.setrecursionlimit(4000)
# def process(arr, l, r):
#     # if l == r:
#     #     return 0
#     mid = l + ((r-1) >> 1)
#     return process(arr, l, mid) + \
#         process(arr, mid + 1, r) + \
#         merge(arr, 0, mid, r)
#
# def merge(arr, L, m, r):
#     help = []
#     i = 0
#     p1 = L
#     p2 = m + 1
#     res = 0
#     while (p1 <= m) & (p2 <= r):
#         if arr[p1] < arr[p2]:
#             res += (r - p1 + 1) * arr[p1]
#             help.append(arr[p1])
#             p1 += 1
#             i += 1
#         else:
#             res += 0
#             help.append(arr[p2])
#             p2 += 1
#             i += 1
#
#     while p1 <= m:
#         help.append(arr[p1])
#         p1 += 1
#         i += 1
#     while p2 <= r:
#         help.append(arr[p2])
#         p2 += 1
#         i += 1
#
#     for j in range(len(help)):
#         arr.append(help[j])
#
#     return res
#
# arr = [1, 3]
#
# print(process(arr, 0, len(arr) - 1))

# 快排
# import random
# def swap(arr, i, j):
#     tmp = arr[i]
#     arr[i] = arr[j]
#     arr[j] = tmp
#
# def qsort(arr, L, R):
#     if L < R:
#         swap(arr, L + int(random.random() * (R - L + 1)), R)
#         p = partition(arr, L, R)
#         qsort(arr, L, p[0] - 1)
#         qsort(arr, p[1] + 1, R)
#
# def partition(arr, L, R):
#     less = L - 1
#     more = R
#     while L < more:
#         if arr[L] < arr[R]:
#             less += 1
#             swap(arr, less, L)
#             L += 1
#         elif arr[L] > arr[R]:
#             more = more - 1
#             swap(arr, more, L)
#         else:
#             L += 1
#     swap(arr, more, R)
#     return [less+1, more]
#
# arr = [4,5,6,23,43,2,5,7,3]
# print(arr)
# qsort(arr, 0, len(arr) - 1)
# print(arr)




