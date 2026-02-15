#
# @lc app=leetcode id=1020 lang=python3
#
# [1020] Number of Enclaves
#

# @lc code=start
from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        
        def dfs(row: int, col: int) -> None:
            grid[row][col] = 0
            

            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            for delta_row, delta_col in directions:
                new_row = row + delta_row
                new_col = col + delta_col

                if (0 <= new_row < rows and 
                    0 <= new_col < cols and 
                    grid[new_row][new_col] == 1):
                    dfs(new_row, new_col)
      

        rows = len(grid)
        cols = len(grid[0])
      
        for col in range(cols):
            if grid[0][col] == 1:
                dfs(0, col)
            if grid[rows - 1][col] == 1:
                dfs(rows - 1, col)
      
       
        for row in range(1, rows - 1):
            if grid[row][0] == 1:
                dfs(row, 0)
            if grid[row][cols - 1] == 1:
                dfs(row, cols - 1)
      
        total_enclaves = 0
        for row in grid:
            total_enclaves += sum(row)
      
        return total_enclaves
# @lc code=end

