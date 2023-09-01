#
# @lc app=leetcode id=892 lang=python3
#
# [892] Surface Area of 3D Shapes
#

# @lc code=start
from typing import List


class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        ans = 0

        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j]:
                    ans += grid[i][j] * 4 + 2
                if i > 0:
                    ans -= min(grid[i][j], grid[i - 1][j]) * 2
                if j > 0:
                    ans -= min(grid[i][j], grid[i][j - 1]) * 2

        return ans
# @lc code=end

