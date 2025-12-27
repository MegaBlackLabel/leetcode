#
# @lc app=leetcode id=947 lang=python3
#
# [947] Most Stones Removed with Same Row or Column
#

# @lc code=start
from typing import List


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        
        parent = {}

        def find(x):
            if parent.setdefault(x, x) != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        for x, y in stones:
            union(x, ~y)

        return len(stones) - len({find(x) for x in parent})
# @lc code=end

