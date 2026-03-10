#
# @lc app=leetcode id=3127 lang=python3
#
# [3127] Make a Square with the Same Color
#

# @lc code=start
from typing import List


class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        for r in range(2):
            for c in range(2):
                black_count = 0
                white_count = 0
                
                for i in range(r, r + 2):
                    for j in range(c, c + 2):
                        if grid[i][j] == 'B':
                            black_count += 1
                        else:
                            white_count += 1
                
                if black_count >= 3 or white_count >= 3:
                    return True
        
        return False
# @lc code=end

