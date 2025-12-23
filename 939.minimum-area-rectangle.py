#
# @lc app=leetcode id=939 lang=python3
#
# [939] Minimum Area Rectangle
#

# @lc code=start
from typing import List


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        
        point_set = set(map(tuple, points))
        min_area = float('inf')

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                p1, p2 = points[i], points[j]
                if p1[0] != p2[0] and p1[1] != p2[1]:
                    if (p1[0], p2[1]) in point_set and (p2[0], p1[1]) in point_set:
                        area = abs(p1[0] - p2[0]) * abs(p1[1] - p2[1])
                        min_area = min(min_area, area)

        return min_area if min_area != float('inf') else 0
# @lc code=end

