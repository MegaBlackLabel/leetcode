#
# @lc app=leetcode id=2544 lang=python3
#
# [2544] Alternating Digit Sum
#

# @lc code=start
class Solution:
    def alternateDigitSum(self, n: int) -> int:
        ans = 0
        sign = 1

        while n > 0:
            sign *= -1
            ans += n % 10 * sign
            n //= 10

        return sign * ans
# @lc code=end

