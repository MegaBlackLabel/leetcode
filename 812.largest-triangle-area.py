#
# @lc app=leetcode id=812 lang=python3
#
# [812] Largest Triangle Area
#

# @lc code=start
from typing import List


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        ans = 0

        for Ax, Ay in points:
            for Bx, By in points:
                for Cx, Cy in points:
                    ans = max(ans, 0.5 * abs((Bx - Ax) * (Cy - Ay) -
                                            (Cx - Ax) * (By - Ay)))

        return ans
# @lc code=end

