#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#

# @lc code=start
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        if not heights:
            return []

        rows, cols = len(heights), len(heights[0])
        pacific = [[False] * cols for _ in range(rows)]
        atlantic = [[False] * cols for _ in range(rows)]

        def dfs(r, c, visited):
            visited[r][c] = True
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and heights[nr][nc] >= heights[r][c]:
                    dfs(nr, nc, visited)

        for i in range(rows):
            dfs(i, 0, pacific)
            dfs(i, cols - 1, atlantic)

        for j in range(cols):
            dfs(0, j, pacific)
            dfs(rows - 1, j, atlantic)

        return [[i, j] for i in range(rows) for j in range(cols) if pacific[i][j] and atlantic[i][j]]
# @lc code=end

