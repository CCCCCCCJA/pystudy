class Solution(object):
    def maximumTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        index = []
        tmp = time
        for i in range(len(time)):
            if time[i] == '?':
                index.append(i)
        print(index)
        for i in index:
            if i == 0:
                # if time[1] > 3:
                #     time = time.replace('?', '1', 1)
                # elif time[1] <= 3:
                #     time = time.replace('?', '2', 1)
                # else:
                #     time = time.replace('??', '23', 1)
                if (time[0] + time[1]) == '??':
                    time = time.replace('?', '2', 1)
                elif (time[1] == '0') | (time[1] == '1') | (time[1] == '2') | (time[1] == '3'):
                    time = time.replace('?', '2', 1)
                else:
                    time = time.replace('?', '1', 1)
            if i == 1:
                if (time[0] == '1') | (time[0] == '0'):
                    time = time.replace('?', '9', 1)
                else:
                    time = time.replace('?', '3', 1)
            if i == 3:
                time = time.replace('?', '5', 1)
            if i == 4:
                time = time.replace('?', '9', 1)
        print(time)
        return time

time = "?0:15"
ss = Solution()
ss.maximumTime(time)