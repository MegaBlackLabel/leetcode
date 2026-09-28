#
# @lc app=leetcode id=1267 lang=python3
#
# [1267] Count Servers that Communicate
#

# @lc code=start
class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        row_counts = [0] * rows
        col_counts = [0] * cols
      
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    row_counts[i] += 1
                    col_counts[j] += 1
      
        connected_servers = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (row_counts[i] > 1 or col_counts[j] > 1):
                    connected_servers += 1
      
        return connected_servers
# @lc code=end

