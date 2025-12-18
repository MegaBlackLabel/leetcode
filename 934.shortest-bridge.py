#
# @lc app=leetcode id=934 lang=python3
#
# [934] Shortest Bridge
#

# @lc code=start
from typing import List


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def in_bounds(r: int, c: int) -> bool:
            return 0 <= r < rows and 0 <= c < cols

        def dfs(r: int, c: int):
            if not in_bounds(r, c) or grid[r][c] != 1:
                return
            grid[r][c] = 2
            island.append((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        island = []
        found = False
        for r in range(rows):
            if found:
                break
            for c in range(cols):
                if grid[r][c] == 1:
                    dfs(r, c)
                    found = True
                    break

        queue = island[:]
        steps = 0
        while queue:
            next_queue = []
            for r, c in queue:
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if in_bounds(nr, nc):
                        if grid[nr][nc] == 1:
                            return steps
                        elif grid[nr][nc] == 0:
                            grid[nr][nc] = -1
                            next_queue.append((nr, nc))
            queue = next_queue
            steps += 1

        return -1
# @lc code=end

