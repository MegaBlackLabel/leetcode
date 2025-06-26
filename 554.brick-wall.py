#
# @lc app=leetcode id=554 lang=python3
#
# [554] Brick Wall
#

# @lc code=start
from typing import List
from collections import defaultdict

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        
        edge_count = defaultdict(int)

        for row in wall:
            edge = 0
            for brick in row[:-1]:
                edge += brick
                edge_count[edge] += 1

        if not edge_count:
            return len(wall)
        max_edges = max(edge_count.values())
        return len(wall) - max_edges
# @lc code=end

