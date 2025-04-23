#
# @lc app=leetcode id=427 lang=python3
#
# [427] Construct Quad Tree
#

# @lc code=start

# Definition for a QuadTree node.
from typing import List


class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        
        def isLeaf(x1, y1, x2, y2):
            val = grid[x1][y1]
            for i in range(x1, x2):
                for j in range(y1, y2):
                    if grid[i][j] != val:
                        return False
            return True

        def build(x1, y1, x2, y2):
            if isLeaf(x1, y1, x2, y2):
                return Node(grid[x1][y1] == 1, True, None, None, None, None)
            mid_x = (x1 + x2) // 2
            mid_y = (y1 + y2) // 2
            return Node(
                True,
                False,
                build(x1, y1, mid_x, mid_y),
                build(x1, mid_y, mid_x, y2),
                build(mid_x, y1, x2, mid_y),
                build(mid_x, mid_y, x2, y2),
            )

        return build(0, 0, len(grid), len(grid[0]))
# @lc code=end

