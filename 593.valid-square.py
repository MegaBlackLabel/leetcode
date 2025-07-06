#
# @lc app=leetcode id=593 lang=python3
#
# [593] Valid Square
#

# @lc code=start
from typing import List


class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        
        def dist_sq(p1, p2):
            return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

        points = [p1, p2, p3, p4]
        dists = sorted(dist_sq(points[i], points[j])
                       for i in range(4) for j in range(i + 1, 4))

        # A valid square has 4 equal sides and 2 equal diagonals
        return (dists[0] > 0 and
                dists[0] == dists[1] == dists[2] == dists[3] and
                dists[4] == dists[5] and
                dists[4] > dists[0])
# @lc code=end

