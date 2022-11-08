class Solution(object):
    def countGoodTriplets(self, arr, a, b, c):
        lenlen = len(arr)
        count = 0
        for i in range(lenlen-2):
            for j in range(i+1, lenlen-1):
                for k in range(j+1, lenlen):
                    if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <=b and abs(arr[i] - arr[k]) <= c:
                        count += 1
        return count