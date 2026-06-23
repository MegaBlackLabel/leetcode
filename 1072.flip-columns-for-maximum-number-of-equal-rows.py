#
# @lc app=leetcode id=1072 lang=python3
#
# [1072] Flip Columns For Maximum Number of Equal Rows
#

# @lc code=start
from collections import defaultdict
from typing import List


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        counts = defaultdict(int)
        
        for row in matrix:
        
            if row[0] == 1:
                normalized_row = tuple(1 - val for val in row)
            else:
                normalized_row = tuple(row)
                
            counts[normalized_row] += 1
            
        return max(counts.values())
# @lc code=end

