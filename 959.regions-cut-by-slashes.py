#
# @lc app=leetcode id=959 lang=python3
#
# [959] Regions Cut By Slashes
#

# @lc code=start
from typing import List


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        parent = {}
        def find(x):
            parent.setdefault(x, x)
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootY] = rootX
        
        for i in range(n):
            for j in range(n):
                if i > 0:
                    union((i-1, j, 2), (i, j, 0))
                if j > 0:
                    union((i, j-1, 1), (i, j, 3))
                
               
                if grid[i][j] == '/':
                    union((i, j, 0), (i, j, 3))
                    union((i, j, 1), (i, j, 2))
                elif grid[i][j] == '\\':
                    union((i, j, 0), (i, j, 1))
                    union((i, j, 2), (i, j, 3))
                else:
                    union((i, j, 0), (i, j, 1))
                    union((i, j, 1), (i, j, 2))
                    union((i, j, 2), (i, j, 3))
                    union((i, j, 3), (i, j, 0))

        roots = set()
        for key in parent:
            roots.add(find(key))
        
        return len(roots)
# @lc code=end

