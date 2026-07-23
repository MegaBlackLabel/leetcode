#
# @lc app=leetcode id=1131 lang=python3
#
# [1131] Maximum of Absolute Value Expression
#

# @lc code=start
from typing import List


class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        scenarios = [
            (1, 1, 1),
            (1, -1, 1),
            (1, 1, -1),
            (1, -1, -1)
        ]
        
        max_total_diff = 0
        
        for s1, s2, s3 in scenarios:
            max_val = float('-inf')
            min_val = float('inf')
            
            for i in range(len(arr1)):
                current_transformed = s1 * arr1[i] + s2 * arr2[i] + s3 * i
                
                if current_transformed > max_val:
                    max_val = current_transformed
                if current_transformed < min_val:
                    min_val = current_transformed
            
            max_total_diff = max(max_total_diff, max_val - min_val)
            
        return max_total_diff
# @lc code=end

