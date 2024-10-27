#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1

        sign = -1 if (dividend > 0) ^ (divisor > 0) else 1
        ans = 0
        dvd = abs(dividend)
        dvs = abs(divisor)

        while dvd >= dvs:
            k = 1
            while k * 2 * dvs <= dvd:
                k <<= 1
            dvd -= k * dvs
            ans += k

        return sign * ans
# @lc code=end

