#
# @lc app=leetcode id=785 lang=python3
#
# [785] Is Graph Bipartite?
#

# @lc code=start
from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        n = len(graph)
        color = [0] * n

        def dfs(node: int, c: int) -> bool:
            color[node] = c
            for neighbor in graph[node]:
                if color[neighbor] == 0:
                    if not dfs(neighbor, -c):
                        return False
                elif color[neighbor] == c:
                    return False
            return True

        for i in range(n):
            if color[i] == 0:
                if not dfs(i, 1):
                    return False
        return True
# @lc code=end

