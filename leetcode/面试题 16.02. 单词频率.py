from collections import Counter
class WordsFrequency(object):
    # bookbook = []
    def __init__(self, book):
        self.bookbook = Counter(book)
    def get(self, word):
        return self.bookbook[word]



# Your WordsFrequency object will be instantiated and called as such:
# obj = WordsFrequency(book)
# param_1 = obj.get(word)