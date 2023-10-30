#
# @lc app=leetcode id=1232 lang=python3
#
# [1232] Check If It Is a Straight Line
#

# @lc code=start
from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x0, y0, x1, y1 = *coordinates[0], *coordinates[1]
        dx = x1 - x0
        dy = y1 - y0

        return all((x - x0) * dy == (y - y0) * dx for x, y in coordinates)
# @lc code=end

