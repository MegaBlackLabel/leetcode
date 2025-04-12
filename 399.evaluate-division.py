#
# @lc app=leetcode id=399 lang=python3
#
# [399] Evaluate Division
#

# @lc code=start
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        graph = {}
        for (a, b), value in zip(equations, values):
            if a not in graph:
                graph[a] = {}
            if b not in graph:
                graph[b] = {}
            graph[a][b] = value
            graph[b][a] = 1 / value

        def dfs(a, b, visited):
            if a not in graph or b not in graph:
                return -1.0
            if a == b:
                return 1.0
            visited.add(a)
            for neighbor, value in graph[a].items():
                if neighbor not in visited:
                    result = dfs(neighbor, b, visited)
                    if result != -1.0:
                        return result * value
            return -1.0

        results = []
        for a, b in queries:
            results.append(dfs(a, b, set()))

        return results
        

# @lc code=end

