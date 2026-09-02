#
# @lc app=leetcode id=1219 lang=python3
#
# [1219] Path with Maximum Gold
#

# @lc code=start
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        max_gold = 0

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0:
                return 0
            
            current_gold = grid[r][c]
            original_val = current_gold
            grid[r][c] = 0  
            
            local_max = 0
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                local_max = max(local_max, dfs(r + dr, c + dc))
                
            grid[r][c] = original_val  
            return current_gold + local_max

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] > 0:
                    max_gold = max(max_gold, dfs(r, c))

        return max_gold
# @lc code=end

