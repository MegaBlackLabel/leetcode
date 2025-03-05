#
# @lc app=leetcode id=310 lang=python3
#
# [310] Minimum Height Trees
#

# @lc code=start
import collections
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1 or not edges:
            return [0]

        ans = []
        graph = collections.defaultdict(set)

        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        for label, children in graph.items():
            if len(children) == 1:
                ans.append(label)
        
        while n > 2:
            n -= len(ans)
            new_leaves = []
            for leaf in ans:
                parent = graph[leaf].pop()
                graph[parent].remove(leaf)
                if len(graph[parent]) == 1:
                    new_leaves.append(parent)
            ans = new_leaves
        
        return ans

# @lc code=end

