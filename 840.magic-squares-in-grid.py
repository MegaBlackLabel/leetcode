#
# @lc app=leetcode id=840 lang=python3
#
# [840] Magic Squares In Grid
#

# @lc code=start
from typing import List


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        
        def is_magic(i: int, j: int) -> bool:
            s = set()
            for x in range(3):
                for y in range(3):
                    val = grid[i + x][j + y]
                    if val < 1 or val > 9 or val in s:
                        return False
                    s.add(val)

            target = sum(grid[i][j:j + 3])
            for x in range(3):
                if sum(grid[i + x][j:j + 3]) != target:
                    return False
            for y in range(3):
                if sum(grid[i + x][j + y] for x in range(3)) != target:
                    return False
            if sum(grid[i + k][j + k] for k in range(3)) != target:
                return False
            if sum(grid[i + k][j + 2 - k] for k in range(3)) != target:
                return False
            return True

        count = 0
        rows, cols = len(grid), len(grid[0])
        for i in range(rows - 2):
            for j in range(cols - 2):
                if is_magic(i, j):
                    count += 1
        return count
# @lc code=end

