#
# @lc app=leetcode id=1413 lang=python3
#
# [1413] Minimum Value to Get Positive Step by Step Sum
#

# @lc code=start
from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        summ = 0
        minSum = 0

        for num in nums:
            summ += num
            minSum = min(minSum, summ)

        return 1 - minSum
# @lc code=end

