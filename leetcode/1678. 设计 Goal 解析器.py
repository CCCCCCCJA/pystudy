class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        command = command.replace('G', "G").replace('()', "o").replace('(al)', "al")
        print(command)
        return command


command = "(al)G(al)()()G"
ss = Solution()
ss.interpret(command)