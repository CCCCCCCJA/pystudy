class Solution(object):
    def isValid(self, s):
        stack = []
        if len(s) % 2 != 0 or len(s) == 0:
            return False
        for ss in s:
            if ss == '(' or ss == '{' or ss == '[':
                stack.append(ss)
            else:
                if len(stack) == 0:
                    return False
                tmp = stack[-1]
                if ss == ')' and tmp == '(':
                    stack.pop(-1)
                elif ss == '}' and tmp == '{':
                    stack.pop(-1)
                elif ss == ']' and tmp == '[':
                    stack.pop(-1)
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False

s = ""
ss = Solution()
print(ss.isValid(s))
