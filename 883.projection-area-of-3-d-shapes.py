#
# @lc app=leetcode id=883 lang=python3
#
# [883] Projection Area of 3D Shapes
#

# @lc code=start
from typing import List


class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        return sum(a > 0 for row in grid for a in row) + sum(max(row) for row in grid) + sum(max(col) for col in zip(*grid))
# @lc code=end

