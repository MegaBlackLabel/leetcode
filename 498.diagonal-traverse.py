#
# @lc app=leetcode id=498 lang=python3
#
# [498] Diagonal Traverse
#

# @lc code=start
from collections import defaultdict
from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        if mat is None or mat == []: 
            return []
        
        res = []
        lines = defaultdict(list)
        rows = len(mat)
        cols = len(mat[0])
        for i in range(rows):
            for j in range(cols):
                lines[i+j].append(mat[i][j])
        for k in range(rows + cols - 1):
            if k % 2 == 0:
                res += lines[k][::-1]
            else:
                res += lines[k]
        return res
# @lc code=end

