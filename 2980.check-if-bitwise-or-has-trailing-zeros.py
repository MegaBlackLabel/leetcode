#
# @lc app=leetcode id=2980 lang=python3
#
# [2980] Check if Bitwise OR Has Trailing Zeros
#

# @lc code=start
from typing import List


class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        return sum(num % 2 == 0 for num in nums) >= 2
# @lc code=end

