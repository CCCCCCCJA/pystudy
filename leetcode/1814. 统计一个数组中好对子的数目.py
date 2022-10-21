# 时间复杂度过高
# class Solution(object):
#     def countNicePairs(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         count = 0
#         len_len = len(nums)
#         for i in range(len_len):
#             for j in range(i+1, len_len):
#                 if nums[i] + self.rev(nums[j]) == nums[j] + self.rev(nums[i]):
#                     count += 1
#         print(count)
#         return count
#     def rev(self, x):
#         x_s = str(x)
#         x_s = x_s[::-1]
#         tag = 0
#         flag = 0
#         for s in x_s:
#             if (flag == 0) & (s != '0'):
#                 flag = 1
#             if (s == '0') & (flag == 0):
#                 tag += 1
#             if flag == 1:
#                 break
#         x_s = x_s[tag:]
#         x_s = int(x_s)
#         # print(x_s, tag)
#         return x_s
class Solution(object):
    def countNicePairs(self, nums):
        res = {}
        num = []
        count = 0
        for n in nums:
            res_num = n - self.rev(n)
            if res_num in res:
                tmp = res.get(res_num)
                res[res_num] = tmp + 1
            else:
                res[res_num] = 1
                num.append(res_num)
        for s in num:
            tmp = res.get(s)
            # print(tmp)
            count += int((tmp * (tmp - 1)) / 2)
        # print(count % (10**9 + 7))
        return count % (10**9 + 7)

    def rev(self, x):
        x_s = str(x)
        x_s = x_s[::-1]
        tag = 0
        flag = 0
        for s in x_s:
            if (flag == 0) & (s != '0'):
                flag = 1
            if (s == '0') & (flag == 0):
                tag += 1
            if flag == 1:
                break
        if x > 0:
            x_s = x_s[tag:]
        x_s = int(x_s)
        # print(x_s, tag)
        return x_s
nums = [352171103,442454244,42644624,152727101,413370302,293999243]
ss = Solution()
ss.countNicePairs(nums)