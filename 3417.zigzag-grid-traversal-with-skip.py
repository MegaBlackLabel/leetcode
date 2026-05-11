#
# @lc app=leetcode id=3417 lang=python3
#
# [3417] Zigzag Grid Traversal With Skip
#

# @lc code=start
from typing import List


class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        result = []
        skip = False
        
        for r in range(len(grid)):
            row_elements = grid[r] if r % 2 == 0 else grid[r][::-1]
            
            for val in row_elements:
                if not skip:
                    result.append(val)
                skip = not skip
                
        return result
# @lc code=end

