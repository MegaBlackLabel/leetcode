#
# @lc app=leetcode id=1281 lang=python3
#
# [1281] Subtract the Product and Sum of Digits of an Integer
#

# @lc code=start
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod = 1
        summ = 0

        while n > 0:
            prod *= n % 10
            summ += n % 10
            n //= 10

        return prod - summ
# @lc code=end

