# 直接枚举   超时超时超时超时超时超时超时超时超时超时超时超时超时超时超时超时超时超时超时超时超时超时超时超时！！！！！！！！
# class Solution:
#     def countPrimes(self, n):
#         nums = list(range(n))
#         count = 0
#         print(nums)
#         tag = 1
#         for num in nums:
#             if num > 1:
#                 for i in range(2, num):
#                     if num % i == 0:
#                         tag = 0
#                         break
#                 if tag:
#                     count += 1
#             tag = 1
#         # print(count)
#         return count
class Solution:
    def countPrimes(self, n: int) -> int:
        # 定义数组标记是否是质数
        is_prime = [1] * n
        is_prime[0] = is_prime[1] = 0
        print(is_prime)
        count = 0
        for i in range(2, n):
            # 将质数的倍数标记为合数
            if is_prime[i]:
                count += 1
                # 从 i*i 开始标记
                for j in range(i * i, n, i):
                    is_prime[j] = 0
        print(is_prime)
        return count

n = 1000
ss = Solution()
print(ss.countPrimes(n))