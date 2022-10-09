class Solution(object):
	def isPerfectSquare(self, num):
		i = 1
		while(1):
			res = i * i
			i += 1
			if(res == num):
				return True
			elif(res > num):
				return False

