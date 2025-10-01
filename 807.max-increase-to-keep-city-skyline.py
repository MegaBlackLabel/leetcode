#
# @lc app=leetcode id=807 lang=python3
#
# [807] Max Increase to Keep City Skyline
#

# @lc code=start
from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        m = len(grid[0])
        row_max = [max(row) for row in grid]
        col_max = [max(grid[i][j] for i in range(n)) for j in range(m)]
        total_increase = 0

        for i in range(n):
            for j in range(m):
                allowed_height = min(row_max[i], col_max[j])
                total_increase += allowed_height - grid[i][j]

        return total_increase
# @lc code=end

