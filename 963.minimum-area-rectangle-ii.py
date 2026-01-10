#
# @lc app=leetcode id=963 lang=python3
#
# [963] Minimum Area Rectangle II
#

# @lc code=start
from typing import List


class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        
        point_set = set(map(tuple, points))
        min_area = float('inf')

        for i in range(len(points)):
            for j in range(len(points)):
                for k in range(len(points)):
                    if i == j or j == k or i == k:
                        continue

                    p1, p2, p3 = points[i], points[j], points[k]

                    v1 = (p2[0] - p1[0], p2[1] - p1[1])
                    v2 = (p3[0] - p1[0], p3[1] - p1[1])

                    dot_product = v1[0] * v2[0] + v1[1] * v2[1]
                    if dot_product != 0:
                        continue

                    p4 = (p3[0] + v1[0], p3[1] + v1[1])
                    if p4 in point_set:
                        area = (v1[0] ** 2 + v1[1] ** 2) ** 0.5 * (v2[0] ** 2 + v2[1] ** 2) ** 0.5
                        min_area = min(min_area, area)

        return min_area if min_area != float('inf') else 0.0
# @lc code=end

