#
# @lc app=leetcode id=2180 lang=python3
#
# [2180] Count Integers With Even Digit Sum
#

# @lc code=start
class Solution:
    def countEven(self, num: int) -> int:
        return (num - self._getDigitSum(num) % 2) // 2

    def _getDigitSum(self, num: int) -> int:
        return sum(int(digit) for digit in str(num))
# @lc code=end

