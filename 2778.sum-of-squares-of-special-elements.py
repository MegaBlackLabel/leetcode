#
# @lc app=leetcode id=2778 lang=python3
#
# [2778] Sum of Squares of Special Elements 
#

# @lc code=start
from typing import List


class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        return sum(num**2 for i, num in enumerate(nums)
               if len(nums) % (i + 1) == 0)
# @lc code=end

