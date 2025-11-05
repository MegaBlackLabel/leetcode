#
# @lc app=leetcode id=861 lang=python3
#
# [861] Score After Flipping Matrix
#

# @lc code=start
from typing import List


class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            if grid[r][0] == 0:
                for c in range(cols):
                    grid[r][c] ^= 1

        for c in range(1, cols):
            count_ones = sum(grid[r][c] for r in range(rows))
            if count_ones < rows / 2:
                for r in range(rows):
                    grid[r][c] ^= 1

        total_score = 0
        for r in range(rows):
            row_value = 0
            for c in range(cols):
                row_value = (row_value << 1) | grid[r][c]
            total_score += row_value

        return total_score
# @lc code=end

