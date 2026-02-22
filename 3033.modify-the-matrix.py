#
# @lc app=leetcode id=3033 lang=python3
#
# [3033] Modify the Matrix
#

# @lc code=start
from typing import List


class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        
        m = len(matrix)
        n = len(matrix[0])
    
        for j in range(n):
            # 1. その列の最大値を探す
            max_val = 0
            for i in range(m):
                max_val = max(max_val, matrix[i][j])
            
            # 2. -1を最大値に置き換える
            for i in range(m):
                if matrix[i][j] == -1:
                    matrix[i][j] = max_val
                
        return matrix
# @lc code=end

