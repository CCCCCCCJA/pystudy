class Solution(object):
    def uniqueOccurrences(self, arr):
        arr.sort()
        print(arr)
        tag = arr[0]
        cont_list = []
        count = 1
        for i in range(1, len(arr)):
            if tag == arr[i]:
                count += 1
            else:
                tag = arr[i]
                cont_list.append(count)
                count = 1
        cont_list.append(count)
        len_list = len(cont_list)
        cont_set = set(cont_list)
        len_set = len(cont_set)
        if len_list == len_set:
            return True
        else:
            return False

arr = [1,2,2,1,1,3]
ss = Solution()
print(ss.uniqueOccurrences(arr))