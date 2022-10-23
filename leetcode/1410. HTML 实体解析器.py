class Solution(object):
    def entityParser(self, text):
        text = text.replace('&quot;', '"').replace('&apos;', "'").replace('&amp;', '&').replace('&gt;', '>').replace('&lt;', '<').replace('&frasl;', '/')
        print(text)
        return text



text = "and I quote: &quot;...&quot;"
ss = Solution()
ss.entityParser(text)