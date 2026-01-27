#
# @lc app=leetcode id=990 lang=python3
#
# [990] Satisfiability of Equality Equations
#

# @lc code=start
from typing import List


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        
        parent = {}

        def find(x):
            if parent.setdefault(x, x) != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        for eq in equations:
            if eq[1:3] == "==":
                union(eq[0], eq[3])

        for eq in equations:
            if eq[1:3] == "!=":
                if find(eq[0]) == find(eq[3]):
                    return False

        return True
# @lc code=end

