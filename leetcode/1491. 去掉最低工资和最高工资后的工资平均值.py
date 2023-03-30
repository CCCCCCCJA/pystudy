class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        maxSalary = max(salary)
        minSalary = min(salary)
        salary.remove(maxSalary)
        salary.remove(minSalary)
        return sum(salary) / len(salary)



salary = [4000,3000,1000,2000]
ss = Solution()
print(ss.average(salary))