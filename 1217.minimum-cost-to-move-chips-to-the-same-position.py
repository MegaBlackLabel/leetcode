#
# @lc app=leetcode id=1217 lang=python3
#
# [1217] Minimum Cost to Move Chips to The Same Position
#

# @lc code=start
from typing import List


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        count = [0] * 2

        for p in position:
            count[p % 2] += 1

        return min(count[0], count[1])
# @lc code=end

