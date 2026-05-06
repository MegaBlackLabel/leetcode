#
# @lc app=leetcode id=3402 lang=python3
#
# [3402] Minimum Operations to Make Columns Strictly Increasing
#

# @lc code=start
from typing import List


class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        total_ops = 0
        
        for j in range(cols):
            for i in range(1, rows):
                if grid[i][j] <= grid[i-1][j]:
                    target_val = grid[i-1][j] + 1
                    total_ops += (target_val - grid[i][j])
                    grid[i][j] = target_val
                    
        return total_ops
# @lc code=end

