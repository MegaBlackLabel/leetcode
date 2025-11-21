#
# @lc app=leetcode id=886 lang=python3
#
# [886] Possible Bipartition
#

# @lc code=start
from typing import List


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        graph = [[] for _ in range(n + 1)]
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)

        color = [0] * (n + 1)

        def dfs(node: int, c: int) -> bool:
            color[node] = c
            for neighbor in graph[node]:
                if color[neighbor] == c:
                    return False
                if color[neighbor] == 0 and not dfs(neighbor, -c):
                    return False
            return True

        for i in range(1, n + 1):
            if color[i] == 0 and not dfs(i, 1):
                return False

        return True
# @lc code=end

