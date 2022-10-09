class Solution(object):
	def lastStoneWeight(self, stones):
		while(len(stones) > 1):
			stones.sort(reverse=True)
			y = stones[0]
			x = stones[1]
			if(x == y):
				stones.remove(y)
				stones.remove(x)
			else:
				stones.remove(x)
				stones[0] = y-x
			# print(stones)
			# print(x, y)
		if(len(stones) == 1):
			return stones[0]
		else:
			return 0

list = [2,2]
ss = Solution()
print(ss.lastStoneWeight(list))