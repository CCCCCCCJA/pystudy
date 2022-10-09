class Solution(object):
	def floodFill(self, image, sr, sc, color):
		res = image[sr][sc]
		if(sr > 0 ):
			if(res == image[sr-1][sc]):
				print()