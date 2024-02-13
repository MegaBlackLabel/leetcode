#
# @lc app=leetcode id=1779 lang=python3
#
# [1779] Find Nearest Point That Has the Same X or Y Coordinate
#

# @lc code=start
import math
from typing import List


class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        res = math.inf
        index = -1

        for i, (length, r) in enumerate(points):
            if (x-length)*(y-r) == 0 and (abs(x-length) + abs(y-r)<res):
                res = abs(x-length) + abs(y-r)
                index = i

        return index
# @lc code=end

