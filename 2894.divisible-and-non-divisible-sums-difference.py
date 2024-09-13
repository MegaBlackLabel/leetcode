#
# @lc app=leetcode id=2894 lang=python3
#
# [2894] Divisible and Non-divisible Sums Difference
#

# @lc code=start
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        summ = (1 + n) * n // 2
        num2 = self._getDivisibleSum(n, m)
        num1 = summ - num2
        return num1 - num2

    def _getDivisibleSum(self, n: int, m: int) -> int:
        last = n // m * m
        if last == 0:
            return 0
        first = m
        count = (last - first) // m + 1
        return (first + last) * count // 2
# @lc code=end

