#
# @lc app=leetcode id=1034 lang=python3
#
# [1034] Coloring A Border
#

# @lc code=start
from typing import List


class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        original_color = grid[row][col]
        visited = set()
        border_cells = []
        
        def dfs(r, c):
            visited.add((r, c))
            is_border = False
            
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < m and 0 <= nc < n:
                    if grid[nr][nc] != original_color:
                        if (nr, nc) not in visited:
                            is_border = True
                    elif (nr, nc) not in visited:
                        dfs(nr, nc)
                else:
                    is_border = True
                    
            if is_border:
                border_cells.append((r, c))

        dfs(row, col)
        
        for r, c in border_cells:
            grid[r][c] = color
            
        return grid
# @lc code=end

