class Solution(object):
	def mergeSimilarItems(self, items1, items2):
		list = []
		tag = 0
		for i1 in items1:
			for i2 in items2:
				if(i1[0] == i2[0]):
					i1[1] = i1[1] + i2[1]
					list.append(i1)
					break
		for i1 in items1:
			for i in list:
				if(i1[0] == i[0]):
					tag = 1
			if(tag != 1):
				list.append(i1)
			tag = 0
		for i2 in items2:
			for i in list:
				if(i2[0] == i[0]):
					tag = 1
			if(tag != 1):
				list.append(i2)
			tag = 0
		list.sort()
		return list

items1 = [[1,1],[3,2],[2,3]]

items2 = [[2,1],[3,2],[1,3]]
ss = Solution()
print(ss.mergeSimilarItems(items1, items2))