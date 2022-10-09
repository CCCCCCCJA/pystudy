class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """

        return address.replace('.', '[.]')

address = "1.1.1.1"
ss = Solution()
print(ss.defangIPaddr(address))