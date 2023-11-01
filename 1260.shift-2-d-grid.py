#
# @lc app=leetcode id=1260 lang=python3
#
# [1260] Shift 2D Grid
#

# @lc code=start
from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        ans = [[0] * n for _ in range(m)]

        k %= m * n

        for i in range(m):
            for j in range(n):
                index = (i * n + j + k) % (m * n)
                x = index // n
                y = index % n
                ans[x][y] = grid[i][j]

        return ans
# @lc code=end

