class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        # fuhao = ['+', '-', '*', '/']
        # while 1:
        #     count = 0
        #     tag = 0
        #     for i in range(len(tokens)):
        #         if tokens[i] in fuhao:
        #             flag = fuhao.index(tokens[i])
        #             if flag == 0:
        #                 tmpnum = int(tokens[i-2]) + int(tokens[i-1])
        #             elif flag == 1:
        #                 tmpnum = int(tokens[i-2]) - int(tokens[i-1])
        #             elif flag == 2:
        #                 tmpnum = int(tokens[i-2]) * int(tokens[i-1])
        #             else:
        #                 tmpnum = int(tokens[i-2]) / int(tokens[i-1])
        #             tokens.pop(i)
        #             tokens.pop(i-1)
        #             tokens[i-2] = str(int(tmpnum))
        #             tag += 1
        #             break
        #         else:
        #             count += 1
        #     if tag != 0:
        #         continue
        #     if count == len(tokens):
        #         break
        # print(tokens[0])
        # 使用栈进行辅助
        stack = []
        fuhao = ['+', '-', '*', '/']
        for i in range(len(tokens)):
            if tokens[i] not in fuhao:
                stack.append(int(tokens[i]))
            else:
                num1 = stack.pop(-1)
                num2 = stack.pop(-1)
                flag = fuhao.index(tokens[i])
                if flag == 0:
                    tmpnum = num2 + num1
                elif flag == 1:
                    tmpnum = num2 - num1
                elif flag == 2:
                    tmpnum = num2 * num1
                else:
                    tmpnum = num2 / num1
                stack.append(int(tmpnum))
        print(stack[0])
        return stack[0]



tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
ss = Solution()
ss.evalRPN(tokens)
