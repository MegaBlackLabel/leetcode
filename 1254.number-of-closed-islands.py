#
# @lc app=leetcode id=1254 lang=python3
#
# [1254] Number of Closed Islands
#

# @lc code=start
class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        
        def dfs(r: int, c: int) -> int:
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return 0
            if grid[r][c] == 1:
                return 1
            
            grid[r][c] = 1
            
            up = dfs(r - 1, c)
            down = dfs(r + 1, c)
            left = dfs(r, c - 1)
            right = dfs(r, c + 1)
            
            return up and down and left and right

        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    count += dfs(r, c)
        return count
# @lc code=end

