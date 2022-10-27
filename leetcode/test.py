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
# 交换两个值
def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp
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

# 堆排序
def heapify(arr, index, heapsize):
    left = index * 2 + 1
    while left < heapsize:
        if (left + 1 < heapsize) & (arr[left+1] > arr[left]):
            largest = left + 1
        else:
            largest = left

        if arr[largest] <= arr[index]:
            largest = index

        if largest == index: break
        swap(arr, largest, index)
        index = largest
        left = index * 2 + 1

def heapinsert(arr, index):
    while arr[index] > arr[int((index-1) / 2)]:
        swap(arr, index, int((index-1) / 2))
        index = int((index-1) / 2)

def heapsort(arr):
    if (arr == None) | (len(arr) < 2):
        return
    # for i in range(len(arr)):
    #     heapinsert(arr, i) # logN
    # 更好的方法
    for i in reversed(range(len(arr))):
        heapify(arr, i, len(arr))
    print(arr)
    print('---')
    heapsize = len(arr) - 1
    swap(arr, 0, heapsize)
    while heapsize > 0:
        heapify(arr, 0, heapsize)
        heapsize -= 1
        swap(arr, 0, heapsize)
        print(arr)

#
# arr = [3,5,9,4,6,7,0]
# heapsort(arr)
# print('---')
# print(arr.sort())



# 树的最大宽度
import queue
import math
# class Node(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def w(head):
#     if head == None:
#         return
#     q = queue.Queue(maxsize=100)
#     q.put(head)
#     level = {}
#     level[head] = 1
#     curlevel = 1
#     curlevelnodes = 0
#     maxnum = -100000
#     while q.empty() != True:
#         cur = q.get()
#         curnodelevel = level.get(cur)
#         if curnodelevel == curlevel:
#             curlevelnodes += 1
#         else:
#             maxnum = max(maxnum, curlevelnodes)
#             curlevel += 1
#             curlevelnodes = 0
#
#         if cur.left != None:
#             level[cur.left] = curnodelevel + 1
#             q.put(cur.left)
#         if cur.right != None:

# hash
# import random
# class Pool(object):
#     keyIndexDict = {}
#     indexKeyDict = {}
#     size = 0
#     def insert(self, key):
#         if key not in self.keyIndexDict:
#             self.keyIndexDict[key] = self.size
#             self.indexKeyDict[self.size] = key
#             self.size += 1
#     def getRandom(self):
#         if self.size == 0:
#             return None
#         randomIndex = int(random.random() * self.size)
#         return self.indexKeyDict[randomIndex]
#     def delete(self, key):
#         if key in self.keyIndexDict:
#             deleteIndex = self.keyIndexDict[key]
#             self.size -= 1
#             lastIndex = self.size
#             lastK = self.indexKeyDict[lastIndex]
#             self.keyIndexDict[lastK] = deleteIndex
#             self.indexKeyDict[deleteIndex] = lastK
#             self.keyIndexDict.pop(key)
#             self.indexKeyDict.pop(lastIndex)
#     def printDict(self):
#         print(self.keyIndexDict, self.indexKeyDict)
# ss = Pool()
# ss.insert("A")
# ss.insert("B")
# ss.insert("C")
# ss.insert("D")
# ss.insert("E")
# ss.printDict()
# ss.delete('E')
# ss.printDict()

# 布隆过滤器
# n = 样本量  p = 失误率
# m = - (n * lnp)/(ln2) ** 2
# k = ln2 * (m / n) 约等于 0.7 * (m / n)  个哈希函数
# p真 = 1 - e ** ((n * k真) / m真)

# s = '01101110'
# print(s[5:10])

# 回文串
def manacherString(s):
    chararr = s
    res = []
    index = 0
    for i in range(len(s)*2+1):
        if i & 1 == 0:
            res.append('#')
        else:
            res.append(chararr[index])
            index += 1
    print(res)
    return res

def maxLcapsLength(s):
    if (s==None) | (len(s) == 0):
        return 0
    str = manacherString(s) # 将#字符加入需判断的字符串中
    pArr = [] # 回文半径数组
    C = -1 # 中心
    R = -1 # 回文右边界的再往右的一个位置 最右的有效区为R-1
    max111 = -10**9 # 扩出来的最大值
    for i in range(len(str)): # 每个位置都求会问半径
        # i至少
        if R > i:
            pArr.append(min(2*C-i, R-i) ) # 不用验的区域
        else:
            pArr.append(1)
        while (i + pArr[i] < len(str)) & (i - pArr[i] > -1):
            if str[i+pArr[i]] == str[i-pArr[i]]:
                pArr[i] += 1
            else:
                break
        if i + pArr[i] > R:
            R = i + pArr[i]
            C = i
        max111 = max(max111, pArr[i])
    return max111 - 1
s = 'abcddcbabcd'
print(maxLcapsLength(s))













