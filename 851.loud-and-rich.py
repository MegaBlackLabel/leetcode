#
# @lc app=leetcode id=851 lang=python3
#
# [851] Loud and Rich
#

# @lc code=start
from typing import List


class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        
        n = len(quiet)
        graph = [[] for _ in range(n)]
        for u, v in richer:
            graph[v].append(u)

        ans = [-1] * n

        def dfs(node: int) -> int:
            if ans[node] != -1:
                return ans[node]

            ans[node] = node
            for neighbor in graph[node]:
                candidate = dfs(neighbor)
                if quiet[candidate] < quiet[ans[node]]:
                    ans[node] = candidate

            return ans[node]

        for i in range(n):
            dfs(i)

        return ans
# @lc code=end

