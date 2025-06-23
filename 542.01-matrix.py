#
# @lc app=leetcode id=542 lang=python3
#
# [542] 01 Matrix
#

# @lc code=start
from typing import List
from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        rows, cols = len(mat), len(mat[0])
        queue = deque()
        distances = [[float('inf')] * cols for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    queue.append((r, c))
                    distances[r][c] = 0

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if distances[nr][nc] > distances[r][c] + 1:
                        distances[nr][nc] = distances[r][c] + 1
                        queue.append((nr, nc))

        return distances
# @lc code=end

