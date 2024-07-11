#
# @lc app=leetcode id=2535 lang=python3
#
# [2535] Difference Between Element Sum and Digit Sum of an Array
#

# @lc code=start
from typing import List


class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        elementSum = sum(nums)
        digitSum = self._getAllDigitSum(nums)
        return abs(elementSum - digitSum)

    def _getAllDigitSum(self, nums: List[int]) -> int:
        return sum(self._getDigitSum(num) for num in nums)

    def _getDigitSum(self, num: int) -> int:
        return sum(int(digit) for digit in str(num))
# @lc code=end

