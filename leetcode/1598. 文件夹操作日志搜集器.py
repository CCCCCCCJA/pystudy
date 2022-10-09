class Solution(object):
    def minOperations(self, logs):
        count = 0
        for log in logs:
            if(log == '../'):
                count-=1
            elif(log == './'):
                count = count
            else:
                count+=1
        return count
logs = ["d1/","d2/","../","d21/","./"]
ss = Solution()
print(ss.minOperations(logs))