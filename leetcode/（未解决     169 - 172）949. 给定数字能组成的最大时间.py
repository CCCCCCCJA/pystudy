class Solution(object):
    def largestTimeFromDigits(self, arr):
        """
        :type arr: List[int]
        :rtype: str
        """
        res = ''
        if 2 in arr:
            if 1 in arr or 3 in arr or arr.count(2) >= 2 or 0 in arr:
                res += '2'
                arr.remove(2)
                if 3 in arr:
                    res += '3'
                    arr.remove(3)
                elif arr.count(2) >= 2:
                    res += '2'
                    arr.remove(2)
                elif 1 in arr:
                    res += '1'
                    arr.remove(1)
                else:
                    res += '0'
                    arr.remove(0)
            elif 1 in arr:
                res += '1'
                arr.remove(1)
                maxn = max(arr)
                res += str(maxn)
                arr.remove(maxn)
                # res += ':'
            elif 0 in arr:
                res += '0'
                maxn = max(arr)
                res += str(maxn)
                arr.remove(0)
                arr.remove(maxn)
                # res += ':'
            else:
                return ''
            res += ':'
        elif 1 in arr:
            res += '1'
            arr.remove(1)
            maxn = max(arr)
            res += str(maxn)
            arr.remove(maxn)
            res += ':'
        elif 0 in arr:
            res += '0'
            maxn = max(arr)
            res += str(maxn)
            arr.remove(0)
            arr.remove(maxn)
            res += ':'
        else:
            return ''
        arr.sort()
        arr = arr[::-1]
        for ar in arr:
            res += str(ar)
        return res
arr = [2,0,6,6]
ss = Solution()
ss.largestTimeFromDigits(arr)
