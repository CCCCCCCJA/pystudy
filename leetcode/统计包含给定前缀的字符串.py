class Solution(object):
	def prefixCount(self, words, pref):
		count = 0
		pref_len = len(pref)
		for word in words:
			word = word[0:pref_len]
			if(word == pref):
				count = count + 1
		return count

words = ["pay","attention","practice","attend"]
pref = "at"
ss = Solution()
print(ss.prefixCount(words, pref))