#
# @lc app=leetcode id=452 lang=python3
#
# [452] Minimum Number of Arrows to Burst Balloons
#

# @lc code=start
from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        points.sort(key=lambda x: x[1])
        
        arrows = 0
        current_end = float('-inf')

        for start, end in points:
            if start > current_end:
                arrows += 1
                current_end = end

        return arrows
# @lc code=end

